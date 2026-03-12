import asyncio
import logging
from typing import Dict, Any, List
from pydantic import ValidationError

from domain.entities.company import Company
from domain.ports.data_sources.b3_data_source import B3DataSource
from domain.ports.repositories.company_repository import CompanyRepository

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
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=basic_info.get("companyName"),
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("market"),
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get("segmentEng"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get("dateListing"),
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get("website"),
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get("status"),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=str(detailed_info.get("has_quotation", "")),
                has_emissions=str(detailed_info.get("has_emissions", "")),
                has_bdr=str(detailed_info.get("has_bdr", ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e

    async def execute(self) -> None:
        """
        Main execution flow:
        1. Fetch all companies listed.
        2. Fetch details for each company.
        3. Map to Domain Entities.
        4. Save to Repository in batches.
        """
        logger.info("Starting B3 Companies Synchronization")
        
        # 1. Fetch the raw initial list
        initial_companies = await self._data_source.fetch_initial_companies()
        
        entities_to_save: List[Company] = []
        
        for index, raw_company in enumerate(initial_companies):
            ticker = raw_company.get("issuingCompany")
            cvm_code = str(raw_company.get("codeCVM"))
            
            if not ticker or not cvm_code.isdigit():
                logger.warning(f"Skipping invalid entry: {ticker} (CVM: {cvm_code})")
                continue
                
            logger.info(f"Processing {index + 1}/{len(initial_companies)}: {ticker}")
            
            try:
                # 2. Detail fetch
                details = await self._data_source.fetch_company_details(cvm_code)
                
                # 3. Domain Mapping 
                # Merging dictionaries strategy isn't needed here if we pass both
                company_entity = self._map_b3_payload_to_entity(raw_company, details)
                entities_to_save.append(company_entity)
            except Exception as e:
                logger.error(f"Failed to process {ticker}: {e}")
                
        # 4. Persistence
        if entities_to_save:
            logger.info(f"Saving {len(entities_to_save)} companies to the repository.")
            self._repository.save_batch(entities_to_save)
        
        logger.info("Synchronization completed successfully.")
