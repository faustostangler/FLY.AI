from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional
import uuid

class Entity(BaseModel):
    """Base class for all Domain Entities"""
    model_config = ConfigDict(from_attributes=True)

class AggregateRoot(Entity):
    """Base class for Aggregate Roots"""
    pass

class ValueObject(BaseModel):
    """Base class for Value Objects"""
    model_config = ConfigDict(frozen=True)
