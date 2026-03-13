import pandas as pd
import pytest
from shared.infrastructure.adapters.pandas.visitor import PandasVisitor
from shared.domain.utils.specs import Cmp, StrMatch, NullCheck, ListAny, And, Or, Not

@pytest.fixture
def visitor():
    return PandasVisitor()

@pytest.fixture
def df():
    return pd.DataFrame({
        "age": [20, 25, 30, None],
        "name": ["Alice", "Bob", "Charlie", None],
        "tags": [["tech", "python"], ["finance"], ["tech"], []],
        "date": pd.to_datetime(["2020-01-01", "2021-01-01", "2022-01-01", None])
    })

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
    spec = StrMatch("name", "contains", "li") # Alice, Charlie
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
