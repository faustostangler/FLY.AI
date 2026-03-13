import pytest
import pandas as pd

from shared.application.utils.filter_builder import FilterBuilder
from shared.domain.value_objects.search_filter_tree import SearchFilterTree
from shared.infrastructure.adapters.pandas.visitor import PandasVisitor


def test_filtered_by_fields_keeps_only_allowed_leaves():
    tree_raw = {
        "and": [
            {"industry_segment": {"in": ["TECNOLOGIA"]}},
            {"date": {">=": "2020-01-01"}},
        ]
    }
    tree = SearchFilterTree.from_raw(tree_raw)

    filtered = tree.filtered_by_fields({"date"})

    assert filtered is not None
    assert filtered.to_dict() == {"and": [{"date": {">=": "2020-01-01"}}]}


def test_filtered_by_fields_returns_none_when_all_pruned():
    tree_raw = {"industry_segment": {"in": ["TECNOLOGIA"]}}
    tree = SearchFilterTree.from_raw(tree_raw)

    assert tree.filtered_by_fields({"date"}) is None


def test_filtered_tree_works_with_filter_builder():
    tree_raw = {
        "and": [
            {"industry_segment": {"in": ["TECNOLOGIA"]}},
            {"date": {">=": "2020-01-01"}},
        ]
    }
    tree = SearchFilterTree.from_raw(tree_raw)
    filtered = tree.filtered_by_fields({"date"})

    df = pd.DataFrame(
        {
            "date": pd.to_datetime(["2019-01-01", "2021-05-10"]),
            "value": [1, 2],
        }
    )

    spec = FilterBuilder().build_spec(filtered.to_dict())
    mask = spec.accept(PandasVisitor(), df)

    filtered_df = df[mask]

    assert len(filtered_df) == 1
    assert filtered_df.iloc[0]["value"] == 2

def test_search_filter_tree_hash_is_deterministic():
    tree1 = SearchFilterTree.from_raw({"and": [{"f1": "v1"}, {"f2": "v2"}]})
    tree2 = SearchFilterTree.from_raw({"and": [{"f1": "v1"}, {"f2": "v2"}]})
    
    assert tree1.to_hash() == tree2.to_hash()

def test_search_filter_tree_is_empty():
    assert SearchFilterTree.from_raw({}).is_empty() is True
    assert SearchFilterTree.from_raw({"f": "v"}).is_empty() is False

def test_search_filter_tree_invalid_data():
    with pytest.raises(TypeError):
        SearchFilterTree.from_raw("not a dict")

def test_search_filter_tree_none():
    assert SearchFilterTree.from_raw(None) is None
