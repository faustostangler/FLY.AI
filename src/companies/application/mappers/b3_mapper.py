from typing import Dict, Any, List, Optional, Tuple
import structlog
from companies.domain.entities import Company
from companies.application.dtos.b3_company_dto import B3CompanyPayloadDTO
from shared.domain.ports.telemetry_port import TelemetryPort
from shared.infrastructure.utils.date_resilient import DateResilientParser

logger = structlog.get_logger().bind(bounded_context="companies")


class B3CompanyMapper:
    """Anti-Corruption Layer (ACL) Mapper for B3 Data.
    
    Translates raw and often inconsistent JSON responses from B3 private APIs
    into clean, validated Domain Entities. This isolates the Application logic
    from external schema changes.
    """

    @staticmethod
    def to_domain(
        basic_info: Dict[str, Any], 
        detailed_info: Dict[str, Any],
        telemetry: TelemetryPort
    ) -> Company:
        """Transforms raw B3 payloads into a Domain Entity.
        
        Args:
            basic_info: Summary data from the initial listing.
            detailed_info: Granular metadata from the detail API.
            telemetry: Telemetry port for tracking parsing anomalies.
            
        Returns:
            Company: A hydrated and validated Domain Entity.
        """
        # 1. Process Industry Classification (Sector / Subsector / Segment)
        sector, subsector, segment = B3CompanyMapper._parse_industry_classification(
            detailed_info.get("industryClassification", "")
        )

        # 2. Extract Security Identifiers (Ticker codes and ISIN codes)
        ticker_codes, isin_codes = B3CompanyMapper._extract_security_identifiers(
            detailed_info.get("otherCodes", [])
        )

        # 3. Assemble DTO (Sanitization Layer)
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
            "date_listing": DateResilientParser.parse(
                detailed_info.get("dateListing") or basic_info.get("dateListing"),
                "date_listing",
                telemetry=telemetry,
            ),
            "last_date": DateResilientParser.parse(
                detailed_info.get("lastDate"), "last_date", telemetry=telemetry
            ),
            "date_quotation": DateResilientParser.parse(
                detailed_info.get("dateQuotation"),
                "date_quotation",
                telemetry=telemetry,
            ),
            "website": detailed_info.get("website"),
            "registrar": detailed_info.get("registrar") or detailed_info.get("institutionCommon"),
            "main_registrar": (
                detailed_info.get("mainRegistrar") or 
                detailed_info.get("institutionPreferred") or 
                detailed_info.get("main_registrar")
            ),
            "status": detailed_info.get("status"),
            "company_type": detailed_info.get("type"),
            "market_indicator": detailed_info.get("marketIndicator"),
            "ticker_codes": ticker_codes,
            "isin_codes": isin_codes,
            "type_bdr": detailed_info.get("typeBDR"),
            "has_quotation": detailed_info.get("hasQuotation", detailed_info.get("has_quotation")),
            "has_emissions": detailed_info.get("hasEmissions", detailed_info.get("has_emissions")),
            "has_bdr": detailed_info.get("hasBDR", detailed_info.get("has_bdr")),
        }

        dto = B3CompanyPayloadDTO(**payload_data)
        return dto.to_domain()

    @staticmethod
    def _parse_industry_classification(industry_raw: str) -> Tuple[Optional[str], Optional[str], Optional[str]]:
        """Splits industry classification string into (sector, subsector, segment)."""
        if not industry_raw:
            return None, None, None

        parts = [p.strip() for p in industry_raw.split("/")]

        sector = parts[0] if len(parts) > 0 else None
        subsector = parts[1] if len(parts) > 1 else sector
        segment = parts[2] if len(parts) > 2 else sector

        return sector, subsector, segment

    @staticmethod
    def _extract_security_identifiers(other_codes: List[Dict[str, Any]]) -> Tuple[List[str], List[str]]:
        """Extracts ticker and ISIN codes from the otherCodes list."""
        if not other_codes:
            return [], []

        ticker_codes = [
            o["code"] for o in other_codes if isinstance(o, dict) and "code" in o
        ]
        isin_codes = [
            o["isin"] for o in other_codes if isinstance(o, dict) and "isin" in o
        ]

        return ticker_codes, isin_codes
