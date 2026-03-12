import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.companies.domain.entities.company import Company
from src.companies.infrastructure.adapters.database.models import Base, CompanyModel
from src.companies.infrastructure.adapters.database.postgres_company_repository import PostgresCompanyRepository

# Setup in-memory SQLite for testing adapter logic
engine = create_engine("sqlite:///:memory:")
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(scope="function")
def db_session():
    Base.metadata.create_all(bind=engine)
    session = TestingSessionLocal()
    yield session
    session.close()
    Base.metadata.drop_all(bind=engine)

@pytest.fixture
def repo(db_session):
    return PostgresCompanyRepository(session=db_session)

@pytest.fixture
def sample_company():
    return Company(
        ticker="PETR4",
        cvm_code="9512",
        company_name="Petrobras",
        trading_name="PETROBRAS",
        cnpj="33000167000101",
        sector="Energy"
    )

def test_save_company_success(repo, db_session, sample_company):
    repo.save(sample_company)
    
    # Assert
    saved = db_session.query(CompanyModel).filter_by(ticker="PETR4").first()
    assert saved is not None
    assert saved.company_name == "Petrobras"
    assert saved.sector == "Energy"

def test_get_by_ticker_success(repo, db_session, sample_company):
    # Setup
    repo.save(sample_company)
    
    # Action
    fetched = repo.get_by_ticker("PETR4")
    
    # Assert
    assert fetched is not None
    assert fetched.cvm_code == "9512"
    assert fetched.cnpj.root == "33000167000101"

def test_get_by_ticker_not_found(repo):
    fetched = repo.get_by_ticker("UNKNOWN")
    assert fetched is None

def test_save_batch_success(repo, db_session):
    companies = [
        Company(ticker="VALE3", cvm_code="4170", company_name="Vale S.A.", sector="Materials"),
        Company(ticker="ITUB4", cvm_code="19348", company_name="Itau Unibanco", sector="Financials")
    ]
    
    # Action
    repo.save_batch(companies)
    
    # Assert
    all_companies = repo.get_all()
    assert len(all_companies) == 2
    tickers = [c.ticker for c in all_companies]
    assert "VALE3" in tickers
    assert "ITUB4" in tickers
