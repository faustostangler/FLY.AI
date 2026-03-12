from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class CompanyModel(Base):
    __tablename__ = "company_info"

    id = Column(Integer, primary_key=True, autoincrement=True)
    
    # Core
    ticker = Column(String, unique=True, nullable=False, index=True)
    cvm_code = Column(String, nullable=False, index=True)
    company_name = Column(String, nullable=False)
    trading_name = Column(String)
    cnpj = Column(String)
    
    # Market details
    listing = Column(String)
    sector = Column(String)
    subsector = Column(String)
    segment = Column(String)
    segment_eng = Column(String)
    activity = Column(String)
    describle_category_bvmf = Column(String)
    
    # Dates
    date_listing = Column(String)
    last_date = Column(String)
    date_quotation = Column(String)
    
    # Infrastructure / Legal
    website = Column(String)
    registrar = Column(String)
    main_registrar = Column(String)
    status = Column(String)
    type = Column(String)
    market_indicator = Column(String)
    
    # Securities Identifiers
    ticker_codes = Column(String)
    isin_codes = Column(String)
    type_bdr = Column(String)
    has_quotation = Column(String)
    has_emissions = Column(String)
    has_bdr = Column(String)
