from datetime import datetime
from typing import Optional
from sqlalchemy import Boolean, DateTime, Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from src.shared.infrastructure.database.mixins import AuditMixin

class Base(DeclarativeBase):
    pass

class CompanyModel(Base, AuditMixin):
    __tablename__ = "company_info"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)

    # Core
    ticker: Mapped[str] = mapped_column(String, unique=True, nullable=False, index=True)
    cvm_code: Mapped[str] = mapped_column(String, nullable=False, index=True)
    company_name: Mapped[str] = mapped_column(String, nullable=False)
    trading_name: Mapped[Optional[str]] = mapped_column(String)
    cnpj: Mapped[Optional[str]] = mapped_column(String)

    # Market details
    listing: Mapped[Optional[str]] = mapped_column(String)
    sector: Mapped[Optional[str]] = mapped_column(String)
    subsector: Mapped[Optional[str]] = mapped_column(String)
    segment: Mapped[Optional[str]] = mapped_column(String)
    segment_eng: Mapped[Optional[str]] = mapped_column(String)
    activity: Mapped[Optional[str]] = mapped_column(String)
    describle_category_bvmf: Mapped[Optional[str]] = mapped_column(String)

    # Dates
    date_listing: Mapped[Optional[datetime]] = mapped_column(DateTime)
    last_date: Mapped[Optional[datetime]] = mapped_column(DateTime)
    date_quotation: Mapped[Optional[datetime]] = mapped_column(DateTime)

    # Infrastructure / Legal
    website: Mapped[Optional[str]] = mapped_column(String)
    registrar: Mapped[Optional[str]] = mapped_column(String)
    main_registrar: Mapped[Optional[str]] = mapped_column(String)
    status: Mapped[Optional[str]] = mapped_column(String)
    company_type: Mapped[Optional[str]] = mapped_column(String)
    market_indicator: Mapped[Optional[str]] = mapped_column(String)

    # Securities Identifiers
    ticker_codes: Mapped[Optional[str]] = mapped_column(String)
    isin_codes: Mapped[Optional[str]] = mapped_column(String)
    type_bdr: Mapped[Optional[str]] = mapped_column(String)
    has_quotation: Mapped[Optional[bool]] = mapped_column(Boolean)
    has_emissions: Mapped[Optional[bool]] = mapped_column(Boolean)
    has_bdr: Mapped[Optional[bool]] = mapped_column(Boolean)
