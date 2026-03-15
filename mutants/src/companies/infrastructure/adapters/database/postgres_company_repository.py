from typing import List, Optional
from sqlalchemy.orm import Session
from sqlalchemy.dialects.postgresql import insert

from companies.domain.entities.company import Company
from companies.domain.ports.company_repository import CompanyRepository
from companies.infrastructure.adapters.database.models import CompanyModel
from companies.infrastructure.adapters.database.mapper import CompanyDataMapper
from typing import Annotated
from typing import Callable
from typing import ClassVar

MutantDict = Annotated[dict[str, Callable], "Mutant"]  # type: ignore


def _mutmut_trampoline(orig, mutants, call_args, call_kwargs, self_arg=None):  # type: ignore
    """Forward call to original or mutated function, depending on the environment"""
    import os  # type: ignore

    mutant_under_test = os.environ["MUTANT_UNDER_TEST"]  # type: ignore
    if mutant_under_test == "fail":  # type: ignore
        from mutmut.__main__ import MutmutProgrammaticFailException  # type: ignore

        raise MutmutProgrammaticFailException("Failed programmatically")  # type: ignore
    elif mutant_under_test == "stats":  # type: ignore
        from mutmut.__main__ import record_trampoline_hit  # type: ignore

        record_trampoline_hit(orig.__module__ + "." + orig.__name__)  # type: ignore
        # (for class methods, orig is bound and thus does not need the explicit self argument)
        result = orig(*call_args, **call_kwargs)  # type: ignore
        return result  # type: ignore
    prefix = orig.__module__ + "." + orig.__name__ + "__mutmut_"  # type: ignore
    if not mutant_under_test.startswith(prefix):  # type: ignore
        result = orig(*call_args, **call_kwargs)  # type: ignore
        return result  # type: ignore
    mutant_name = mutant_under_test.rpartition(".")[-1]  # type: ignore
    if self_arg is not None:  # type: ignore
        # call to a class method where self is not bound
        result = mutants[mutant_name](self_arg, *call_args, **call_kwargs)  # type: ignore
    else:
        result = mutants[mutant_name](*call_args, **call_kwargs)  # type: ignore
    return result  # type: ignore


