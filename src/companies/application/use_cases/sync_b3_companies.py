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
    CompanySyncError,
)
from shared.domain.errors import DomainError
from companies.application.mappers.b3_mapper import B3CompanyMapper
from shared.infrastructure.config import settings
from shared.domain.ports.telemetry_port import TelemetryPort
from shared.infrastructure.progress import ProgressReporter
from shared.domain.utils.result import Result
from shared.domain.errors import DomainError

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

    async def _worker(
        self,
        queue: asyncio.Queue,
        results: List[Result[Company, Exception]],
        reporter: ProgressReporter,
    ) -> None:
        """Worker loop to consume tasks from the queue."""
        while True:
            task = await queue.get()
            try:
                if task is None:
                    break

                index, raw_company = task
                result = await self._process_single_company(index, raw_company, reporter)
                results.append(result)
            except asyncio.CancelledError:
                break
            except Exception as e:
                logger.exception("Unexpected error in worker loop", error=str(e))
            finally:
                queue.task_done()

    async def _process_single_company(
        self,
        index: int,
        raw_company: Dict[str, Any],
        reporter: ProgressReporter,
    ) -> Result[Company, DomainError]: # Changed from Exception to DomainError
        """Helper to process a single company using Result Monad."""
        ticker = raw_company.get("issuingCompany")
        cvm_code = str(raw_company.get("codeCVM"))

        if not ticker or not cvm_code.isdigit():
            return Result.fail(
                CompanyDataValidationError(
                    "Missing Ticker or invalid CVM", "cvm_code", ticker
                )
            )

        try:
            # 1. Infrastructure: Detail fetch
            res_details = await self._data_source.fetch_company_details(cvm_code)
            if res_details.is_failure:
                # Map infrastructure-specific errors to Domain Errors
                if isinstance(res_details.error, (asyncio.TimeoutError, TimeoutError)):
                    return Result.fail(
                        B3NetworkTimeoutError(
                            f"Timeout fetching details for {ticker} ({cvm_code})"
                        )
                    )
                return Result.fail(res_details.error)
            
            details = res_details.value

            # 2. Application/Domain: Mapping & Validation (ACL Mapper -> Entity)
            # The Mapper now handles business validation and returns Result.
            return B3CompanyMapper.to_domain(
                raw_company, details, self._telemetry
            )

        except (asyncio.TimeoutError, TimeoutError):
            return Result.fail(
                B3NetworkTimeoutError(
                    f"Timeout fetching details for {ticker} ({cvm_code})"
                )
            )
        except Exception as e:
            # Catch-all for unexpected infrastructure level errors
            return Result.fail(
                CompanySyncError(
                    message=f"Unexpected error fetching details for {ticker} ({cvm_code}): {str(e)}",
                    code="INFRASTRUCTURE_ERROR"
                )
            )

    async def execute(self) -> None:
        """Executes the complete synchronization workflow.

        Nested Logical Steps:
            1. Saturation tracking: Increment active task gauge.
            2. Data Discovery: Fetch the initial issuer list.
            3. Worker Pool Orchestration: Execute detail probes via asyncio.Queue.
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
                initial_res = await self._data_source.fetch_initial_companies()
                if initial_res.is_failure:
                    logger.error("Failed to fetch initial companies", error=str(initial_res.error))
                    return

                initial_companies = initial_res.value
                total_companies = len(initial_companies)
                
                if not initial_companies:
                    logger.info("No companies found to synchronize.")
                    return

                # 2. ORCHESTRATION: Worker Pool with asyncio.Queue
                # maxsize provides backpressure to the producer
                queue: asyncio.Queue = asyncio.Queue(maxsize=settings.app.max_concurrency * 2)
                results: List[Result[Company, Exception]] = []
                reporter = ProgressReporter(total=total_companies)

                # Initialize fixed-size worker pool
                num_workers = min(settings.app.max_concurrency, total_companies)
                workers = [
                    asyncio.create_task(self._worker(queue, results, reporter))
                    for _ in range(num_workers)
                ]

                # Producer: Feed the queue
                for i, raw in enumerate(initial_companies):
                    await queue.put((i, raw))

                # Wait for all tasks to be processed
                await queue.join()

                # Stop workers gracefully
                for _ in range(num_workers):
                    await queue.put(None)
                await asyncio.gather(*workers)

                # Unpack Monad
                success_list: List[Company] = []
                failure_list: List[DomainError] = []

                for r in results:
                    if r.is_success and r.value:
                        success_list.append(r.value)
                    elif r.is_failure and r.error:
                        # We know these are now DomainError or Exception
                        failure_list.append(r.error)

                # 3. SRE: Telemetry for Errors (Taxonomy-driven)
                for error in failure_list:
                    if isinstance(error, CompanyDataValidationError):
                        self._telemetry.increment_data_validation_error(
                            entity="Company",
                            field=error.details.get("field", "unknown") if error.details else "unknown",
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

                # 4. Persistence & Outcome Telemetry
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
