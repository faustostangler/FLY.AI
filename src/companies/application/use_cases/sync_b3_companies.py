import asyncio
import logging
from typing import Dict, Any, List, Optional
from pydantic import ValidationError

from companies.domain.entities.company import Company
from companies.domain.ports.b3_data_source import B3DataSource
from companies.domain.ports.company_repository import CompanyRepository
from shared.infrastructure.progress import ProgressReporter
from shared.infrastructure.utils.date_resilient import DateResilientParser
from shared.infrastructure.monitoring.metrics import metrics
from shared.infrastructure.config import settings
import time

logger = logging.getLogger(__name__)

class SyncB3CompaniesUseCase:
    """
    Application Use Case to synchronize the list of companies from B3
    into the database using the data source and repository ports.
    """
    def __init__(self, data_source: B3DataSource, repository: CompanyRepository):
        self._data_source = data_source
        self._repository = repository
        
    def _map_b3_payload_to_entity(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
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
        try:
            return Company(
                ticker=detailed_info.get("issuingCompany") or basic_info.get("issuingCompany"),
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=detailed_info.get("companyName") or basic_info.get("companyName"),
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("market"),
                sector=sector,
                subsector=subsector,
                segment=segment,
                segment_eng=detailed_info.get("industryClassificationEng") or detailed_info.get("segmentEng"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("describleCategoryBVMF"),
                date_listing=DateResilientParser.parse(detailed_info.get("dateListing") or basic_info.get("dateListing"), "date_listing"),
                last_date=DateResilientParser.parse(detailed_info.get("lastDate"), "last_date"),
                date_quotation=DateResilientParser.parse(detailed_info.get("dateQuotation"), "date_quotation"),
                website=detailed_info.get("website"),
                registrar=detailed_info.get("registrar") or detailed_info.get("institutionCommon"),
                main_registrar=detailed_info.get("mainRegistrar") or detailed_info.get("institutionPreferred") or detailed_info.get("main_registrar"),
                status=detailed_info.get("status"),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("marketIndicator"),
                ticker_codes=ticker_codes,
                isin_codes=isin_codes,
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=detailed_info.get("hasQuotation", detailed_info.get("has_quotation")),
                has_emissions=detailed_info.get("hasEmissions", detailed_info.get("has_emissions")),
                has_bdr=detailed_info.get("hasBDR", detailed_info.get("has_bdr"))
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e

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

    async def execute(self) -> None:
        """
        Main execution flow with SOTA concurrency:
        1. Fetch all companies listed.
        2. Fetch details for each company concurrently with rate limiting.
        3. Map to Domain Entities.
        4. Save to Repository in high-performance batches.
        """
        logger.info("Starting B3 Companies Synchronization")
        start_time = time.perf_counter()
        
        # 1. SATURATION: Mark task as active
        metrics.ACTIVE_SYNC_TASKS.inc()
        
        try:
            async with self._data_source:
                # 1. Fetch the raw initial list
                initial_companies = await self._data_source.fetch_initial_companies()
                
                # Using concurrency from centralized configuration
                semaphore = asyncio.Semaphore(settings.app.max_concurrency)
                reporter = ProgressReporter(total=len(initial_companies))
                
                async def process_company(index: int, raw_company: Dict[str, Any]) -> Optional[Company]:
                    ticker = raw_company.get("issuingCompany")
                    cvm_code = str(raw_company.get("codeCVM"))
                    
                    if not ticker or not cvm_code.isdigit():
                        return None
                        
                    async with semaphore:
                        try:
                            # 2. Detail fetch
                            details = await self._data_source.fetch_company_details(cvm_code)

                            # 3. Domain Mapping 
                            entity = self._map_b3_payload_to_entity(raw_company, details)
                            
                            logger.info(reporter.get_formatted_progress(index, [ticker]))
                            return entity
                        except Exception:
                            # Silently continue to process others, reported by error metrics if needed
                            return None

                # Execute all tasks concurrently
                tasks = [process_company(i, raw) for i, raw in enumerate(initial_companies)]
                results = await asyncio.gather(*tasks)
                
                # Filter out None results from skips or errors
                entities_to_save = [e for e in results if e is not None]
                        
                # 4. Persistence
                if entities_to_save:
                    # Deduplicate by ticker to prevent conflicts within the same batch
                    unique_entities = list({e.ticker: e for e in entities_to_save}.values())
                    logger.info(f"Saving {len(unique_entities)} unique companies to the repository.")
                    self._repository.save_batch(unique_entities)
                    
                    # 2. BUSINESS OUTCOMES: Telemetry
                    metrics.COMPANIES_SYNCED_TOTAL.labels(status="success").inc(len(unique_entities))
                    
                    # 3. MARKET INSIGHTS: Update snapshot gauges
                    # Note: In a real system, these would be aggregated from the DB periodically
                    # but updating here provides real-time visibility post-sync.
                    sectors = {}
                    segments = {}
                    for e in unique_entities:
                        if e.sector:
                            sectors[e.sector] = sectors.get(e.sector, 0) + 1
                        if e.listing:
                            segments[e.listing] = segments.get(e.listing, 0) + 1
                    
                    for sector, count in sectors.items():
                        metrics.COMPANIES_BY_SECTOR.labels(sector=sector).set(count)
                    for segment, count in segments.items():
                        metrics.COMPANIES_BY_SEGMENT.labels(segment=segment).set(count)
            
            duration = time.perf_counter() - start_time
            metrics.SYNC_DURATION_SECONDS.labels(context="companies").observe(duration)
            logger.info(f"Synchronization completed successfully in {duration:.2f}s.")
            
        finally:
            # Always decrement saturation gauge
            metrics.ACTIVE_SYNC_TASKS.dec()
