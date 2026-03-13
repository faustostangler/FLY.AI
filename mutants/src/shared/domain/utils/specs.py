# domain/utils/specs.py
from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Iterable, Protocol, Mapping, Union
import pandas as pd
import numpy as np
from typing import Annotated
from typing import Callable
from typing import ClassVar

MutantDict = Annotated[dict[str, Callable], "Mutant"] # type: ignore


def _mutmut_trampoline(orig, mutants, call_args, call_kwargs, self_arg = None): # type: ignore
    """Forward call to original or mutated function, depending on the environment"""
    import os # type: ignore
    mutant_under_test = os.environ['MUTANT_UNDER_TEST'] # type: ignore
    if mutant_under_test == 'fail': # type: ignore
        from mutmut.__main__ import MutmutProgrammaticFailException # type: ignore
        raise MutmutProgrammaticFailException('Failed programmatically')       # type: ignore
    elif mutant_under_test == 'stats': # type: ignore
        from mutmut.__main__ import record_trampoline_hit # type: ignore
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__) # type: ignore
        # (for class methods, orig is bound and thus does not need the explicit self argument)
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_' # type: ignore
    if not mutant_under_test.startswith(prefix): # type: ignore
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    mutant_name = mutant_under_test.rpartition('.')[-1] # type: ignore
    if self_arg is not None: # type: ignore
        # call to a class method where self is not bound
        result = mutants[mutant_name](self_arg, *call_args, **call_kwargs) # type: ignore
    else:
        result = mutants[mutant_name](*call_args, **call_kwargs) # type: ignore
    return result # type: ignore

# Nós imutáveis
class Spec(Protocol):
    def accept(self, v: "PandasVisitor", df: pd.DataFrame) -> pd.Series: ...

@dataclass(frozen=True)
class And(Spec):
    items: tuple[Spec, ...]
    def accept(self, v, df): return v.visit_and(self, df)

@dataclass(frozen=True)
class Or(Spec):
    items: tuple[Spec, ...]
    def accept(self, v, df): return v.visit_or(self, df)

@dataclass(frozen=True)
class Not(Spec):
    item: Spec
    def accept(self, v, df): return v.visit_not(self, df)

@dataclass(frozen=True)
class Cmp(Spec):
    field: str
    op: str       # "==", "!=", ">", ">=", "<", "<=", "in", "nin", "between"
    value: Any    # escalar, sequência, ou (low, high)
    def accept(self, v, df): return v.visit_cmp(self, df)

@dataclass(frozen=True)
class StrMatch(Spec):
    field: str
    mode: str     # "contains", "startswith", "endswith", "regex"
    pattern: str
    case: bool = True
    na: bool = False
    def accept(self, v, df): return v.visit_str(self, df)

@dataclass(frozen=True)
class NullCheck(Spec):
    field: str
    negate: bool = False  # False -> isnull, True -> notnull
    def accept(self, v, df): return v.visit_null(self, df)

@dataclass(frozen=True)
class ListAny(Spec):
    """Para colunas JSON list (e.g., ticker_codes)."""
    field: str
    op: str       # "contains", "in", "overlap"
    value: Any
    def accept(self, v, df): return v.visit_list_any(self, df)