class PostgresCompanyRepository(CompanyRepository):
    """PostgreSQL implementation of the CompanyRepository port.

    This adapter provides high-performance persistence using native
    PostgreSQL features (UPSERT) while keeping the Domain decoupled from
    relational schemas through the use of Data Mappers.

    Attributes:
        session (Session): An active SQLAlchemy session for transaction management.
    """

    def __init__(self, session: Session):
        args = [session]  # type: ignore
        kwargs = {}  # type: ignore
        return _mutmut_trampoline(
            object.__getattribute__(
                self, "xǁPostgresCompanyRepositoryǁ__init____mutmut_orig"
            ),
            object.__getattribute__(
                self, "xǁPostgresCompanyRepositoryǁ__init____mutmut_mutants"
            ),
            args,
            kwargs,
            self,
        )

    def xǁPostgresCompanyRepositoryǁ__init____mutmut_orig(self, session: Session):
        self._session = session

    def xǁPostgresCompanyRepositoryǁ__init____mutmut_1(self, session: Session):
        self._session = None

    xǁPostgresCompanyRepositoryǁ__init____mutmut_mutants: ClassVar[MutantDict] = {  # type: ignore
        "xǁPostgresCompanyRepositoryǁ__init____mutmut_1": xǁPostgresCompanyRepositoryǁ__init____mutmut_1
    }
    xǁPostgresCompanyRepositoryǁ__init____mutmut_orig.__name__ = (
        "xǁPostgresCompanyRepositoryǁ__init__"
    )

    def save(self, company: Company) -> None:
        args = [company]  # type: ignore
        kwargs = {}  # type: ignore
        return _mutmut_trampoline(
            object.__getattribute__(
                self, "xǁPostgresCompanyRepositoryǁsave__mutmut_orig"
            ),
            object.__getattribute__(
                self, "xǁPostgresCompanyRepositoryǁsave__mutmut_mutants"
            ),
            args,
            kwargs,
            self,
        )

    def xǁPostgresCompanyRepositoryǁsave__mutmut_orig(self, company: Company) -> None:
        """Persists or updates an issuer using an atomic UPSERT operation.

        Relying on native 'ON CONFLICT' clauses ensures atomicity and
        prevents race conditions during concurrent updates of the same ticker.

        Args:
            company (Company): The domain entity to be persisted.
        """
        data = CompanyDataMapper.to_persistence_dict(company)

        stmt = insert(CompanyModel).values(data)
        stmt = stmt.on_conflict_do_update(
            index_elements=["ticker"],
            set_={k: v for k, v in data.items() if k != "ticker"},
        )

        self._session.execute(stmt)
        self._session.commit()

    def xǁPostgresCompanyRepositoryǁsave__mutmut_1(self, company: Company) -> None:
        """Persists or updates an issuer using an atomic UPSERT operation.

        Relying on native 'ON CONFLICT' clauses ensures atomicity and
        prevents race conditions during concurrent updates of the same ticker.

        Args:
            company (Company): The domain entity to be persisted.
        """
        data = None

        stmt = insert(CompanyModel).values(data)
        stmt = stmt.on_conflict_do_update(
            index_elements=["ticker"],
            set_={k: v for k, v in data.items() if k != "ticker"},
        )

        self._session.execute(stmt)
        self._session.commit()

    def xǁPostgresCompanyRepositoryǁsave__mutmut_2(self, company: Company) -> None:
        """Persists or updates an issuer using an atomic UPSERT operation.

        Relying on native 'ON CONFLICT' clauses ensures atomicity and
        prevents race conditions during concurrent updates of the same ticker.

        Args:
            company (Company): The domain entity to be persisted.
        """
        data = CompanyDataMapper.to_persistence_dict(None)

        stmt = insert(CompanyModel).values(data)
        stmt = stmt.on_conflict_do_update(
            index_elements=["ticker"],
            set_={k: v for k, v in data.items() if k != "ticker"},
        )

        self._session.execute(stmt)
        self._session.commit()

    def xǁPostgresCompanyRepositoryǁsave__mutmut_3(self, company: Company) -> None:
        """Persists or updates an issuer using an atomic UPSERT operation.

        Relying on native 'ON CONFLICT' clauses ensures atomicity and
        prevents race conditions during concurrent updates of the same ticker.

        Args:
            company (Company): The domain entity to be persisted.
        """
        data = CompanyDataMapper.to_persistence_dict(company)

        stmt = None
        stmt = stmt.on_conflict_do_update(
            index_elements=["ticker"],
            set_={k: v for k, v in data.items() if k != "ticker"},
        )

        self._session.execute(stmt)
        self._session.commit()

    def xǁPostgresCompanyRepositoryǁsave__mutmut_4(self, company: Company) -> None:
        """Persists or updates an issuer using an atomic UPSERT operation.

        Relying on native 'ON CONFLICT' clauses ensures atomicity and
        prevents race conditions during concurrent updates of the same ticker.

        Args:
            company (Company): The domain entity to be persisted.
        """
        data = CompanyDataMapper.to_persistence_dict(company)

        stmt = insert(CompanyModel).values(None)
        stmt = stmt.on_conflict_do_update(
            index_elements=["ticker"],
            set_={k: v for k, v in data.items() if k != "ticker"},
        )

        self._session.execute(stmt)
        self._session.commit()

    def xǁPostgresCompanyRepositoryǁsave__mutmut_5(self, company: Company) -> None:
        """Persists or updates an issuer using an atomic UPSERT operation.

        Relying on native 'ON CONFLICT' clauses ensures atomicity and
        prevents race conditions during concurrent updates of the same ticker.

        Args:
            company (Company): The domain entity to be persisted.
        """
        data = CompanyDataMapper.to_persistence_dict(company)

        stmt = insert(None).values(data)
        stmt = stmt.on_conflict_do_update(
            index_elements=["ticker"],
            set_={k: v for k, v in data.items() if k != "ticker"},
        )

        self._session.execute(stmt)
        self._session.commit()

    def xǁPostgresCompanyRepositoryǁsave__mutmut_6(self, company: Company) -> None:
        """Persists or updates an issuer using an atomic UPSERT operation.

        Relying on native 'ON CONFLICT' clauses ensures atomicity and
        prevents race conditions during concurrent updates of the same ticker.

        Args:
            company (Company): The domain entity to be persisted.
        """
        data = CompanyDataMapper.to_persistence_dict(company)

        stmt = insert(CompanyModel).values(data)
        stmt = None

        self._session.execute(stmt)
        self._session.commit()

    def xǁPostgresCompanyRepositoryǁsave__mutmut_7(self, company: Company) -> None:
        """Persists or updates an issuer using an atomic UPSERT operation.

        Relying on native 'ON CONFLICT' clauses ensures atomicity and
        prevents race conditions during concurrent updates of the same ticker.

        Args:
            company (Company): The domain entity to be persisted.
        """
        data = CompanyDataMapper.to_persistence_dict(company)

        stmt = insert(CompanyModel).values(data)
        stmt = stmt.on_conflict_do_update(
            index_elements=None, set_={k: v for k, v in data.items() if k != "ticker"}
        )

        self._session.execute(stmt)
        self._session.commit()

    def xǁPostgresCompanyRepositoryǁsave__mutmut_8(self, company: Company) -> None:
        """Persists or updates an issuer using an atomic UPSERT operation.

        Relying on native 'ON CONFLICT' clauses ensures atomicity and
        prevents race conditions during concurrent updates of the same ticker.

        Args:
            company (Company): The domain entity to be persisted.
        """
        data = CompanyDataMapper.to_persistence_dict(company)

        stmt = insert(CompanyModel).values(data)
        stmt = stmt.on_conflict_do_update(index_elements=["ticker"], set_=None)

        self._session.execute(stmt)
        self._session.commit()

    def xǁPostgresCompanyRepositoryǁsave__mutmut_9(self, company: Company) -> None:
        """Persists or updates an issuer using an atomic UPSERT operation.

        Relying on native 'ON CONFLICT' clauses ensures atomicity and
        prevents race conditions during concurrent updates of the same ticker.

        Args:
            company (Company): The domain entity to be persisted.
        """
        data = CompanyDataMapper.to_persistence_dict(company)

        stmt = insert(CompanyModel).values(data)
        stmt = stmt.on_conflict_do_update(
            set_={k: v for k, v in data.items() if k != "ticker"}
        )

        self._session.execute(stmt)
        self._session.commit()

    def xǁPostgresCompanyRepositoryǁsave__mutmut_10(self, company: Company) -> None:
        """Persists or updates an issuer using an atomic UPSERT operation.

        Relying on native 'ON CONFLICT' clauses ensures atomicity and
        prevents race conditions during concurrent updates of the same ticker.

        Args:
            company (Company): The domain entity to be persisted.
        """
        data = CompanyDataMapper.to_persistence_dict(company)

        stmt = insert(CompanyModel).values(data)
        stmt = stmt.on_conflict_do_update(
            index_elements=["ticker"],
        )

        self._session.execute(stmt)
        self._session.commit()

    def xǁPostgresCompanyRepositoryǁsave__mutmut_11(self, company: Company) -> None:
        """Persists or updates an issuer using an atomic UPSERT operation.

        Relying on native 'ON CONFLICT' clauses ensures atomicity and
        prevents race conditions during concurrent updates of the same ticker.

        Args:
            company (Company): The domain entity to be persisted.
        """
        data = CompanyDataMapper.to_persistence_dict(company)

        stmt = insert(CompanyModel).values(data)
        stmt = stmt.on_conflict_do_update(
            index_elements=["XXtickerXX"],
            set_={k: v for k, v in data.items() if k != "ticker"},
        )

        self._session.execute(stmt)
        self._session.commit()

    def xǁPostgresCompanyRepositoryǁsave__mutmut_12(self, company: Company) -> None:
        """Persists or updates an issuer using an atomic UPSERT operation.

        Relying on native 'ON CONFLICT' clauses ensures atomicity and
        prevents race conditions during concurrent updates of the same ticker.

        Args:
            company (Company): The domain entity to be persisted.
        """
        data = CompanyDataMapper.to_persistence_dict(company)

        stmt = insert(CompanyModel).values(data)
        stmt = stmt.on_conflict_do_update(
            index_elements=["TICKER"],
            set_={k: v for k, v in data.items() if k != "ticker"},
        )

        self._session.execute(stmt)
        self._session.commit()

    def xǁPostgresCompanyRepositoryǁsave__mutmut_13(self, company: Company) -> None:
        """Persists or updates an issuer using an atomic UPSERT operation.

        Relying on native 'ON CONFLICT' clauses ensures atomicity and
        prevents race conditions during concurrent updates of the same ticker.

        Args:
            company (Company): The domain entity to be persisted.
        """
        data = CompanyDataMapper.to_persistence_dict(company)

        stmt = insert(CompanyModel).values(data)
        stmt = stmt.on_conflict_do_update(
            index_elements=["ticker"],
            set_={k: v for k, v in data.items() if k == "ticker"},
        )

        self._session.execute(stmt)
        self._session.commit()

    def xǁPostgresCompanyRepositoryǁsave__mutmut_14(self, company: Company) -> None:
        """Persists or updates an issuer using an atomic UPSERT operation.

        Relying on native 'ON CONFLICT' clauses ensures atomicity and
        prevents race conditions during concurrent updates of the same ticker.

        Args:
            company (Company): The domain entity to be persisted.
        """
        data = CompanyDataMapper.to_persistence_dict(company)

        stmt = insert(CompanyModel).values(data)
        stmt = stmt.on_conflict_do_update(
            index_elements=["ticker"],
            set_={k: v for k, v in data.items() if k != "XXtickerXX"},
        )

        self._session.execute(stmt)
        self._session.commit()

    def xǁPostgresCompanyRepositoryǁsave__mutmut_15(self, company: Company) -> None:
        """Persists or updates an issuer using an atomic UPSERT operation.

        Relying on native 'ON CONFLICT' clauses ensures atomicity and
        prevents race conditions during concurrent updates of the same ticker.

        Args:
            company (Company): The domain entity to be persisted.
        """
        data = CompanyDataMapper.to_persistence_dict(company)

        stmt = insert(CompanyModel).values(data)
        stmt = stmt.on_conflict_do_update(
            index_elements=["ticker"],
            set_={k: v for k, v in data.items() if k != "TICKER"},
        )

        self._session.execute(stmt)
        self._session.commit()

    def xǁPostgresCompanyRepositoryǁsave__mutmut_16(self, company: Company) -> None:
        """Persists or updates an issuer using an atomic UPSERT operation.

        Relying on native 'ON CONFLICT' clauses ensures atomicity and
        prevents race conditions during concurrent updates of the same ticker.

        Args:
            company (Company): The domain entity to be persisted.
        """
        data = CompanyDataMapper.to_persistence_dict(company)

        stmt = insert(CompanyModel).values(data)
        stmt = stmt.on_conflict_do_update(
            index_elements=["ticker"],
            set_={k: v for k, v in data.items() if k != "ticker"},
        )

        self._session.execute(None)
        self._session.commit()

    xǁPostgresCompanyRepositoryǁsave__mutmut_mutants: ClassVar[MutantDict] = {  # type: ignore
        "xǁPostgresCompanyRepositoryǁsave__mutmut_1": xǁPostgresCompanyRepositoryǁsave__mutmut_1,
        "xǁPostgresCompanyRepositoryǁsave__mutmut_2": xǁPostgresCompanyRepositoryǁsave__mutmut_2,
        "xǁPostgresCompanyRepositoryǁsave__mutmut_3": xǁPostgresCompanyRepositoryǁsave__mutmut_3,
        "xǁPostgresCompanyRepositoryǁsave__mutmut_4": xǁPostgresCompanyRepositoryǁsave__mutmut_4,
        "xǁPostgresCompanyRepositoryǁsave__mutmut_5": xǁPostgresCompanyRepositoryǁsave__mutmut_5,
        "xǁPostgresCompanyRepositoryǁsave__mutmut_6": xǁPostgresCompanyRepositoryǁsave__mutmut_6,
        "xǁPostgresCompanyRepositoryǁsave__mutmut_7": xǁPostgresCompanyRepositoryǁsave__mutmut_7,
        "xǁPostgresCompanyRepositoryǁsave__mutmut_8": xǁPostgresCompanyRepositoryǁsave__mutmut_8,
        "xǁPostgresCompanyRepositoryǁsave__mutmut_9": xǁPostgresCompanyRepositoryǁsave__mutmut_9,
        "xǁPostgresCompanyRepositoryǁsave__mutmut_10": xǁPostgresCompanyRepositoryǁsave__mutmut_10,
        "xǁPostgresCompanyRepositoryǁsave__mutmut_11": xǁPostgresCompanyRepositoryǁsave__mutmut_11,
        "xǁPostgresCompanyRepositoryǁsave__mutmut_12": xǁPostgresCompanyRepositoryǁsave__mutmut_12,
        "xǁPostgresCompanyRepositoryǁsave__mutmut_13": xǁPostgresCompanyRepositoryǁsave__mutmut_13,
        "xǁPostgresCompanyRepositoryǁsave__mutmut_14": xǁPostgresCompanyRepositoryǁsave__mutmut_14,
        "xǁPostgresCompanyRepositoryǁsave__mutmut_15": xǁPostgresCompanyRepositoryǁsave__mutmut_15,
        "xǁPostgresCompanyRepositoryǁsave__mutmut_16": xǁPostgresCompanyRepositoryǁsave__mutmut_16,
    }
    xǁPostgresCompanyRepositoryǁsave__mutmut_orig.__name__ = (
        "xǁPostgresCompanyRepositoryǁsave"
    )

    def save_batch(self, companies: List[Company]) -> None:
        args = [companies]  # type: ignore
        kwargs = {}  # type: ignore
        return _mutmut_trampoline(
            object.__getattribute__(
                self, "xǁPostgresCompanyRepositoryǁsave_batch__mutmut_orig"
            ),
            object.__getattribute__(
                self, "xǁPostgresCompanyRepositoryǁsave_batch__mutmut_mutants"
            ),
            args,
            kwargs,
            self,
        )

    def xǁPostgresCompanyRepositoryǁsave_batch__mutmut_orig(
        self, companies: List[Company]
    ) -> None:
        """Executes a bulk UPSERT for a collection of issuers.

        During full-market synchronizations, individual inserts are
        prohibitively slow. Native batch UPSERTs reduce I/O wait times
        by orders of magnitude.

        Args:
            companies (List[Company]): A sequence of domain entities.
        """
        if not companies:
            return

        # Transform domain entities into flat dictionaries compatible with the ORM.
        data_list = [
            CompanyDataMapper.to_persistence_dict(company) for company in companies
        ]

        # Standard PostgreSQL UPSERT logic (ON CONFLICT DO UPDATE).
        stmt = insert(CompanyModel).values(data_list)

        # Calculate update columns dynamically from the model definition.
        # This automatically handles schema changes without requiring
        # manual updates to the repository logic.
        update_cols = {
            c.name: stmt.excluded[c.name]
            for c in CompanyModel.__table__.columns
            if c.name not in ["id", "ticker"]
        }

        stmt = stmt.on_conflict_do_update(index_elements=["ticker"], set_=update_cols)

        self._session.execute(stmt)
        self._session.commit()

    def xǁPostgresCompanyRepositoryǁsave_batch__mutmut_1(
        self, companies: List[Company]
    ) -> None:
        """Executes a bulk UPSERT for a collection of issuers.

        During full-market synchronizations, individual inserts are
        prohibitively slow. Native batch UPSERTs reduce I/O wait times
        by orders of magnitude.

        Args:
            companies (List[Company]): A sequence of domain entities.
        """
        if companies:
            return

        # Transform domain entities into flat dictionaries compatible with the ORM.
        data_list = [
            CompanyDataMapper.to_persistence_dict(company) for company in companies
        ]

        # Standard PostgreSQL UPSERT logic (ON CONFLICT DO UPDATE).
        stmt = insert(CompanyModel).values(data_list)

        # Calculate update columns dynamically from the model definition.
        # This automatically handles schema changes without requiring
        # manual updates to the repository logic.
        update_cols = {
            c.name: stmt.excluded[c.name]
            for c in CompanyModel.__table__.columns
            if c.name not in ["id", "ticker"]
        }

        stmt = stmt.on_conflict_do_update(index_elements=["ticker"], set_=update_cols)

        self._session.execute(stmt)
        self._session.commit()

    def xǁPostgresCompanyRepositoryǁsave_batch__mutmut_2(
        self, companies: List[Company]
    ) -> None:
        """Executes a bulk UPSERT for a collection of issuers.

        During full-market synchronizations, individual inserts are
        prohibitively slow. Native batch UPSERTs reduce I/O wait times
        by orders of magnitude.

        Args:
            companies (List[Company]): A sequence of domain entities.
        """
        if not companies:
            return

        # Transform domain entities into flat dictionaries compatible with the ORM.
        data_list = None

        # Standard PostgreSQL UPSERT logic (ON CONFLICT DO UPDATE).
        stmt = insert(CompanyModel).values(data_list)

        # Calculate update columns dynamically from the model definition.
        # This automatically handles schema changes without requiring
        # manual updates to the repository logic.
        update_cols = {
            c.name: stmt.excluded[c.name]
            for c in CompanyModel.__table__.columns
            if c.name not in ["id", "ticker"]
        }

        stmt = stmt.on_conflict_do_update(index_elements=["ticker"], set_=update_cols)

        self._session.execute(stmt)
        self._session.commit()

    def xǁPostgresCompanyRepositoryǁsave_batch__mutmut_3(
        self, companies: List[Company]
    ) -> None:
        """Executes a bulk UPSERT for a collection of issuers.

        During full-market synchronizations, individual inserts are
        prohibitively slow. Native batch UPSERTs reduce I/O wait times
        by orders of magnitude.

        Args:
            companies (List[Company]): A sequence of domain entities.
        """
        if not companies:
            return

        # Transform domain entities into flat dictionaries compatible with the ORM.
        data_list = [
            CompanyDataMapper.to_persistence_dict(None) for company in companies
        ]

        # Standard PostgreSQL UPSERT logic (ON CONFLICT DO UPDATE).
        stmt = insert(CompanyModel).values(data_list)

        # Calculate update columns dynamically from the model definition.
        # This automatically handles schema changes without requiring
        # manual updates to the repository logic.
        update_cols = {
            c.name: stmt.excluded[c.name]
            for c in CompanyModel.__table__.columns
            if c.name not in ["id", "ticker"]
        }

        stmt = stmt.on_conflict_do_update(index_elements=["ticker"], set_=update_cols)

        self._session.execute(stmt)
        self._session.commit()

    def xǁPostgresCompanyRepositoryǁsave_batch__mutmut_4(
        self, companies: List[Company]
    ) -> None:
        """Executes a bulk UPSERT for a collection of issuers.

        During full-market synchronizations, individual inserts are
        prohibitively slow. Native batch UPSERTs reduce I/O wait times
        by orders of magnitude.

        Args:
            companies (List[Company]): A sequence of domain entities.
        """
        if not companies:
            return

        # Transform domain entities into flat dictionaries compatible with the ORM.
        data_list = [
            CompanyDataMapper.to_persistence_dict(company) for company in companies
        ]

        # Standard PostgreSQL UPSERT logic (ON CONFLICT DO UPDATE).
        stmt = None

        # Calculate update columns dynamically from the model definition.
        # This automatically handles schema changes without requiring
        # manual updates to the repository logic.
        update_cols = {
            c.name: stmt.excluded[c.name]
            for c in CompanyModel.__table__.columns
            if c.name not in ["id", "ticker"]
        }

        stmt = stmt.on_conflict_do_update(index_elements=["ticker"], set_=update_cols)

        self._session.execute(stmt)
        self._session.commit()

    def xǁPostgresCompanyRepositoryǁsave_batch__mutmut_5(
        self, companies: List[Company]
    ) -> None:
        """Executes a bulk UPSERT for a collection of issuers.

        During full-market synchronizations, individual inserts are
        prohibitively slow. Native batch UPSERTs reduce I/O wait times
        by orders of magnitude.

        Args:
            companies (List[Company]): A sequence of domain entities.
        """
        if not companies:
            return

        # Transform domain entities into flat dictionaries compatible with the ORM.
        data_list = [
            CompanyDataMapper.to_persistence_dict(company) for company in companies
        ]

        # Standard PostgreSQL UPSERT logic (ON CONFLICT DO UPDATE).
        stmt = insert(CompanyModel).values(None)

        # Calculate update columns dynamically from the model definition.
        # This automatically handles schema changes without requiring
        # manual updates to the repository logic.
        update_cols = {
            c.name: stmt.excluded[c.name]
            for c in CompanyModel.__table__.columns
            if c.name not in ["id", "ticker"]
        }

        stmt = stmt.on_conflict_do_update(index_elements=["ticker"], set_=update_cols)

        self._session.execute(stmt)
        self._session.commit()

    def xǁPostgresCompanyRepositoryǁsave_batch__mutmut_6(
        self, companies: List[Company]
    ) -> None:
        """Executes a bulk UPSERT for a collection of issuers.

        During full-market synchronizations, individual inserts are
        prohibitively slow. Native batch UPSERTs reduce I/O wait times
        by orders of magnitude.

        Args:
            companies (List[Company]): A sequence of domain entities.
        """
        if not companies:
            return

        # Transform domain entities into flat dictionaries compatible with the ORM.
        data_list = [
            CompanyDataMapper.to_persistence_dict(company) for company in companies
        ]

        # Standard PostgreSQL UPSERT logic (ON CONFLICT DO UPDATE).
        stmt = insert(None).values(data_list)

        # Calculate update columns dynamically from the model definition.
        # This automatically handles schema changes without requiring
        # manual updates to the repository logic.
        update_cols = {
            c.name: stmt.excluded[c.name]
            for c in CompanyModel.__table__.columns
            if c.name not in ["id", "ticker"]
        }

        stmt = stmt.on_conflict_do_update(index_elements=["ticker"], set_=update_cols)

        self._session.execute(stmt)
        self._session.commit()

    def xǁPostgresCompanyRepositoryǁsave_batch__mutmut_7(
        self, companies: List[Company]
    ) -> None:
        """Executes a bulk UPSERT for a collection of issuers.

        During full-market synchronizations, individual inserts are
        prohibitively slow. Native batch UPSERTs reduce I/O wait times
        by orders of magnitude.

        Args:
            companies (List[Company]): A sequence of domain entities.
        """
        if not companies:
            return

        # Transform domain entities into flat dictionaries compatible with the ORM.
        data_list = [
            CompanyDataMapper.to_persistence_dict(company) for company in companies
        ]

        # Standard PostgreSQL UPSERT logic (ON CONFLICT DO UPDATE).
        stmt = insert(CompanyModel).values(data_list)

        # Calculate update columns dynamically from the model definition.
        # This automatically handles schema changes without requiring
        # manual updates to the repository logic.
        update_cols = None

        stmt = stmt.on_conflict_do_update(index_elements=["ticker"], set_=update_cols)

        self._session.execute(stmt)
        self._session.commit()

    def xǁPostgresCompanyRepositoryǁsave_batch__mutmut_8(
        self, companies: List[Company]
    ) -> None:
        """Executes a bulk UPSERT for a collection of issuers.

        During full-market synchronizations, individual inserts are
        prohibitively slow. Native batch UPSERTs reduce I/O wait times
        by orders of magnitude.

        Args:
            companies (List[Company]): A sequence of domain entities.
        """
        if not companies:
            return

        # Transform domain entities into flat dictionaries compatible with the ORM.
        data_list = [
            CompanyDataMapper.to_persistence_dict(company) for company in companies
        ]

        # Standard PostgreSQL UPSERT logic (ON CONFLICT DO UPDATE).
        stmt = insert(CompanyModel).values(data_list)

        # Calculate update columns dynamically from the model definition.
        # This automatically handles schema changes without requiring
        # manual updates to the repository logic.
        update_cols = {
            c.name: stmt.excluded[c.name]
            for c in CompanyModel.__table__.columns
            if c.name in ["id", "ticker"]
        }

        stmt = stmt.on_conflict_do_update(index_elements=["ticker"], set_=update_cols)

        self._session.execute(stmt)
        self._session.commit()

    def xǁPostgresCompanyRepositoryǁsave_batch__mutmut_9(
        self, companies: List[Company]
    ) -> None:
        """Executes a bulk UPSERT for a collection of issuers.

        During full-market synchronizations, individual inserts are
        prohibitively slow. Native batch UPSERTs reduce I/O wait times
        by orders of magnitude.

        Args:
            companies (List[Company]): A sequence of domain entities.
        """
        if not companies:
            return

        # Transform domain entities into flat dictionaries compatible with the ORM.
        data_list = [
            CompanyDataMapper.to_persistence_dict(company) for company in companies
        ]

        # Standard PostgreSQL UPSERT logic (ON CONFLICT DO UPDATE).
        stmt = insert(CompanyModel).values(data_list)

        # Calculate update columns dynamically from the model definition.
        # This automatically handles schema changes without requiring
        # manual updates to the repository logic.
        update_cols = {
            c.name: stmt.excluded[c.name]
            for c in CompanyModel.__table__.columns
            if c.name not in ["XXidXX", "ticker"]
        }

        stmt = stmt.on_conflict_do_update(index_elements=["ticker"], set_=update_cols)

        self._session.execute(stmt)
        self._session.commit()

    def xǁPostgresCompanyRepositoryǁsave_batch__mutmut_10(
        self, companies: List[Company]
    ) -> None:
        """Executes a bulk UPSERT for a collection of issuers.

        During full-market synchronizations, individual inserts are
        prohibitively slow. Native batch UPSERTs reduce I/O wait times
        by orders of magnitude.

        Args:
            companies (List[Company]): A sequence of domain entities.
        """
        if not companies:
            return

        # Transform domain entities into flat dictionaries compatible with the ORM.
        data_list = [
            CompanyDataMapper.to_persistence_dict(company) for company in companies
        ]

        # Standard PostgreSQL UPSERT logic (ON CONFLICT DO UPDATE).
        stmt = insert(CompanyModel).values(data_list)

        # Calculate update columns dynamically from the model definition.
        # This automatically handles schema changes without requiring
        # manual updates to the repository logic.
        update_cols = {
            c.name: stmt.excluded[c.name]
            for c in CompanyModel.__table__.columns
            if c.name not in ["ID", "ticker"]
        }

        stmt = stmt.on_conflict_do_update(index_elements=["ticker"], set_=update_cols)

        self._session.execute(stmt)
        self._session.commit()

    def xǁPostgresCompanyRepositoryǁsave_batch__mutmut_11(
        self, companies: List[Company]
    ) -> None:
        """Executes a bulk UPSERT for a collection of issuers.

        During full-market synchronizations, individual inserts are
        prohibitively slow. Native batch UPSERTs reduce I/O wait times
        by orders of magnitude.

        Args:
            companies (List[Company]): A sequence of domain entities.
        """
        if not companies:
            return

        # Transform domain entities into flat dictionaries compatible with the ORM.
        data_list = [
            CompanyDataMapper.to_persistence_dict(company) for company in companies
        ]

        # Standard PostgreSQL UPSERT logic (ON CONFLICT DO UPDATE).
        stmt = insert(CompanyModel).values(data_list)

        # Calculate update columns dynamically from the model definition.
        # This automatically handles schema changes without requiring
        # manual updates to the repository logic.
        update_cols = {
            c.name: stmt.excluded[c.name]
            for c in CompanyModel.__table__.columns
            if c.name not in ["id", "XXtickerXX"]
        }

        stmt = stmt.on_conflict_do_update(index_elements=["ticker"], set_=update_cols)

        self._session.execute(stmt)
        self._session.commit()

    def xǁPostgresCompanyRepositoryǁsave_batch__mutmut_12(
        self, companies: List[Company]
    ) -> None:
        """Executes a bulk UPSERT for a collection of issuers.

        During full-market synchronizations, individual inserts are
        prohibitively slow. Native batch UPSERTs reduce I/O wait times
        by orders of magnitude.

        Args:
            companies (List[Company]): A sequence of domain entities.
        """
        if not companies:
            return

        # Transform domain entities into flat dictionaries compatible with the ORM.
        data_list = [
            CompanyDataMapper.to_persistence_dict(company) for company in companies
        ]

        # Standard PostgreSQL UPSERT logic (ON CONFLICT DO UPDATE).
        stmt = insert(CompanyModel).values(data_list)

        # Calculate update columns dynamically from the model definition.
        # This automatically handles schema changes without requiring
        # manual updates to the repository logic.
        update_cols = {
            c.name: stmt.excluded[c.name]
            for c in CompanyModel.__table__.columns
            if c.name not in ["id", "TICKER"]
        }

        stmt = stmt.on_conflict_do_update(index_elements=["ticker"], set_=update_cols)

        self._session.execute(stmt)
        self._session.commit()

    def xǁPostgresCompanyRepositoryǁsave_batch__mutmut_13(
        self, companies: List[Company]
    ) -> None:
        """Executes a bulk UPSERT for a collection of issuers.

        During full-market synchronizations, individual inserts are
        prohibitively slow. Native batch UPSERTs reduce I/O wait times
        by orders of magnitude.

        Args:
            companies (List[Company]): A sequence of domain entities.
        """
        if not companies:
            return

        # Transform domain entities into flat dictionaries compatible with the ORM.
        data_list = [
            CompanyDataMapper.to_persistence_dict(company) for company in companies
        ]

        # Standard PostgreSQL UPSERT logic (ON CONFLICT DO UPDATE).
        stmt = insert(CompanyModel).values(data_list)

        # Calculate update columns dynamically from the model definition.
        # This automatically handles schema changes without requiring
        # manual updates to the repository logic.
        update_cols = {
            c.name: stmt.excluded[c.name]
            for c in CompanyModel.__table__.columns
            if c.name not in ["id", "ticker"]
        }

        stmt = None

        self._session.execute(stmt)
        self._session.commit()

    def xǁPostgresCompanyRepositoryǁsave_batch__mutmut_14(
        self, companies: List[Company]
    ) -> None:
        """Executes a bulk UPSERT for a collection of issuers.

        During full-market synchronizations, individual inserts are
        prohibitively slow. Native batch UPSERTs reduce I/O wait times
        by orders of magnitude.

        Args:
            companies (List[Company]): A sequence of domain entities.
        """
        if not companies:
            return

        # Transform domain entities into flat dictionaries compatible with the ORM.
        data_list = [
            CompanyDataMapper.to_persistence_dict(company) for company in companies
        ]

        # Standard PostgreSQL UPSERT logic (ON CONFLICT DO UPDATE).
        stmt = insert(CompanyModel).values(data_list)

        # Calculate update columns dynamically from the model definition.
        # This automatically handles schema changes without requiring
        # manual updates to the repository logic.
        update_cols = {
            c.name: stmt.excluded[c.name]
            for c in CompanyModel.__table__.columns
            if c.name not in ["id", "ticker"]
        }

        stmt = stmt.on_conflict_do_update(index_elements=None, set_=update_cols)

        self._session.execute(stmt)
        self._session.commit()

    def xǁPostgresCompanyRepositoryǁsave_batch__mutmut_15(
        self, companies: List[Company]
    ) -> None:
        """Executes a bulk UPSERT for a collection of issuers.

        During full-market synchronizations, individual inserts are
        prohibitively slow. Native batch UPSERTs reduce I/O wait times
        by orders of magnitude.

        Args:
            companies (List[Company]): A sequence of domain entities.
        """
        if not companies:
            return

        # Transform domain entities into flat dictionaries compatible with the ORM.
        data_list = [
            CompanyDataMapper.to_persistence_dict(company) for company in companies
        ]

        # Standard PostgreSQL UPSERT logic (ON CONFLICT DO UPDATE).
        stmt = insert(CompanyModel).values(data_list)

        # Calculate update columns dynamically from the model definition.
        # This automatically handles schema changes without requiring
        # manual updates to the repository logic.
        update_cols = {
            c.name: stmt.excluded[c.name]
            for c in CompanyModel.__table__.columns
            if c.name not in ["id", "ticker"]
        }

        stmt = stmt.on_conflict_do_update(index_elements=["ticker"], set_=None)

        self._session.execute(stmt)
        self._session.commit()

    def xǁPostgresCompanyRepositoryǁsave_batch__mutmut_16(
        self, companies: List[Company]
    ) -> None:
        """Executes a bulk UPSERT for a collection of issuers.

        During full-market synchronizations, individual inserts are
        prohibitively slow. Native batch UPSERTs reduce I/O wait times
        by orders of magnitude.

        Args:
            companies (List[Company]): A sequence of domain entities.
        """
        if not companies:
            return

        # Transform domain entities into flat dictionaries compatible with the ORM.
        data_list = [
            CompanyDataMapper.to_persistence_dict(company) for company in companies
        ]

        # Standard PostgreSQL UPSERT logic (ON CONFLICT DO UPDATE).
        stmt = insert(CompanyModel).values(data_list)

        # Calculate update columns dynamically from the model definition.
        # This automatically handles schema changes without requiring
        # manual updates to the repository logic.
        update_cols = {
            c.name: stmt.excluded[c.name]
            for c in CompanyModel.__table__.columns
            if c.name not in ["id", "ticker"]
        }

        stmt = stmt.on_conflict_do_update(set_=update_cols)

        self._session.execute(stmt)
        self._session.commit()

    def xǁPostgresCompanyRepositoryǁsave_batch__mutmut_17(
        self, companies: List[Company]
    ) -> None:
        """Executes a bulk UPSERT for a collection of issuers.

        During full-market synchronizations, individual inserts are
        prohibitively slow. Native batch UPSERTs reduce I/O wait times
        by orders of magnitude.

        Args:
            companies (List[Company]): A sequence of domain entities.
        """
        if not companies:
            return

        # Transform domain entities into flat dictionaries compatible with the ORM.
        data_list = [
            CompanyDataMapper.to_persistence_dict(company) for company in companies
        ]

        # Standard PostgreSQL UPSERT logic (ON CONFLICT DO UPDATE).
        stmt = insert(CompanyModel).values(data_list)

        # Calculate update columns dynamically from the model definition.
        # This automatically handles schema changes without requiring
        # manual updates to the repository logic.
        update_cols = {
            c.name: stmt.excluded[c.name]
            for c in CompanyModel.__table__.columns
            if c.name not in ["id", "ticker"]
        }

        stmt = stmt.on_conflict_do_update(
            index_elements=["ticker"],
        )

        self._session.execute(stmt)
        self._session.commit()

    def xǁPostgresCompanyRepositoryǁsave_batch__mutmut_18(
        self, companies: List[Company]
    ) -> None:
        """Executes a bulk UPSERT for a collection of issuers.

        During full-market synchronizations, individual inserts are
        prohibitively slow. Native batch UPSERTs reduce I/O wait times
        by orders of magnitude.

        Args:
            companies (List[Company]): A sequence of domain entities.
        """
        if not companies:
            return

        # Transform domain entities into flat dictionaries compatible with the ORM.
        data_list = [
            CompanyDataMapper.to_persistence_dict(company) for company in companies
        ]

        # Standard PostgreSQL UPSERT logic (ON CONFLICT DO UPDATE).
        stmt = insert(CompanyModel).values(data_list)

        # Calculate update columns dynamically from the model definition.
        # This automatically handles schema changes without requiring
        # manual updates to the repository logic.
        update_cols = {
            c.name: stmt.excluded[c.name]
            for c in CompanyModel.__table__.columns
            if c.name not in ["id", "ticker"]
        }

        stmt = stmt.on_conflict_do_update(
            index_elements=["XXtickerXX"], set_=update_cols
        )

        self._session.execute(stmt)
        self._session.commit()

    def xǁPostgresCompanyRepositoryǁsave_batch__mutmut_19(
        self, companies: List[Company]
    ) -> None:
        """Executes a bulk UPSERT for a collection of issuers.

        During full-market synchronizations, individual inserts are
        prohibitively slow. Native batch UPSERTs reduce I/O wait times
        by orders of magnitude.

        Args:
            companies (List[Company]): A sequence of domain entities.
        """
        if not companies:
            return

        # Transform domain entities into flat dictionaries compatible with the ORM.
        data_list = [
            CompanyDataMapper.to_persistence_dict(company) for company in companies
        ]

        # Standard PostgreSQL UPSERT logic (ON CONFLICT DO UPDATE).
        stmt = insert(CompanyModel).values(data_list)

        # Calculate update columns dynamically from the model definition.
        # This automatically handles schema changes without requiring
        # manual updates to the repository logic.
        update_cols = {
            c.name: stmt.excluded[c.name]
            for c in CompanyModel.__table__.columns
            if c.name not in ["id", "ticker"]
        }

        stmt = stmt.on_conflict_do_update(index_elements=["TICKER"], set_=update_cols)

        self._session.execute(stmt)
        self._session.commit()

    def xǁPostgresCompanyRepositoryǁsave_batch__mutmut_20(
        self, companies: List[Company]
    ) -> None:
        """Executes a bulk UPSERT for a collection of issuers.

        During full-market synchronizations, individual inserts are
        prohibitively slow. Native batch UPSERTs reduce I/O wait times
        by orders of magnitude.

        Args:
            companies (List[Company]): A sequence of domain entities.
        """
        if not companies:
            return

        # Transform domain entities into flat dictionaries compatible with the ORM.
        data_list = [
            CompanyDataMapper.to_persistence_dict(company) for company in companies
        ]

        # Standard PostgreSQL UPSERT logic (ON CONFLICT DO UPDATE).
        stmt = insert(CompanyModel).values(data_list)

        # Calculate update columns dynamically from the model definition.
        # This automatically handles schema changes without requiring
        # manual updates to the repository logic.
        update_cols = {
            c.name: stmt.excluded[c.name]
            for c in CompanyModel.__table__.columns
            if c.name not in ["id", "ticker"]
        }

        stmt = stmt.on_conflict_do_update(index_elements=["ticker"], set_=update_cols)

        self._session.execute(None)
        self._session.commit()

    xǁPostgresCompanyRepositoryǁsave_batch__mutmut_mutants: ClassVar[MutantDict] = {  # type: ignore
        "xǁPostgresCompanyRepositoryǁsave_batch__mutmut_1": xǁPostgresCompanyRepositoryǁsave_batch__mutmut_1,
        "xǁPostgresCompanyRepositoryǁsave_batch__mutmut_2": xǁPostgresCompanyRepositoryǁsave_batch__mutmut_2,
        "xǁPostgresCompanyRepositoryǁsave_batch__mutmut_3": xǁPostgresCompanyRepositoryǁsave_batch__mutmut_3,
        "xǁPostgresCompanyRepositoryǁsave_batch__mutmut_4": xǁPostgresCompanyRepositoryǁsave_batch__mutmut_4,
        "xǁPostgresCompanyRepositoryǁsave_batch__mutmut_5": xǁPostgresCompanyRepositoryǁsave_batch__mutmut_5,
        "xǁPostgresCompanyRepositoryǁsave_batch__mutmut_6": xǁPostgresCompanyRepositoryǁsave_batch__mutmut_6,
        "xǁPostgresCompanyRepositoryǁsave_batch__mutmut_7": xǁPostgresCompanyRepositoryǁsave_batch__mutmut_7,
        "xǁPostgresCompanyRepositoryǁsave_batch__mutmut_8": xǁPostgresCompanyRepositoryǁsave_batch__mutmut_8,
        "xǁPostgresCompanyRepositoryǁsave_batch__mutmut_9": xǁPostgresCompanyRepositoryǁsave_batch__mutmut_9,
        "xǁPostgresCompanyRepositoryǁsave_batch__mutmut_10": xǁPostgresCompanyRepositoryǁsave_batch__mutmut_10,
        "xǁPostgresCompanyRepositoryǁsave_batch__mutmut_11": xǁPostgresCompanyRepositoryǁsave_batch__mutmut_11,
        "xǁPostgresCompanyRepositoryǁsave_batch__mutmut_12": xǁPostgresCompanyRepositoryǁsave_batch__mutmut_12,
        "xǁPostgresCompanyRepositoryǁsave_batch__mutmut_13": xǁPostgresCompanyRepositoryǁsave_batch__mutmut_13,
        "xǁPostgresCompanyRepositoryǁsave_batch__mutmut_14": xǁPostgresCompanyRepositoryǁsave_batch__mutmut_14,
        "xǁPostgresCompanyRepositoryǁsave_batch__mutmut_15": xǁPostgresCompanyRepositoryǁsave_batch__mutmut_15,
        "xǁPostgresCompanyRepositoryǁsave_batch__mutmut_16": xǁPostgresCompanyRepositoryǁsave_batch__mutmut_16,
        "xǁPostgresCompanyRepositoryǁsave_batch__mutmut_17": xǁPostgresCompanyRepositoryǁsave_batch__mutmut_17,
        "xǁPostgresCompanyRepositoryǁsave_batch__mutmut_18": xǁPostgresCompanyRepositoryǁsave_batch__mutmut_18,
        "xǁPostgresCompanyRepositoryǁsave_batch__mutmut_19": xǁPostgresCompanyRepositoryǁsave_batch__mutmut_19,
        "xǁPostgresCompanyRepositoryǁsave_batch__mutmut_20": xǁPostgresCompanyRepositoryǁsave_batch__mutmut_20,
    }
    xǁPostgresCompanyRepositoryǁsave_batch__mutmut_orig.__name__ = (
        "xǁPostgresCompanyRepositoryǁsave_batch"
    )

    def get_by_ticker(self, ticker: str) -> Optional[Company]:
        args = [ticker]  # type: ignore
        kwargs = {}  # type: ignore
        return _mutmut_trampoline(
            object.__getattribute__(
                self, "xǁPostgresCompanyRepositoryǁget_by_ticker__mutmut_orig"
            ),
            object.__getattribute__(
                self, "xǁPostgresCompanyRepositoryǁget_by_ticker__mutmut_mutants"
            ),
            args,
            kwargs,
            self,
        )

    def xǁPostgresCompanyRepositoryǁget_by_ticker__mutmut_orig(
        self, ticker: str
    ) -> Optional[Company]:
        """Retrieves an issuer by its primary symbol.

        Args:
            ticker (str): The ticker symbol to search for.

        Returns:
            Optional[Company]: A reconstructed domain entity or None.
        """
        model = (
            self._session.query(CompanyModel)
            .filter(CompanyModel.ticker == ticker)
            .first()
        )
        return CompanyDataMapper.to_entity(model) if model else None

    def xǁPostgresCompanyRepositoryǁget_by_ticker__mutmut_1(
        self, ticker: str
    ) -> Optional[Company]:
        """Retrieves an issuer by its primary symbol.

        Args:
            ticker (str): The ticker symbol to search for.

        Returns:
            Optional[Company]: A reconstructed domain entity or None.
        """
        model = None
        return CompanyDataMapper.to_entity(model) if model else None

    def xǁPostgresCompanyRepositoryǁget_by_ticker__mutmut_2(
        self, ticker: str
    ) -> Optional[Company]:
        """Retrieves an issuer by its primary symbol.

        Args:
            ticker (str): The ticker symbol to search for.

        Returns:
            Optional[Company]: A reconstructed domain entity or None.
        """
        model = self._session.query(CompanyModel).filter(None).first()
        return CompanyDataMapper.to_entity(model) if model else None

    def xǁPostgresCompanyRepositoryǁget_by_ticker__mutmut_3(
        self, ticker: str
    ) -> Optional[Company]:
        """Retrieves an issuer by its primary symbol.

        Args:
            ticker (str): The ticker symbol to search for.

        Returns:
            Optional[Company]: A reconstructed domain entity or None.
        """
        model = self._session.query(None).filter(CompanyModel.ticker == ticker).first()
        return CompanyDataMapper.to_entity(model) if model else None

    def xǁPostgresCompanyRepositoryǁget_by_ticker__mutmut_4(
        self, ticker: str
    ) -> Optional[Company]:
        """Retrieves an issuer by its primary symbol.

        Args:
            ticker (str): The ticker symbol to search for.

        Returns:
            Optional[Company]: A reconstructed domain entity or None.
        """
        model = (
            self._session.query(CompanyModel)
            .filter(CompanyModel.ticker != ticker)
            .first()
        )
        return CompanyDataMapper.to_entity(model) if model else None

    def xǁPostgresCompanyRepositoryǁget_by_ticker__mutmut_5(
        self, ticker: str
    ) -> Optional[Company]:
        """Retrieves an issuer by its primary symbol.

        Args:
            ticker (str): The ticker symbol to search for.

        Returns:
            Optional[Company]: A reconstructed domain entity or None.
        """
        model = (
            self._session.query(CompanyModel)
            .filter(CompanyModel.ticker == ticker)
            .first()
        )
        return CompanyDataMapper.to_entity(None) if model else None

    xǁPostgresCompanyRepositoryǁget_by_ticker__mutmut_mutants: ClassVar[MutantDict] = {  # type: ignore
        "xǁPostgresCompanyRepositoryǁget_by_ticker__mutmut_1": xǁPostgresCompanyRepositoryǁget_by_ticker__mutmut_1,
        "xǁPostgresCompanyRepositoryǁget_by_ticker__mutmut_2": xǁPostgresCompanyRepositoryǁget_by_ticker__mutmut_2,
        "xǁPostgresCompanyRepositoryǁget_by_ticker__mutmut_3": xǁPostgresCompanyRepositoryǁget_by_ticker__mutmut_3,
        "xǁPostgresCompanyRepositoryǁget_by_ticker__mutmut_4": xǁPostgresCompanyRepositoryǁget_by_ticker__mutmut_4,
        "xǁPostgresCompanyRepositoryǁget_by_ticker__mutmut_5": xǁPostgresCompanyRepositoryǁget_by_ticker__mutmut_5,
    }
    xǁPostgresCompanyRepositoryǁget_by_ticker__mutmut_orig.__name__ = (
        "xǁPostgresCompanyRepositoryǁget_by_ticker"
    )

    def get_all(self) -> List[Company]:
        args = []  # type: ignore
        kwargs = {}  # type: ignore
        return _mutmut_trampoline(
            object.__getattribute__(
                self, "xǁPostgresCompanyRepositoryǁget_all__mutmut_orig"
            ),
            object.__getattribute__(
                self, "xǁPostgresCompanyRepositoryǁget_all__mutmut_mutants"
            ),
            args,
            kwargs,
            self,
        )

    def xǁPostgresCompanyRepositoryǁget_all__mutmut_orig(self) -> List[Company]:
        """Loads all issuer records from the database.

        Used primarily for populating caches or during full-system audits.

        Returns:
            List[Company]: A list of hydrated domain entities.
        """
        models = self._session.query(CompanyModel).all()
        return [CompanyDataMapper.to_entity(m) for m in models]

    def xǁPostgresCompanyRepositoryǁget_all__mutmut_1(self) -> List[Company]:
        """Loads all issuer records from the database.

        Used primarily for populating caches or during full-system audits.

        Returns:
            List[Company]: A list of hydrated domain entities.
        """
        models = None
        return [CompanyDataMapper.to_entity(m) for m in models]

    def xǁPostgresCompanyRepositoryǁget_all__mutmut_2(self) -> List[Company]:
        """Loads all issuer records from the database.

        Used primarily for populating caches or during full-system audits.

        Returns:
            List[Company]: A list of hydrated domain entities.
        """
        models = self._session.query(None).all()
        return [CompanyDataMapper.to_entity(m) for m in models]

    def xǁPostgresCompanyRepositoryǁget_all__mutmut_3(self) -> List[Company]:
        """Loads all issuer records from the database.

        Used primarily for populating caches or during full-system audits.

        Returns:
            List[Company]: A list of hydrated domain entities.
        """
        models = self._session.query(CompanyModel).all()
        return [CompanyDataMapper.to_entity(None) for m in models]

    xǁPostgresCompanyRepositoryǁget_all__mutmut_mutants: ClassVar[MutantDict] = {  # type: ignore
        "xǁPostgresCompanyRepositoryǁget_all__mutmut_1": xǁPostgresCompanyRepositoryǁget_all__mutmut_1,
        "xǁPostgresCompanyRepositoryǁget_all__mutmut_2": xǁPostgresCompanyRepositoryǁget_all__mutmut_2,
        "xǁPostgresCompanyRepositoryǁget_all__mutmut_3": xǁPostgresCompanyRepositoryǁget_all__mutmut_3,
    }
    xǁPostgresCompanyRepositoryǁget_all__mutmut_orig.__name__ = (
        "xǁPostgresCompanyRepositoryǁget_all"
    )
