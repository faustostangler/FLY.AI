"""Tests for the DDD base components.

These components define the sacred invariants and behavioral contract
expected across all Bounded Contexts for Entities, AggregateRoots,
and ValueObjects.
"""

import pytest
from pydantic import ValidationError

from shared.domain.entities import Entity, AggregateRoot, ValueObject


class DummyEntity(Entity):
    name: str
    age: int


class DummyAggregateRoot(AggregateRoot):
    id: str
    status: str


class DummyValueObject(ValueObject):
    currency: str
    amount: float


class ObjectFromAttributes:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)


class TestDomainBaseClasses:
    """Verifies the core DDD base classes behavior."""

    def test_entity_allows_from_attributes(self):
        """Entity must allow creation from arbitrary objects mapping ORM returns."""
        obj = ObjectFromAttributes(name="Test Name", age=30)
        # Using Pydantic V2 model_validate
        entity = DummyEntity.model_validate(obj)
        
        assert entity.name == "Test Name"
        assert entity.age == 30

    def test_aggregate_root_inherits_entity_behavior(self):
        """AggregateRoot should inherit the 'from_attributes' configuration of Entity."""
        obj = ObjectFromAttributes(id="agg-123", status="active")
        agg = DummyAggregateRoot.model_validate(obj)
        
        assert agg.id == "agg-123"
        assert agg.status == "active"
        assert isinstance(agg, Entity)

    def test_value_object_is_immutable(self):
        """Value Objects describe characteristics; thus they must be frozen (immutable)."""
        vo = DummyValueObject(currency="USD", amount=100.50)
        
        with pytest.raises(ValidationError):
            vo.amount = 200.00
            
    def test_value_object_equality(self):
        """Two Value Objects with identical attributes must be considered equal."""
        vo1 = DummyValueObject(currency="USD", amount=100.50)
        vo2 = DummyValueObject(currency="USD", amount=100.50)
        vo3 = DummyValueObject(currency="BRL", amount=100.50)
        
        assert vo1 == vo2
        assert vo1 != vo3
