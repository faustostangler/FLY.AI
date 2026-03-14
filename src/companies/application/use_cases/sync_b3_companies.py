import asyncio
import logging
import time
from typing import Dict, Any, List, Optional, Union, cast
from pydantic import ValidationError

from companies.domain.entities.company import Company
from companies.domain.ports.b3_data_source import B3DataSource
from companies.domain.ports.company_repository import CompanyRepository
from companies.domain.exceptions import (
    CompanyValidationError, 
    CompanyDataValidationError,
    B3RateLimitExceededError,
    B3NetworkTimeoutError,
    CompanySyncError
)
from companies.application.dtos.b3_company_dto import B3CompanyPayloadDTO
from shared.infrastructure.config import settings
from shared.domain.ports.telemetry_port import TelemetryPort
from shared.infrastructure.utils.date_resilient import DateResilientParser
from shared.infrastructure.progress import ProgressReporter
from shared.domain.utils.result import Result

logger = logging.getLogger(__name__)

class SyncB3CompaniesUseCase:
    """
    Application Use Case to synchronize the list of companies from B3
    into the database using the data source and repository ports.
    """
    def __init__(self, data_source: B3DataSource, repository: CompanyRepository, telemetry: TelemetryPort):
        self._data_source = data_source
        self._repository = repository
        self._telemetry = telemetry
        
    def _map_b3_payload_to_entity(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity via DTO.
        Includes fallbacks and conversions matching the Domain rules.
        """
        # 1. Process Industry Classification (Sector / Subsector / Segment)
        sector, subsector, segment = self._parse_industry_classification(
            detailed_info.get("industryClassification", "")
        )

        # 2. Extract Security Identifiers (Ticker codes and ISIN codes)
        ticker_codes, isin_codes = self._extract_security_identifiers(
            detailed_info.get("otherCodes", [])
        )

        # 3. Merge data for DTO (Anti-Corruption Layer)
        payload_data = {
            "ticker": detailed_info.get("issuingCompany") or basic_info.get("issuingCompany"),
            "cvm_code": str(basic_info.get("codeCVM")),
            "company_name": detailed_info.get("companyName") or basic_info.get("companyName"),
            "trading_name": detailed_info.get("tradingName"),
            "cnpj": detailed_info.get("cnpj"),
            "listing": detailed_info.get("market"),
            "sector": sector,
            "subsector": subsector,
            "segment": segment,
            "segment_eng": detailed_info.get("industryClassificationEng") or detailed_info.get("segmentEng"),
            "activity": detailed_info.get("activity"),
            "describle_category_bvmf": detailed_info.get("describleCategoryBVMF"),
            "date_listing": DateResilientParser.parse(detailed_info.get("dateListing") or basic_info.get("dateListing"), "date_listing", telemetry=self._telemetry),
            "last_date": DateResilientParser.parse(detailed_info.get("lastDate"), "last_date", telemetry=self._telemetry),
            "date_quotation": DateResilientParser.parse(detailed_info.get("dateQuotation"), "date_quotation", telemetry=self._telemetry),
            "website": detailed_info.get("website"),
            "registrar": detailed_info.get("registrar") or detailed_info.get("institutionCommon"),
            "main_registrar": detailed_info.get("mainRegistrar") or detailed_info.get("institutionPreferred") or detailed_info.get("main_registrar"),
            "status": detailed_info.get("status"),
            "type": detailed_info.get("type"),
            "market_indicator": detailed_info.get("marketIndicator"),
            "ticker_codes": ticker_codes,
            "isin_codes": isin_codes,
            "type_bdr": detailed_info.get("typeBDR"),
            "has_quotation": detailed_info.get("hasQuotation", detailed_info.get("has_quotation")),
            "has_emissions": detailed_info.get("hasEmissions", detailed_info.get("has_emissions")),
            "has_bdr": detailed_info.get("hasBDR", detailed_info.get("has_bdr"))
        }

        # 4. Filter through DTO (Scrubbing/Sanitization)
        dto = B3CompanyPayloadDTO(**payload_data)
        
        # 5. Convert to Domain Entity
        return dto.to_domain()

    def _parse_industry_classification(self, industry_raw: str) -> tuple:
        """Splits industry classification string into (sector, subsector, segment)."""
        if not industry_raw:
            return None, None, None
            
        parts = [p.strip() for p in industry_raw.split("/")]
        
        sector = parts[0] if len(parts) > 0 else None
        subsector = parts[1] if len(parts) > 1 else sector
        segment = parts[2] if len(parts) > 2 else sector
        
        return sector, subsector, segment

    def _extract_security_identifiers(self, other_codes: List[Dict[str, Any]]) -> tuple:
        """Extracts ticker and ISIN codes from the otherCodes list."""
        if not other_codes:
            return [], []
            
        ticker_codes = [o["code"] for o in other_codes if isinstance(o, dict) and "code" in o]
        isin_codes = [o["isin"] for o in other_codes if isinstance(o, dict) and "isin" in o]
        
        return ticker_codes, isin_codes

    async def _process_single_company(self, index: int, raw_company: Dict[str, Any], semaphore: asyncio.Semaphore, reporter: ProgressReporter) -> Result[Company, Exception]:
        """Helper to process a single company using Result Monad."""
        ticker = raw_company.get("issuingCompany")
        cvm_code = str(raw_company.get("codeCVM"))
        
        if not ticker or not cvm_code.isdigit():
            return Result.fail(CompanyDataValidationError("Missing Ticker or invalid CVM", "cvm_code", ticker))
            
        async with semaphore:
            try:
                # 1. Infrastructure: Detail fetch
                details = await self._data_source.fetch_company_details(cvm_code)

                # 2. Application: Mapping & Validation (DTO -> Entity)
                entity = self._map_b3_payload_to_entity(raw_company, details)
                
                logger.debug(reporter.get_formatted_progress(index, [ticker]))
                return Result.ok(entity)
            except ValidationError as e:
                return Result.fail(CompanyDataValidationError(f"DTO Validation failed: {e}", "multiple", ticker))
            except CompanyValidationError as e:
                return Result.fail(e)
            except B3RateLimitExceededError as e:
                return Result.fail(e)
            except (asyncio.TimeoutError, TimeoutError):
                return Result.fail(B3NetworkTimeoutError(f"Timeout fetching details for {ticker} ({cvm_code})"))
            except Exception as e:
                # Catch-all for unexpected infrastructure level errors
                return Result.fail(e)

    async def execute(self) -> None:
        """
        Main execution flow with SOTA concurrency and Result Monad:
        1. Fetch all companies listed.
        2. Fetch details for each company concurrently with rate limiting.
        3. Handle failures via Monadic Result (No Pokemon Exception Handling).
        4. Report detailed SRE metrics based on error taxonomy.
        5. Save successes to Repository.
        """
        logger.info("Starting B3 Companies Synchronization (SOTA Result Monad Mode)")
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
                            entity="Company", field=val_error.field, reason="b3_payload_mismatch"
                        )
                    elif isinstance(error, CompanyValidationError):
                        self._telemetry.increment_data_validation_error(
                            entity="Company", field="domain_logic", reason="business_rule_violation"
                        )
                    elif isinstance(error, B3RateLimitExceededError):
                        self._telemetry.increment_b3_rate_limit_hits()
                    elif isinstance(error, B3NetworkTimeoutError):
                        self._telemetry.increment_generic_sync_error(type="NetworkTimeout")
                    else:
                        self._telemetry.increment_generic_sync_error(type=error.__class__.__name__)
                
                # 3. Persistence & Outcome Telemetry
                if success_list:
                    # Deduplicate by ticker
                    unique_entities = list({e.ticker: e for e in success_list}.values())
                    logger.info(f"Persistence: Saving {len(unique_entities)} unique companies.")
                    self._repository.save_batch(unique_entities)
                    self._telemetry.increment_companies_synced(count=len(unique_entities), status="success")
                
                if failure_list:
                    logger.warning(f"SRE Alert: {len(failure_list)} companies failed synchronization.")
                    self._telemetry.increment_companies_synced(count=len(failure_list), status="failed")

            duration = time.perf_counter() - start_time
            self._telemetry.observe_sync_duration(context="companies", duration=duration)
            logger.info(f"Synchronization finished in {duration:.2f}s.")
            
        finally:
            self._telemetry.decrement_active_sync_tasks()
