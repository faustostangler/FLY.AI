import pytest
from shared.application.utils.filter_builder import FilterBuilder
from shared.domain.utils.specs import And, Or, Not, Cmp, StrMatch, NullCheck, ListAny

def test_build_spec_logical_and():
    d = {"and": [{"field1": "val1"}, {"field2": "val2"}]}
    spec = FilterBuilder.build_spec(d)
    assert isinstance(spec, And)
    assert len(spec.items) == 2
    assert spec.items[0].field == "field1"
    assert spec.items[1].field == "field2"

def test_build_spec_logical_or():
    d = {"or": [{"field1": "val1"}, {"field2": "val2"}]}
    spec = FilterBuilder.build_spec(d)
    assert isinstance(spec, Or)
    assert len(spec.items) == 2

def test_build_spec_logical_not():
    d = {"not": {"field": "val"}}
    spec = FilterBuilder.build_spec(d)
    assert isinstance(spec, Not)
    assert spec.item.field == "field"

def test_build_spec_cmp_operators():
    # Test common operators
    ops = {
        "eq": "==", "==": "==",
        "ne": "!=", "!=": "!=",
        "gt": ">",  ">":  ">",
        "gte": ">=", ">=": ">=",
        "lt": "<",  "<":  "<",
        "lte": "<=", "<=": "<=",
        "in": "in",
        "nin": "nin",
        "between": "between"
    }
    for op_key, expected_op in ops.items():
        val = [1, 10] if op_key == "between" else "value"
        d = {"price": {op_key: val}}
        spec = FilterBuilder.build_spec(d)
        if op_key == "in":
            assert isinstance(spec, ListAny)
            assert spec.op == "in"
        else:
            assert isinstance(spec, Cmp)
            assert spec.op == expected_op
        assert spec.value == val

def test_build_spec_null_checks():
    assert FilterBuilder.build_spec({"f": None}) == NullCheck("f", negate=False)
    assert FilterBuilder.build_spec({"f": "isnull"}) == NullCheck("f", negate=False)
    assert FilterBuilder.build_spec({"f": "notnull"}) == NullCheck("f", negate=True)

def test_build_spec_str_match():
    # Direct mode
    d = {"name": {"contains": "abc"}}
    spec = FilterBuilder.build_spec(d)
    assert isinstance(spec, StrMatch)
    assert spec.mode == "contains"
    assert spec.pattern == "abc"
    assert spec.case is True

    # With flags
    d = {"name": {"startswith": "abc", "case": False, "na": True}}
    spec = FilterBuilder.build_spec(d)
    assert spec.mode == "startswith"
    assert spec.case is False
    assert spec.na is True

    # Regex flag override
    d = {"name": {"contains": ".*", "regex": True}}
    spec = FilterBuilder.build_spec(d)
    assert spec.mode == "regex"

def test_build_spec_list_any():
    d = {"tags": {"overlap": ["A", "B"]}}
    spec = FilterBuilder.build_spec(d)
    assert isinstance(spec, ListAny)
    assert spec.op == "overlap"
    assert spec.value == ["A", "B"]

def test_build_spec_implicit_or_from_list():
    d = [{"f1": "v1"}, {"f2": "v2"}]
    spec = FilterBuilder.build_spec(d)
    assert isinstance(spec, Or)
    assert len(spec.items) == 2

def test_build_spec_invalid():
    with pytest.raises(ValueError):
        FilterBuilder.build_spec(123)
