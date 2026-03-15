import pandas as pd
import pytest
from shared.infrastructure.adapters.pandas.visitor import PandasVisitor
from shared.domain.utils.specs import Cmp, StrMatch, NullCheck, ListAny, And, Or, Not


@pytest.fixture
def visitor():
    return PandasVisitor()


@pytest.fixture
def df():
    return pd.DataFrame(
        {
            "age": [20, 25, 30, None],
            "name": ["Alice", "Bob", "Charlie", None],
            "tags": [["tech", "python"], ["finance"], ["tech"], []],
            "date": pd.to_datetime(["2020-01-01", "2021-01-01", "2022-01-01", None]),
        }
    )


def test_visit_cmp_basic(visitor, df):
    # eq
    spec = Cmp("age", "==", 25)
    mask = spec.accept(visitor, df)
    assert mask.tolist() == [False, True, False, False]

    # gt
    spec = Cmp("age", ">", 20)
    mask = spec.accept(visitor, df)
    assert mask.tolist() == [False, True, True, False]


def test_visit_cmp_in_nin(visitor, df):
    spec = Cmp("name", "in", ["Alice", "Bob"])
    mask = spec.accept(visitor, df)
    assert mask.tolist() == [True, True, False, False]

    spec = Cmp("name", "nin", ["Alice"])
    mask = spec.accept(visitor, df)
    assert mask.tolist() == [False, True, True, True]


def test_visit_cmp_between(visitor, df):
    spec = Cmp("age", "between", (22, 32))
    mask = spec.accept(visitor, df)
    assert mask.tolist() == [False, True, True, False]


def test_visit_str(visitor, df):
    # contains
    spec = StrMatch("name", "contains", "li")  # Alice, Charlie
    mask = spec.accept(visitor, df)
    assert mask.tolist() == [True, False, True, False]

    # startswith
    spec = StrMatch("name", "startswith", "B")
    mask = spec.accept(visitor, df)
    assert mask.tolist() == [False, True, False, False]

    # regex
    spec = StrMatch("name", "regex", "^A.*e$")
    mask = spec.accept(visitor, df)
    assert mask.tolist() == [True, False, False, False]


def test_visit_null(visitor, df):
    spec = NullCheck("name", negate=False)
    mask = spec.accept(visitor, df)
    assert mask.tolist() == [False, False, False, True]

    spec = NullCheck("name", negate=True)
    mask = spec.accept(visitor, df)
    assert mask.tolist() == [True, True, True, False]


def test_visit_list_any(visitor, df):
    # contains
    spec = ListAny("tags", "contains", "python")
    mask = spec.accept(visitor, df)
    assert mask.tolist() == [True, False, False, False]

    # in
    spec = ListAny("tags", "in", ["finance", "other"])
    mask = spec.accept(visitor, df)
    assert mask.tolist() == [False, True, False, False]

    # overlap
    spec = ListAny("tags", "overlap", ["tech", "something"])
    mask = spec.accept(visitor, df)
    assert mask.tolist() == [True, False, True, False]


def test_logical_not(visitor, df):
    spec = Not(Cmp("age", "==", 20))
    mask = spec.accept(visitor, df)
    assert mask.tolist() == [False, True, True, True]


def test_logical_and(visitor, df):
    spec = And([Cmp("age", ">", 20), StrMatch("name", "startswith", "B")])
    mask = spec.accept(visitor, df)
    assert mask.tolist() == [False, True, False, False]


def test_logical_or(visitor, df):
    spec = Or([Cmp("age", "==", 20), StrMatch("name", "startswith", "C")])
    mask = spec.accept(visitor, df)
    assert mask.tolist() == [True, False, True, False]


def test_visit_cmp_datetime_and_unknown_operator(visitor, df):
    # Datetime handling
    spec_dt = Cmp("date", "==", pd.to_datetime("2021-01-01"))
    mask = spec_dt.accept(visitor, df)
    assert mask.tolist() == [False, True, False, False]

    # Operators >=, <, <=, !=
    spec_ge = Cmp("age", ">=", 25)
    assert spec_ge.accept(visitor, df).tolist() == [False, True, True, False]

    spec_lt = Cmp("age", "<", 25)
    assert spec_lt.accept(visitor, df).tolist() == [True, False, False, False]

    spec_le = Cmp("age", "<=", 25)
    assert spec_le.accept(visitor, df).tolist() == [True, True, False, False]

    spec_ne = Cmp("age", "!=", 25)
    assert spec_ne.accept(visitor, df).tolist() == [True, False, True, True]

    # Unknown operator
    with pytest.raises(ValueError, match="Operador desconhecido"):
        Cmp("age", "unknown_op", 10).accept(visitor, df)


def test_visit_str_endswith_and_unknown_mode(visitor, df):
    spec_ends = StrMatch("name", "endswith", "e")
    mask = spec_ends.accept(visitor, df)
    assert mask.tolist() == [True, False, True, False]

    with pytest.raises(ValueError, match="Modo string desconhecido"):
        StrMatch("name", "unknown_mode", "xx").accept(visitor, df)


def test_visit_list_any_unknown_operator(visitor, df):
    with pytest.raises(ValueError, match="Operador lista desconhecido"):
        ListAny("tags", "unknown_op", "val").accept(visitor, df)
