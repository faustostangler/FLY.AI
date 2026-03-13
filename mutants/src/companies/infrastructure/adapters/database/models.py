from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()
from typing import Annotated
from typing import Callable
from typing import ClassVar

MutantDict = Annotated[dict[str, Callable], "Mutant"] # type: ignore


def _mutmut_trampoline(orig, mutants, call_args, call_kwargs, self_arg = None): # type: ignore
    """Forward call to original or mutated function, depending on the environment"""
    import os # type: ignore
    mutant_under_test = os.environ['MUTANT_UNDER_TEST'] # type: ignore
    if mutant_under_test == 'fail': # type: ignore
        from mutmut.__main__ import MutmutProgrammaticFailException # type: ignore
        raise MutmutProgrammaticFailException('Failed programmatically')       # type: ignore
    elif mutant_under_test == 'stats': # type: ignore
        from mutmut.__main__ import record_trampoline_hit # type: ignore
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__) # type: ignore
        # (for class methods, orig is bound and thus does not need the explicit self argument)
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_' # type: ignore
    if not mutant_under_test.startswith(prefix): # type: ignore
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    mutant_name = mutant_under_test.rpartition('.')[-1] # type: ignore
    if self_arg is not None: # type: ignore
        # call to a class method where self is not bound
        result = mutants[mutant_name](self_arg, *call_args, **call_kwargs) # type: ignore
    else:
        result = mutants[mutant_name](*call_args, **call_kwargs) # type: ignore
    return result # type: ignore

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
    date_listing = Column(DateTime)
    last_date = Column(DateTime)
    date_quotation = Column(DateTime)
    
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
    has_quotation = Column(Boolean)
    has_emissions = Column(Boolean)
    has_bdr = Column(Boolean)
