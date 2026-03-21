import asyncio
import structlog
import time
from typing import Dict, Any, List, cast
from pydantic import ValidationError

from companies.domain.entities import Company
from companies.domain.ports.b3_data_source import B3DataSource
from companies.domain.ports.company_repository import CompanyRepository
from companies.domain.exceptions import (
    CompanyValidationError,
    CompanyDataValidationError,
    B3RateLimitExceededError,
    B3NetworkTimeoutError,
)
from companies.application.mappers.b3_mapper import B3CompanyMapper
from shared.infrastructure.config import settings
from shared.domain.ports.telemetry_port import TelemetryPort
from shared.infrastructure.progress import ProgressReporter
from shared.domain.utils.result import Result

logger = structlog.get_logger().bind(bounded_context="companies")


class SyncB3CompaniesUseCase:
    """Application Use Case for synchronizing the B3 Issuer Catalog.

    This use case serves as the primary orchestrator for the B3 Bounded Context.
    It ensures that raw data from external scraping is refined through an
    Anti-Corruption Layer (ACL) before being admitted into the Domain.
    """

    def __init__(
        self,
        data_source: B3DataSource,
        repository: CompanyRepository,
        telemetry: TelemetryPort,
    ):
        """Initializes the use case with required Ports.

        Args:
            data_source (B3DataSource): Port for fetching market data.
            repository (CompanyRepository): Port for persisting validated entities.
            telemetry (TelemetryPort): Port for capturing SRE and business metrics.
        """
        self._data_source = data_source
        self._repository = repository
        self._telemetry = telemetry

    async def _process_single_company(
        self,
        index: int,
        raw_company: Dict[str, Any],
        semaphore: asyncio.Semaphore,
        reporter: ProgressReporter,
    ) -> Result[Company, Exception]:
        """Helper to process a single company using Result Monad."""
        ticker = raw_company.get("issuingCompany")
        cvm_code = str(raw_company.get("codeCVM"))

        if not ticker or not cvm_code.isdigit():
            return Result.fail(
                CompanyDataValidationError(
                    "Missing Ticker or invalid CVM", "cvm_code", ticker
                )
            )

        async with semaphore:
            try:
                # 1. Infrastructure: Detail fetch
                details = await self._data_source.fetch_company_details(cvm_code)

                # 2. Application: Mapping & Validation (ACL Mapper -> Entity)
                entity = B3CompanyMapper.to_domain(
                    raw_company, details, self._telemetry
                )

                logger.debug(reporter.get_formatted_progress(index, [ticker]))
                return Result.ok(entity)
            except ValidationError as e:
                return Result.fail(
                    CompanyDataValidationError(
                        f"DTO Validation failed: {e}", "multiple", ticker
                    )
                )
            except CompanyValidationError as e:
                return Result.fail(e)
            except B3RateLimitExceededError as e:
                return Result.fail(e)
            except (asyncio.TimeoutError, TimeoutError):
                return Result.fail(
                    B3NetworkTimeoutError(
                        f"Timeout fetching details for {ticker} ({cvm_code})"
                    )
                )
            except Exception as e:
                # Catch-all for unexpected infrastructure level errors
                return Result.fail(e)

    async def execute(self) -> None:
        """Executes the complete synchronization workflow.

        Nested Logical Steps:
            1. Saturation tracking: Increment active task gauge.
            2. Data Discovery: Fetch the initial issuer list.
            3. Concurrency Orchestration: Execute detail probes via semaphore.
            4. Error Taxonomy: Categorize failures for proactive alerting.
            5. Persistence: Commit valid entities to the repository in bulk.
        """
        logger.info("Starting B3 Companies Synchronization")
        start_time = time.perf_counter()

        # 1. SATURATION: Mark task as active
        self._telemetry.increment_active_sync_tasks()

        try:
            async with self._data_source:
                # Fetch the raw initial list
                initial_companies = await self._data_source.fetch_initial_companies()

                semaphore = asyncio.Semaphore(settings.app.max_concurrency)
                reporter = ProgressReporter(total=len(initial_companies))

                # Execute all tasks concurrently
                tasks = [
                    self._process_single_company(i, raw, semaphore, reporter)
                    for i, raw in enumerate(initial_companies)
                ]
                results = await asyncio.gather(*tasks)

                # Unpack Monad
                success_list: List[Company] = []
                failure_list: List[Exception] = []

                for r in results:
                    if r.is_success and r.value:
                        success_list.append(r.value)
                    elif r.is_failure and r.error:
                        failure_list.append(r.error)

                # 2. SRE: Telemetry for Errors (Taxonomy-driven)
                for error in failure_list:
                    if isinstance(error, CompanyDataValidationError):
                        # Use cast to help Pyre identify the attributes
                        val_error = cast(CompanyDataValidationError, error)
                        self._telemetry.increment_data_validation_error(
                            entity="Company",
                            field=val_error.field,
                            reason="b3_payload_mismatch",
                        )
                    elif isinstance(error, CompanyValidationError):
                        self._telemetry.increment_data_validation_error(
                            entity="Company",
                            field="domain_logic",
                            reason="business_rule_violation",
                        )
                    elif isinstance(error, B3RateLimitExceededError):
                        self._telemetry.increment_b3_rate_limit_hits()
                    elif isinstance(error, B3NetworkTimeoutError):
                        self._telemetry.increment_generic_sync_error(
                            type="NetworkTimeout"
                        )
                    else:
                        self._telemetry.increment_generic_sync_error(
                            type=error.__class__.__name__
                        )

                # 3. Persistence & Outcome Telemetry
                if success_list:
                    # Deduplicate by ticker
                    unique_entities = list({e.ticker: e for e in success_list}.values())
                    logger.info(
                        f"Persistence: Saving {len(unique_entities)} unique companies."
                    )
                    await self._repository.save_batch(unique_entities)
                    self._telemetry.increment_companies_synced(
                        count=len(unique_entities), status="success"
                    )

                if failure_list:
                    logger.warning(
                        f"SRE Alert: {len(failure_list)} companies failed synchronization."
                    )
                    self._telemetry.increment_companies_synced(
                        count=len(failure_list), status="failed"
                    )

            duration = time.perf_counter() - start_time
            self._telemetry.observe_sync_duration(
                context="companies", duration=duration
            )
            logger.info(f"Synchronization finished in {duration:.2f}s.")

        finally:
            self._telemetry.decrement_active_sync_tasks()
