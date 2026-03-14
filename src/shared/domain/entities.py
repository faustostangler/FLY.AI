from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional
import uuid

class Entity(BaseModel):
    """Base class for all Domain Entities.

    Entities possess a unique identity that persists across state 
    changes. Inheriting from this base ensures consistent configuration 
    for ORM mapping and attribute access.
    """
    model_config = ConfigDict(from_attributes=True)

class AggregateRoot(Entity):
    """A cluster of associated objects that we treat as a unit for data changes.

    The Aggregate Root is the only entry point for modifying the 
    aggregate, ensuring that all business invariants remain satisfied 
    within the boundary.
    """
    pass

class ValueObject(BaseModel):
    """Objects that describe characteristics but have no conceptual identity.

    Value Objects are immutable by design (frozen=True). Two value objects 
    are equal if all their attributes are equal. This immutability 
    simplifies the domain logic and prevents side effects.
    """
    model_config = ConfigDict(frozen=True)
