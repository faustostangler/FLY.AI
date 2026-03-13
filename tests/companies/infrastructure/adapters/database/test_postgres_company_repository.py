import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from companies.domain.entities.company import Company
from companies.infrastructure.adapters.database.models import Base, CompanyModel
from companies.infrastructure.adapters.database.postgres_company_repository import PostgresCompanyRepository

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
        company_name="Petróleo Brasileiro S.A. - Petrobras",
        trading_name="PETROBRAS",
        cnpj="33000167000101",
        sector="Energy",
        subsector="Oil, Gas and Biofuels",
        segment="Exploration and Production",
        website="https://www.petrobras.com.br",
        status="A",
        listing="BOLSA",
        type="CI",
        market_indicator="1",
        has_quotation=True,
        has_emissions=True,
        has_bdr=False,
        ticker_codes=["PETR4", "PETR3"],
        isin_codes=["BRPETRACNOR9", "BRPETRACNPR6"]
    )

def test_save_company_success(repo, db_session, sample_company):
    # Action
    repo.save(sample_company)
    
    # Assert
    saved = db_session.query(CompanyModel).filter_by(ticker="PETR4").first()
    assert saved is not None
    # Entidade limpa o nome para uppercase internamente
    assert saved.company_name == sample_company.company_name
    assert saved.sector == sample_company.sector
    assert saved.cnpj == sample_company.cnpj.root

def test_mapping_integrity_roundtrip(repo, sample_company):
    """
    Testa se todos os atributos da entidade sobrevivem à ida e volta do banco de dados.
    Isso garante que o _to_model e _to_entity mapeiem todos os campos corretamente.
    """
    # Action
    repo.save(sample_company)
    fetched = repo.get_by_ticker(sample_company.ticker)
    
    # Assert
    assert fetched is not None
    
    # Comparação exaustiva de campos
    for field in Company.model_fields:
        val_original = getattr(sample_company, field)
        val_fetched = getattr(fetched, field)
        
        # Especial para Value Objects (CNPJ)
        if field == "cnpj" and val_original:
            assert val_fetched.root == val_original.root
        else:
            assert val_fetched == val_original, f"Mapeamento do campo '{field}' falhou no Round-trip"

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
    
    indexed_companies = {c.ticker: c for c in all_companies}
    assert indexed_companies["VALE3"].cvm_code == "4170"
    assert indexed_companies["ITUB4"].cvm_code == "19348"
    assert indexed_companies["VALE3"].sector == "MATERIALS"
