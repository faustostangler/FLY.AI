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

def test_search_filter_tree_from_raw_returns_same_instance():
    tree = SearchFilterTree({"f": "v"})
    assert SearchFilterTree.from_raw(tree) is tree

def test_search_filter_tree_hash_empty():
    tree = SearchFilterTree({})
    assert tree.to_hash() == tree._empty_hash()

def test_filtered_by_fields_returns_none_when_empty():
    tree = SearchFilterTree({})
    assert tree.filtered_by_fields({"date"}) is None

def test_filtered_by_fields_or_clause():
    tree_raw = {
        "or": [
            {"industry_segment": {"in": ["TECNOLOGIA"]}},
            {"date": {">=": "2020-01-01"}},
        ]
    }
    tree = SearchFilterTree.from_raw(tree_raw)
    filtered = tree.filtered_by_fields({"date"})
    assert filtered.to_dict() == {"or": [{"date": {">=": "2020-01-01"}}]}

def test_filtered_by_fields_or_clause_empty():
    tree_raw = {"or": [{"f1": "v1"}]}
    tree = SearchFilterTree.from_raw(tree_raw)
    filtered = tree.filtered_by_fields({"f2"})
    assert filtered is None

def test_filtered_by_fields_and_clause_empty():
    tree_raw = {"and": [{"f1": "v1"}]}
    tree = SearchFilterTree.from_raw(tree_raw)
    filtered = tree.filtered_by_fields({"f2"})
    assert filtered is None

def test_filtered_by_fields_not_clause():
    tree_raw = {"not": {"f1": "v1"}}
    tree = SearchFilterTree.from_raw(tree_raw)
    assert tree.filtered_by_fields({"f1"}).to_dict() == {"not": {"f1": "v1"}}

def test_filtered_by_fields_not_clause_empty():
    tree_raw = {"not": {"f1": "v1"}}
    tree = SearchFilterTree.from_raw(tree_raw)
    assert tree.filtered_by_fields({"f2"}) is None

def test_filtered_by_fields_list_handling():
    # To hit line 123 in the dict block:
    # A dict with length > 1, but doesn't match 'and'/'or'/'not'.
    # e.g., {"f1": "v1", "f2": "v2"} -> drops down past `if len(node) == 1:`
    # We put it in an array so it bypasses from_raw structure limits or just use constructor.
    tree = SearchFilterTree({"unknown_multi_key": "val1", "another_key": "val2"}) # type: ignore
    # Returns the node as-is (line 123 `return node`)
    res = tree.filtered_by_fields({"f1"})
    assert res is not None
    assert res.to_dict() == {"unknown_multi_key": "val1", "another_key": "val2"}

def test_filtered_by_fields_list_nested_handling():
    tree3 = SearchFilterTree(["literal_string_in_list", {"f1": "v1"}]) # type: ignore
    res = tree3.filtered_by_fields({"f1"})
    # The valid dict {"f1": "v1"} is retained, list elements that are strings evaluate to None in _filter_node(str)
    # The final array has length 1
    assert res is not None
    assert res.to_dict() == [{"f1": "v1"}] # type: ignore

def test_filtered_by_fields_list_all_pruned():
    tree = SearchFilterTree(["string_val", [{"invalid": "child"}]]) # type: ignore
    res = tree.filtered_by_fields({"f1"})
    assert res is None

def test_filter_node_returns_none_non_dict_non_list():
    # To hit line 132 `return None` we need _filter_node to encouter a literal like a string outside of a proper node
    # The only way is if root itself is a string/int
    tree2 = SearchFilterTree("string_payload") # type: ignore
    assert tree2.filtered_by_fields({"field"}) is None

