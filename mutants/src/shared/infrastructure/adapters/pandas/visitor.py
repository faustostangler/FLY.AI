# infrastructure/utils/pandas_visitor.py
import pandas as pd
import re
from .types import ensure_datetime_col, ensure_list_col
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


class PandasVisitor:
    """Converte Spec -> mask booleana, respeitando tipo da coluna."""

    def visit_and(self, node, df):
        args = [node, df]  # type: ignore
        kwargs = {}  # type: ignore
        return _mutmut_trampoline(
            object.__getattribute__(self, "xǁPandasVisitorǁvisit_and__mutmut_orig"),
            object.__getattribute__(self, "xǁPandasVisitorǁvisit_and__mutmut_mutants"),
            args,
            kwargs,
            self,
        )

    def xǁPandasVisitorǁvisit_and__mutmut_orig(self, node, df):
        m = pd.Series(True, index=df.index)
        for it in node.items:
            m &= it.accept(self, df)
        return m

    def xǁPandasVisitorǁvisit_and__mutmut_1(self, node, df):
        m = None
        for it in node.items:
            m &= it.accept(self, df)
        return m

    def xǁPandasVisitorǁvisit_and__mutmut_2(self, node, df):
        m = pd.Series(None, index=df.index)
        for it in node.items:
            m &= it.accept(self, df)
        return m

    def xǁPandasVisitorǁvisit_and__mutmut_3(self, node, df):
        m = pd.Series(True, index=None)
        for it in node.items:
            m &= it.accept(self, df)
        return m

    def xǁPandasVisitorǁvisit_and__mutmut_4(self, node, df):
        m = pd.Series(index=df.index)
        for it in node.items:
            m &= it.accept(self, df)
        return m

    def xǁPandasVisitorǁvisit_and__mutmut_5(self, node, df):
        m = pd.Series(
            True,
        )
        for it in node.items:
            m &= it.accept(self, df)
        return m

    def xǁPandasVisitorǁvisit_and__mutmut_6(self, node, df):
        m = pd.Series(False, index=df.index)
        for it in node.items:
            m &= it.accept(self, df)
        return m

    def xǁPandasVisitorǁvisit_and__mutmut_7(self, node, df):
        m = pd.Series(True, index=df.index)
        for it in node.items:
            m = it.accept(self, df)
        return m

    def xǁPandasVisitorǁvisit_and__mutmut_8(self, node, df):
        m = pd.Series(True, index=df.index)
        for it in node.items:
            m |= it.accept(self, df)
        return m

    def xǁPandasVisitorǁvisit_and__mutmut_9(self, node, df):
        m = pd.Series(True, index=df.index)
        for it in node.items:
            m &= it.accept(None, df)
        return m

    def xǁPandasVisitorǁvisit_and__mutmut_10(self, node, df):
        m = pd.Series(True, index=df.index)
        for it in node.items:
            m &= it.accept(self, None)
        return m

    def xǁPandasVisitorǁvisit_and__mutmut_11(self, node, df):
        m = pd.Series(True, index=df.index)
        for it in node.items:
            m &= it.accept(df)
        return m

    def xǁPandasVisitorǁvisit_and__mutmut_12(self, node, df):
        m = pd.Series(True, index=df.index)
        for it in node.items:
            m &= it.accept(
                self,
            )
        return m

    xǁPandasVisitorǁvisit_and__mutmut_mutants: ClassVar[MutantDict] = {  # type: ignore
        "xǁPandasVisitorǁvisit_and__mutmut_1": xǁPandasVisitorǁvisit_and__mutmut_1,
        "xǁPandasVisitorǁvisit_and__mutmut_2": xǁPandasVisitorǁvisit_and__mutmut_2,
        "xǁPandasVisitorǁvisit_and__mutmut_3": xǁPandasVisitorǁvisit_and__mutmut_3,
        "xǁPandasVisitorǁvisit_and__mutmut_4": xǁPandasVisitorǁvisit_and__mutmut_4,
        "xǁPandasVisitorǁvisit_and__mutmut_5": xǁPandasVisitorǁvisit_and__mutmut_5,
        "xǁPandasVisitorǁvisit_and__mutmut_6": xǁPandasVisitorǁvisit_and__mutmut_6,
        "xǁPandasVisitorǁvisit_and__mutmut_7": xǁPandasVisitorǁvisit_and__mutmut_7,
        "xǁPandasVisitorǁvisit_and__mutmut_8": xǁPandasVisitorǁvisit_and__mutmut_8,
        "xǁPandasVisitorǁvisit_and__mutmut_9": xǁPandasVisitorǁvisit_and__mutmut_9,
        "xǁPandasVisitorǁvisit_and__mutmut_10": xǁPandasVisitorǁvisit_and__mutmut_10,
        "xǁPandasVisitorǁvisit_and__mutmut_11": xǁPandasVisitorǁvisit_and__mutmut_11,
        "xǁPandasVisitorǁvisit_and__mutmut_12": xǁPandasVisitorǁvisit_and__mutmut_12,
    }
    xǁPandasVisitorǁvisit_and__mutmut_orig.__name__ = "xǁPandasVisitorǁvisit_and"

    def visit_or(self, node, df):
        args = [node, df]  # type: ignore
        kwargs = {}  # type: ignore
        return _mutmut_trampoline(
            object.__getattribute__(self, "xǁPandasVisitorǁvisit_or__mutmut_orig"),
            object.__getattribute__(self, "xǁPandasVisitorǁvisit_or__mutmut_mutants"),
            args,
            kwargs,
            self,
        )

    def xǁPandasVisitorǁvisit_or__mutmut_orig(self, node, df):
        m = pd.Series(False, index=df.index)
        for it in node.items:
            m |= it.accept(self, df)
        return m

    def xǁPandasVisitorǁvisit_or__mutmut_1(self, node, df):
        m = None
        for it in node.items:
            m |= it.accept(self, df)
        return m

    def xǁPandasVisitorǁvisit_or__mutmut_2(self, node, df):
        m = pd.Series(None, index=df.index)
        for it in node.items:
            m |= it.accept(self, df)
        return m

    def xǁPandasVisitorǁvisit_or__mutmut_3(self, node, df):
        m = pd.Series(False, index=None)
        for it in node.items:
            m |= it.accept(self, df)
        return m

    def xǁPandasVisitorǁvisit_or__mutmut_4(self, node, df):
        m = pd.Series(index=df.index)
        for it in node.items:
            m |= it.accept(self, df)
        return m

    def xǁPandasVisitorǁvisit_or__mutmut_5(self, node, df):
        m = pd.Series(
            False,
        )
        for it in node.items:
            m |= it.accept(self, df)
        return m

    def xǁPandasVisitorǁvisit_or__mutmut_6(self, node, df):
        m = pd.Series(True, index=df.index)
        for it in node.items:
            m |= it.accept(self, df)
        return m

    def xǁPandasVisitorǁvisit_or__mutmut_7(self, node, df):
        m = pd.Series(False, index=df.index)
        for it in node.items:
            m = it.accept(self, df)
        return m

    def xǁPandasVisitorǁvisit_or__mutmut_8(self, node, df):
        m = pd.Series(False, index=df.index)
        for it in node.items:
            m &= it.accept(self, df)
        return m

    def xǁPandasVisitorǁvisit_or__mutmut_9(self, node, df):
        m = pd.Series(False, index=df.index)
        for it in node.items:
            m |= it.accept(None, df)
        return m

    def xǁPandasVisitorǁvisit_or__mutmut_10(self, node, df):
        m = pd.Series(False, index=df.index)
        for it in node.items:
            m |= it.accept(self, None)
        return m

    def xǁPandasVisitorǁvisit_or__mutmut_11(self, node, df):
        m = pd.Series(False, index=df.index)
        for it in node.items:
            m |= it.accept(df)
        return m

    def xǁPandasVisitorǁvisit_or__mutmut_12(self, node, df):
        m = pd.Series(False, index=df.index)
        for it in node.items:
            m |= it.accept(
                self,
            )
        return m

    xǁPandasVisitorǁvisit_or__mutmut_mutants: ClassVar[MutantDict] = {  # type: ignore
        "xǁPandasVisitorǁvisit_or__mutmut_1": xǁPandasVisitorǁvisit_or__mutmut_1,
        "xǁPandasVisitorǁvisit_or__mutmut_2": xǁPandasVisitorǁvisit_or__mutmut_2,
        "xǁPandasVisitorǁvisit_or__mutmut_3": xǁPandasVisitorǁvisit_or__mutmut_3,
        "xǁPandasVisitorǁvisit_or__mutmut_4": xǁPandasVisitorǁvisit_or__mutmut_4,
        "xǁPandasVisitorǁvisit_or__mutmut_5": xǁPandasVisitorǁvisit_or__mutmut_5,
        "xǁPandasVisitorǁvisit_or__mutmut_6": xǁPandasVisitorǁvisit_or__mutmut_6,
        "xǁPandasVisitorǁvisit_or__mutmut_7": xǁPandasVisitorǁvisit_or__mutmut_7,
        "xǁPandasVisitorǁvisit_or__mutmut_8": xǁPandasVisitorǁvisit_or__mutmut_8,
        "xǁPandasVisitorǁvisit_or__mutmut_9": xǁPandasVisitorǁvisit_or__mutmut_9,
        "xǁPandasVisitorǁvisit_or__mutmut_10": xǁPandasVisitorǁvisit_or__mutmut_10,
        "xǁPandasVisitorǁvisit_or__mutmut_11": xǁPandasVisitorǁvisit_or__mutmut_11,
        "xǁPandasVisitorǁvisit_or__mutmut_12": xǁPandasVisitorǁvisit_or__mutmut_12,
    }
    xǁPandasVisitorǁvisit_or__mutmut_orig.__name__ = "xǁPandasVisitorǁvisit_or"

    def visit_not(self, node, df):
        args = [node, df]  # type: ignore
        kwargs = {}  # type: ignore
        return _mutmut_trampoline(
            object.__getattribute__(self, "xǁPandasVisitorǁvisit_not__mutmut_orig"),
            object.__getattribute__(self, "xǁPandasVisitorǁvisit_not__mutmut_mutants"),
            args,
            kwargs,
            self,
        )

    def xǁPandasVisitorǁvisit_not__mutmut_orig(self, node, df):
        return ~node.item.accept(self, df)

    def xǁPandasVisitorǁvisit_not__mutmut_1(self, node, df):
        return node.item.accept(self, df)

    def xǁPandasVisitorǁvisit_not__mutmut_2(self, node, df):
        return ~node.item.accept(None, df)

    def xǁPandasVisitorǁvisit_not__mutmut_3(self, node, df):
        return ~node.item.accept(self, None)

    def xǁPandasVisitorǁvisit_not__mutmut_4(self, node, df):
        return ~node.item.accept(df)

    def xǁPandasVisitorǁvisit_not__mutmut_5(self, node, df):
        return ~node.item.accept(
            self,
        )

    xǁPandasVisitorǁvisit_not__mutmut_mutants: ClassVar[MutantDict] = {  # type: ignore
        "xǁPandasVisitorǁvisit_not__mutmut_1": xǁPandasVisitorǁvisit_not__mutmut_1,
        "xǁPandasVisitorǁvisit_not__mutmut_2": xǁPandasVisitorǁvisit_not__mutmut_2,
        "xǁPandasVisitorǁvisit_not__mutmut_3": xǁPandasVisitorǁvisit_not__mutmut_3,
        "xǁPandasVisitorǁvisit_not__mutmut_4": xǁPandasVisitorǁvisit_not__mutmut_4,
        "xǁPandasVisitorǁvisit_not__mutmut_5": xǁPandasVisitorǁvisit_not__mutmut_5,
    }
    xǁPandasVisitorǁvisit_not__mutmut_orig.__name__ = "xǁPandasVisitorǁvisit_not"

    def visit_null(self, node, df):
        args = [node, df]  # type: ignore
        kwargs = {}  # type: ignore
        return _mutmut_trampoline(
            object.__getattribute__(self, "xǁPandasVisitorǁvisit_null__mutmut_orig"),
            object.__getattribute__(self, "xǁPandasVisitorǁvisit_null__mutmut_mutants"),
            args,
            kwargs,
            self,
        )

    def xǁPandasVisitorǁvisit_null__mutmut_orig(self, node, df):
        s = df[node.field]
        m = s.isna()
        return ~m if node.negate else m

    def xǁPandasVisitorǁvisit_null__mutmut_1(self, node, df):
        s = None
        m = s.isna()
        return ~m if node.negate else m

    def xǁPandasVisitorǁvisit_null__mutmut_2(self, node, df):
        s = df[node.field]
        m = None
        return ~m if node.negate else m

    def xǁPandasVisitorǁvisit_null__mutmut_3(self, node, df):
        s = df[node.field]
        m = s.isna()
        return m if node.negate else m

    xǁPandasVisitorǁvisit_null__mutmut_mutants: ClassVar[MutantDict] = {  # type: ignore
        "xǁPandasVisitorǁvisit_null__mutmut_1": xǁPandasVisitorǁvisit_null__mutmut_1,
        "xǁPandasVisitorǁvisit_null__mutmut_2": xǁPandasVisitorǁvisit_null__mutmut_2,
        "xǁPandasVisitorǁvisit_null__mutmut_3": xǁPandasVisitorǁvisit_null__mutmut_3,
    }
    xǁPandasVisitorǁvisit_null__mutmut_orig.__name__ = "xǁPandasVisitorǁvisit_null"

    def visit_cmp(self, node, df):
        args = [node, df]  # type: ignore
        kwargs = {}  # type: ignore
        return _mutmut_trampoline(
            object.__getattribute__(self, "xǁPandasVisitorǁvisit_cmp__mutmut_orig"),
            object.__getattribute__(self, "xǁPandasVisitorǁvisit_cmp__mutmut_mutants"),
            args,
            kwargs,
            self,
        )

    def xǁPandasVisitorǁvisit_cmp__mutmut_orig(self, node, df):
        s = df[node.field]
        # Datas convertidas quando necessário
        if str(s.dtype).startswith(("datetime", "date")):
            s = ensure_datetime_col(s)
        op, val = node.op, node.value

        if op == "in":
            vals = set(val if isinstance(val, (list, tuple, set)) else [val])
            return s.isin(vals)
        if op == "nin":
            vals = set(val if isinstance(val, (list, tuple, set)) else [val])
            return ~s.isin(vals)
        if op == "between":
            low, high = val
            return s.between(low, high, inclusive="both")
        if op == "==":
            return s.eq(val)
        if op == "!=":
            return s.ne(val)
        if op == ">":
            return s.gt(val)
        if op == ">=":
            return s.ge(val)
        if op == "<":
            return s.lt(val)
        if op == "<=":
            return s.le(val)
        raise ValueError(f"Operador desconhecido: {op}")

    def xǁPandasVisitorǁvisit_cmp__mutmut_1(self, node, df):
        s = None
        # Datas convertidas quando necessário
        if str(s.dtype).startswith(("datetime", "date")):
            s = ensure_datetime_col(s)
        op, val = node.op, node.value

        if op == "in":
            vals = set(val if isinstance(val, (list, tuple, set)) else [val])
            return s.isin(vals)
        if op == "nin":
            vals = set(val if isinstance(val, (list, tuple, set)) else [val])
            return ~s.isin(vals)
        if op == "between":
            low, high = val
            return s.between(low, high, inclusive="both")
        if op == "==":
            return s.eq(val)
        if op == "!=":
            return s.ne(val)
        if op == ">":
            return s.gt(val)
        if op == ">=":
            return s.ge(val)
        if op == "<":
            return s.lt(val)
        if op == "<=":
            return s.le(val)
        raise ValueError(f"Operador desconhecido: {op}")

    def xǁPandasVisitorǁvisit_cmp__mutmut_2(self, node, df):
        s = df[node.field]
        # Datas convertidas quando necessário
        if str(s.dtype).startswith(None):
            s = ensure_datetime_col(s)
        op, val = node.op, node.value

        if op == "in":
            vals = set(val if isinstance(val, (list, tuple, set)) else [val])
            return s.isin(vals)
        if op == "nin":
            vals = set(val if isinstance(val, (list, tuple, set)) else [val])
            return ~s.isin(vals)
        if op == "between":
            low, high = val
            return s.between(low, high, inclusive="both")
        if op == "==":
            return s.eq(val)
        if op == "!=":
            return s.ne(val)
        if op == ">":
            return s.gt(val)
        if op == ">=":
            return s.ge(val)
        if op == "<":
            return s.lt(val)
        if op == "<=":
            return s.le(val)
        raise ValueError(f"Operador desconhecido: {op}")

    def xǁPandasVisitorǁvisit_cmp__mutmut_3(self, node, df):
        s = df[node.field]
        # Datas convertidas quando necessário
        if str(None).startswith(("datetime", "date")):
            s = ensure_datetime_col(s)
        op, val = node.op, node.value

        if op == "in":
            vals = set(val if isinstance(val, (list, tuple, set)) else [val])
            return s.isin(vals)
        if op == "nin":
            vals = set(val if isinstance(val, (list, tuple, set)) else [val])
            return ~s.isin(vals)
        if op == "between":
            low, high = val
            return s.between(low, high, inclusive="both")
        if op == "==":
            return s.eq(val)
        if op == "!=":
            return s.ne(val)
        if op == ">":
            return s.gt(val)
        if op == ">=":
            return s.ge(val)
        if op == "<":
            return s.lt(val)
        if op == "<=":
            return s.le(val)
        raise ValueError(f"Operador desconhecido: {op}")

    def xǁPandasVisitorǁvisit_cmp__mutmut_4(self, node, df):
        s = df[node.field]
        # Datas convertidas quando necessário
        if str(s.dtype).startswith(("XXdatetimeXX", "date")):
            s = ensure_datetime_col(s)
        op, val = node.op, node.value

        if op == "in":
            vals = set(val if isinstance(val, (list, tuple, set)) else [val])
            return s.isin(vals)
        if op == "nin":
            vals = set(val if isinstance(val, (list, tuple, set)) else [val])
            return ~s.isin(vals)
        if op == "between":
            low, high = val
            return s.between(low, high, inclusive="both")
        if op == "==":
            return s.eq(val)
        if op == "!=":
            return s.ne(val)
        if op == ">":
            return s.gt(val)
        if op == ">=":
            return s.ge(val)
        if op == "<":
            return s.lt(val)
        if op == "<=":
            return s.le(val)
        raise ValueError(f"Operador desconhecido: {op}")

    def xǁPandasVisitorǁvisit_cmp__mutmut_5(self, node, df):
        s = df[node.field]
        # Datas convertidas quando necessário
        if str(s.dtype).startswith(("DATETIME", "date")):
            s = ensure_datetime_col(s)
        op, val = node.op, node.value

        if op == "in":
            vals = set(val if isinstance(val, (list, tuple, set)) else [val])
            return s.isin(vals)
        if op == "nin":
            vals = set(val if isinstance(val, (list, tuple, set)) else [val])
            return ~s.isin(vals)
        if op == "between":
            low, high = val
            return s.between(low, high, inclusive="both")
        if op == "==":
            return s.eq(val)
        if op == "!=":
            return s.ne(val)
        if op == ">":
            return s.gt(val)
        if op == ">=":
            return s.ge(val)
        if op == "<":
            return s.lt(val)
        if op == "<=":
            return s.le(val)
        raise ValueError(f"Operador desconhecido: {op}")

    def xǁPandasVisitorǁvisit_cmp__mutmut_6(self, node, df):
        s = df[node.field]
        # Datas convertidas quando necessário
        if str(s.dtype).startswith(("datetime", "XXdateXX")):
            s = ensure_datetime_col(s)
        op, val = node.op, node.value

        if op == "in":
            vals = set(val if isinstance(val, (list, tuple, set)) else [val])
            return s.isin(vals)
        if op == "nin":
            vals = set(val if isinstance(val, (list, tuple, set)) else [val])
            return ~s.isin(vals)
        if op == "between":
            low, high = val
            return s.between(low, high, inclusive="both")
        if op == "==":
            return s.eq(val)
        if op == "!=":
            return s.ne(val)
        if op == ">":
            return s.gt(val)
        if op == ">=":
            return s.ge(val)
        if op == "<":
            return s.lt(val)
        if op == "<=":
            return s.le(val)
        raise ValueError(f"Operador desconhecido: {op}")

    def xǁPandasVisitorǁvisit_cmp__mutmut_7(self, node, df):
        s = df[node.field]
        # Datas convertidas quando necessário
        if str(s.dtype).startswith(("datetime", "DATE")):
            s = ensure_datetime_col(s)
        op, val = node.op, node.value

        if op == "in":
            vals = set(val if isinstance(val, (list, tuple, set)) else [val])
            return s.isin(vals)
        if op == "nin":
            vals = set(val if isinstance(val, (list, tuple, set)) else [val])
            return ~s.isin(vals)
        if op == "between":
            low, high = val
            return s.between(low, high, inclusive="both")
        if op == "==":
            return s.eq(val)
        if op == "!=":
            return s.ne(val)
        if op == ">":
            return s.gt(val)
        if op == ">=":
            return s.ge(val)
        if op == "<":
            return s.lt(val)
        if op == "<=":
            return s.le(val)
        raise ValueError(f"Operador desconhecido: {op}")

    def xǁPandasVisitorǁvisit_cmp__mutmut_8(self, node, df):
        s = df[node.field]
        # Datas convertidas quando necessário
        if str(s.dtype).startswith(("datetime", "date")):
            s = None
        op, val = node.op, node.value

        if op == "in":
            vals = set(val if isinstance(val, (list, tuple, set)) else [val])
            return s.isin(vals)
        if op == "nin":
            vals = set(val if isinstance(val, (list, tuple, set)) else [val])
            return ~s.isin(vals)
        if op == "between":
            low, high = val
            return s.between(low, high, inclusive="both")
        if op == "==":
            return s.eq(val)
        if op == "!=":
            return s.ne(val)
        if op == ">":
            return s.gt(val)
        if op == ">=":
            return s.ge(val)
        if op == "<":
            return s.lt(val)
        if op == "<=":
            return s.le(val)
        raise ValueError(f"Operador desconhecido: {op}")

    def xǁPandasVisitorǁvisit_cmp__mutmut_9(self, node, df):
        s = df[node.field]
        # Datas convertidas quando necessário
        if str(s.dtype).startswith(("datetime", "date")):
            s = ensure_datetime_col(None)
        op, val = node.op, node.value

        if op == "in":
            vals = set(val if isinstance(val, (list, tuple, set)) else [val])
            return s.isin(vals)
        if op == "nin":
            vals = set(val if isinstance(val, (list, tuple, set)) else [val])
            return ~s.isin(vals)
        if op == "between":
            low, high = val
            return s.between(low, high, inclusive="both")
        if op == "==":
            return s.eq(val)
        if op == "!=":
            return s.ne(val)
        if op == ">":
            return s.gt(val)
        if op == ">=":
            return s.ge(val)
        if op == "<":
            return s.lt(val)
        if op == "<=":
            return s.le(val)
        raise ValueError(f"Operador desconhecido: {op}")

    def xǁPandasVisitorǁvisit_cmp__mutmut_10(self, node, df):
        s = df[node.field]
        # Datas convertidas quando necessário
        if str(s.dtype).startswith(("datetime", "date")):
            s = ensure_datetime_col(s)
        op, val = None

        if op == "in":
            vals = set(val if isinstance(val, (list, tuple, set)) else [val])
            return s.isin(vals)
        if op == "nin":
            vals = set(val if isinstance(val, (list, tuple, set)) else [val])
            return ~s.isin(vals)
        if op == "between":
            low, high = val
            return s.between(low, high, inclusive="both")
        if op == "==":
            return s.eq(val)
        if op == "!=":
            return s.ne(val)
        if op == ">":
            return s.gt(val)
        if op == ">=":
            return s.ge(val)
        if op == "<":
            return s.lt(val)
        if op == "<=":
            return s.le(val)
        raise ValueError(f"Operador desconhecido: {op}")

    def xǁPandasVisitorǁvisit_cmp__mutmut_11(self, node, df):
        s = df[node.field]
        # Datas convertidas quando necessário
        if str(s.dtype).startswith(("datetime", "date")):
            s = ensure_datetime_col(s)
        op, val = node.op, node.value

        if op != "in":
            vals = set(val if isinstance(val, (list, tuple, set)) else [val])
            return s.isin(vals)
        if op == "nin":
            vals = set(val if isinstance(val, (list, tuple, set)) else [val])
            return ~s.isin(vals)
        if op == "between":
            low, high = val
            return s.between(low, high, inclusive="both")
        if op == "==":
            return s.eq(val)
        if op == "!=":
            return s.ne(val)
        if op == ">":
            return s.gt(val)
        if op == ">=":
            return s.ge(val)
        if op == "<":
            return s.lt(val)
        if op == "<=":
            return s.le(val)
        raise ValueError(f"Operador desconhecido: {op}")

    def xǁPandasVisitorǁvisit_cmp__mutmut_12(self, node, df):
        s = df[node.field]
        # Datas convertidas quando necessário
        if str(s.dtype).startswith(("datetime", "date")):
            s = ensure_datetime_col(s)
        op, val = node.op, node.value

        if op == "XXinXX":
            vals = set(val if isinstance(val, (list, tuple, set)) else [val])
            return s.isin(vals)
        if op == "nin":
            vals = set(val if isinstance(val, (list, tuple, set)) else [val])
            return ~s.isin(vals)
        if op == "between":
            low, high = val
            return s.between(low, high, inclusive="both")
        if op == "==":
            return s.eq(val)
        if op == "!=":
            return s.ne(val)
        if op == ">":
            return s.gt(val)
        if op == ">=":
            return s.ge(val)
        if op == "<":
            return s.lt(val)
        if op == "<=":
            return s.le(val)
        raise ValueError(f"Operador desconhecido: {op}")

    def xǁPandasVisitorǁvisit_cmp__mutmut_13(self, node, df):
        s = df[node.field]
        # Datas convertidas quando necessário
        if str(s.dtype).startswith(("datetime", "date")):
            s = ensure_datetime_col(s)
        op, val = node.op, node.value

        if op == "IN":
            vals = set(val if isinstance(val, (list, tuple, set)) else [val])
            return s.isin(vals)
        if op == "nin":
            vals = set(val if isinstance(val, (list, tuple, set)) else [val])
            return ~s.isin(vals)
        if op == "between":
            low, high = val
            return s.between(low, high, inclusive="both")
        if op == "==":
            return s.eq(val)
        if op == "!=":
            return s.ne(val)
        if op == ">":
            return s.gt(val)
        if op == ">=":
            return s.ge(val)
        if op == "<":
            return s.lt(val)
        if op == "<=":
            return s.le(val)
        raise ValueError(f"Operador desconhecido: {op}")

    def xǁPandasVisitorǁvisit_cmp__mutmut_14(self, node, df):
        s = df[node.field]
        # Datas convertidas quando necessário
        if str(s.dtype).startswith(("datetime", "date")):
            s = ensure_datetime_col(s)
        op, val = node.op, node.value

        if op == "in":
            vals = None
            return s.isin(vals)
        if op == "nin":
            vals = set(val if isinstance(val, (list, tuple, set)) else [val])
            return ~s.isin(vals)
        if op == "between":
            low, high = val
            return s.between(low, high, inclusive="both")
        if op == "==":
            return s.eq(val)
        if op == "!=":
            return s.ne(val)
        if op == ">":
            return s.gt(val)
        if op == ">=":
            return s.ge(val)
        if op == "<":
            return s.lt(val)
        if op == "<=":
            return s.le(val)
        raise ValueError(f"Operador desconhecido: {op}")

    def xǁPandasVisitorǁvisit_cmp__mutmut_15(self, node, df):
        s = df[node.field]
        # Datas convertidas quando necessário
        if str(s.dtype).startswith(("datetime", "date")):
            s = ensure_datetime_col(s)
        op, val = node.op, node.value

        if op == "in":
            vals = set(None)
            return s.isin(vals)
        if op == "nin":
            vals = set(val if isinstance(val, (list, tuple, set)) else [val])
            return ~s.isin(vals)
        if op == "between":
            low, high = val
            return s.between(low, high, inclusive="both")
        if op == "==":
            return s.eq(val)
        if op == "!=":
            return s.ne(val)
        if op == ">":
            return s.gt(val)
        if op == ">=":
            return s.ge(val)
        if op == "<":
            return s.lt(val)
        if op == "<=":
            return s.le(val)
        raise ValueError(f"Operador desconhecido: {op}")

    def xǁPandasVisitorǁvisit_cmp__mutmut_16(self, node, df):
        s = df[node.field]
        # Datas convertidas quando necessário
        if str(s.dtype).startswith(("datetime", "date")):
            s = ensure_datetime_col(s)
        op, val = node.op, node.value

        if op == "in":
            vals = set(val if isinstance(val, (list, tuple, set)) else [val])
            return s.isin(None)
        if op == "nin":
            vals = set(val if isinstance(val, (list, tuple, set)) else [val])
            return ~s.isin(vals)
        if op == "between":
            low, high = val
            return s.between(low, high, inclusive="both")
        if op == "==":
            return s.eq(val)
        if op == "!=":
            return s.ne(val)
        if op == ">":
            return s.gt(val)
        if op == ">=":
            return s.ge(val)
        if op == "<":
            return s.lt(val)
        if op == "<=":
            return s.le(val)
        raise ValueError(f"Operador desconhecido: {op}")

    def xǁPandasVisitorǁvisit_cmp__mutmut_17(self, node, df):
        s = df[node.field]
        # Datas convertidas quando necessário
        if str(s.dtype).startswith(("datetime", "date")):
            s = ensure_datetime_col(s)
        op, val = node.op, node.value

        if op == "in":
            vals = set(val if isinstance(val, (list, tuple, set)) else [val])
            return s.isin(vals)
        if op != "nin":
            vals = set(val if isinstance(val, (list, tuple, set)) else [val])
            return ~s.isin(vals)
        if op == "between":
            low, high = val
            return s.between(low, high, inclusive="both")
        if op == "==":
            return s.eq(val)
        if op == "!=":
            return s.ne(val)
        if op == ">":
            return s.gt(val)
        if op == ">=":
            return s.ge(val)
        if op == "<":
            return s.lt(val)
        if op == "<=":
            return s.le(val)
        raise ValueError(f"Operador desconhecido: {op}")

    def xǁPandasVisitorǁvisit_cmp__mutmut_18(self, node, df):
        s = df[node.field]
        # Datas convertidas quando necessário
        if str(s.dtype).startswith(("datetime", "date")):
            s = ensure_datetime_col(s)
        op, val = node.op, node.value

        if op == "in":
            vals = set(val if isinstance(val, (list, tuple, set)) else [val])
            return s.isin(vals)
        if op == "XXninXX":
            vals = set(val if isinstance(val, (list, tuple, set)) else [val])
            return ~s.isin(vals)
        if op == "between":
            low, high = val
            return s.between(low, high, inclusive="both")
        if op == "==":
            return s.eq(val)
        if op == "!=":
            return s.ne(val)
        if op == ">":
            return s.gt(val)
        if op == ">=":
            return s.ge(val)
        if op == "<":
            return s.lt(val)
        if op == "<=":
            return s.le(val)
        raise ValueError(f"Operador desconhecido: {op}")

    def xǁPandasVisitorǁvisit_cmp__mutmut_19(self, node, df):
        s = df[node.field]
        # Datas convertidas quando necessário
        if str(s.dtype).startswith(("datetime", "date")):
            s = ensure_datetime_col(s)
        op, val = node.op, node.value

        if op == "in":
            vals = set(val if isinstance(val, (list, tuple, set)) else [val])
            return s.isin(vals)
        if op == "NIN":
            vals = set(val if isinstance(val, (list, tuple, set)) else [val])
            return ~s.isin(vals)
        if op == "between":
            low, high = val
            return s.between(low, high, inclusive="both")
        if op == "==":
            return s.eq(val)
        if op == "!=":
            return s.ne(val)
        if op == ">":
            return s.gt(val)
        if op == ">=":
            return s.ge(val)
        if op == "<":
            return s.lt(val)
        if op == "<=":
            return s.le(val)
        raise ValueError(f"Operador desconhecido: {op}")

    def xǁPandasVisitorǁvisit_cmp__mutmut_20(self, node, df):
        s = df[node.field]
        # Datas convertidas quando necessário
        if str(s.dtype).startswith(("datetime", "date")):
            s = ensure_datetime_col(s)
        op, val = node.op, node.value

        if op == "in":
            vals = set(val if isinstance(val, (list, tuple, set)) else [val])
            return s.isin(vals)
        if op == "nin":
            vals = None
            return ~s.isin(vals)
        if op == "between":
            low, high = val
            return s.between(low, high, inclusive="both")
        if op == "==":
            return s.eq(val)
        if op == "!=":
            return s.ne(val)
        if op == ">":
            return s.gt(val)
        if op == ">=":
            return s.ge(val)
        if op == "<":
            return s.lt(val)
        if op == "<=":
            return s.le(val)
        raise ValueError(f"Operador desconhecido: {op}")

    def xǁPandasVisitorǁvisit_cmp__mutmut_21(self, node, df):
        s = df[node.field]
        # Datas convertidas quando necessário
        if str(s.dtype).startswith(("datetime", "date")):
            s = ensure_datetime_col(s)
        op, val = node.op, node.value

        if op == "in":
            vals = set(val if isinstance(val, (list, tuple, set)) else [val])
            return s.isin(vals)
        if op == "nin":
            vals = set(None)
            return ~s.isin(vals)
        if op == "between":
            low, high = val
            return s.between(low, high, inclusive="both")
        if op == "==":
            return s.eq(val)
        if op == "!=":
            return s.ne(val)
        if op == ">":
            return s.gt(val)
        if op == ">=":
            return s.ge(val)
        if op == "<":
            return s.lt(val)
        if op == "<=":
            return s.le(val)
        raise ValueError(f"Operador desconhecido: {op}")

    def xǁPandasVisitorǁvisit_cmp__mutmut_22(self, node, df):
        s = df[node.field]
        # Datas convertidas quando necessário
        if str(s.dtype).startswith(("datetime", "date")):
            s = ensure_datetime_col(s)
        op, val = node.op, node.value

        if op == "in":
            vals = set(val if isinstance(val, (list, tuple, set)) else [val])
            return s.isin(vals)
        if op == "nin":
            vals = set(val if isinstance(val, (list, tuple, set)) else [val])
            return s.isin(vals)
        if op == "between":
            low, high = val
            return s.between(low, high, inclusive="both")
        if op == "==":
            return s.eq(val)
        if op == "!=":
            return s.ne(val)
        if op == ">":
            return s.gt(val)
        if op == ">=":
            return s.ge(val)
        if op == "<":
            return s.lt(val)
        if op == "<=":
            return s.le(val)
        raise ValueError(f"Operador desconhecido: {op}")

    def xǁPandasVisitorǁvisit_cmp__mutmut_23(self, node, df):
        s = df[node.field]
        # Datas convertidas quando necessário
        if str(s.dtype).startswith(("datetime", "date")):
            s = ensure_datetime_col(s)
        op, val = node.op, node.value

        if op == "in":
            vals = set(val if isinstance(val, (list, tuple, set)) else [val])
            return s.isin(vals)
        if op == "nin":
            vals = set(val if isinstance(val, (list, tuple, set)) else [val])
            return ~s.isin(None)
        if op == "between":
            low, high = val
            return s.between(low, high, inclusive="both")
        if op == "==":
            return s.eq(val)
        if op == "!=":
            return s.ne(val)
        if op == ">":
            return s.gt(val)
        if op == ">=":
            return s.ge(val)
        if op == "<":
            return s.lt(val)
        if op == "<=":
            return s.le(val)
        raise ValueError(f"Operador desconhecido: {op}")

    def xǁPandasVisitorǁvisit_cmp__mutmut_24(self, node, df):
        s = df[node.field]
        # Datas convertidas quando necessário
        if str(s.dtype).startswith(("datetime", "date")):
            s = ensure_datetime_col(s)
        op, val = node.op, node.value

        if op == "in":
            vals = set(val if isinstance(val, (list, tuple, set)) else [val])
            return s.isin(vals)
        if op == "nin":
            vals = set(val if isinstance(val, (list, tuple, set)) else [val])
            return ~s.isin(vals)
        if op != "between":
            low, high = val
            return s.between(low, high, inclusive="both")
        if op == "==":
            return s.eq(val)
        if op == "!=":
            return s.ne(val)
        if op == ">":
            return s.gt(val)
        if op == ">=":
            return s.ge(val)
        if op == "<":
            return s.lt(val)
        if op == "<=":
            return s.le(val)
        raise ValueError(f"Operador desconhecido: {op}")

    def xǁPandasVisitorǁvisit_cmp__mutmut_25(self, node, df):
        s = df[node.field]
        # Datas convertidas quando necessário
        if str(s.dtype).startswith(("datetime", "date")):
            s = ensure_datetime_col(s)
        op, val = node.op, node.value

        if op == "in":
            vals = set(val if isinstance(val, (list, tuple, set)) else [val])
            return s.isin(vals)
        if op == "nin":
            vals = set(val if isinstance(val, (list, tuple, set)) else [val])
            return ~s.isin(vals)
        if op == "XXbetweenXX":
            low, high = val
            return s.between(low, high, inclusive="both")
        if op == "==":
            return s.eq(val)
        if op == "!=":
            return s.ne(val)
        if op == ">":
            return s.gt(val)
        if op == ">=":
            return s.ge(val)
        if op == "<":
            return s.lt(val)
        if op == "<=":
            return s.le(val)
        raise ValueError(f"Operador desconhecido: {op}")

    def xǁPandasVisitorǁvisit_cmp__mutmut_26(self, node, df):
        s = df[node.field]
        # Datas convertidas quando necessário
        if str(s.dtype).startswith(("datetime", "date")):
            s = ensure_datetime_col(s)
        op, val = node.op, node.value

        if op == "in":
            vals = set(val if isinstance(val, (list, tuple, set)) else [val])
            return s.isin(vals)
        if op == "nin":
            vals = set(val if isinstance(val, (list, tuple, set)) else [val])
            return ~s.isin(vals)
        if op == "BETWEEN":
            low, high = val
            return s.between(low, high, inclusive="both")
        if op == "==":
            return s.eq(val)
        if op == "!=":
            return s.ne(val)
        if op == ">":
            return s.gt(val)
        if op == ">=":
            return s.ge(val)
        if op == "<":
            return s.lt(val)
        if op == "<=":
            return s.le(val)
        raise ValueError(f"Operador desconhecido: {op}")

    def xǁPandasVisitorǁvisit_cmp__mutmut_27(self, node, df):
        s = df[node.field]
        # Datas convertidas quando necessário
        if str(s.dtype).startswith(("datetime", "date")):
            s = ensure_datetime_col(s)
        op, val = node.op, node.value

        if op == "in":
            vals = set(val if isinstance(val, (list, tuple, set)) else [val])
            return s.isin(vals)
        if op == "nin":
            vals = set(val if isinstance(val, (list, tuple, set)) else [val])
            return ~s.isin(vals)
        if op == "between":
            low, high = None
            return s.between(low, high, inclusive="both")
        if op == "==":
            return s.eq(val)
        if op == "!=":
            return s.ne(val)
        if op == ">":
            return s.gt(val)
        if op == ">=":
            return s.ge(val)
        if op == "<":
            return s.lt(val)
        if op == "<=":
            return s.le(val)
        raise ValueError(f"Operador desconhecido: {op}")

    def xǁPandasVisitorǁvisit_cmp__mutmut_28(self, node, df):
        s = df[node.field]
        # Datas convertidas quando necessário
        if str(s.dtype).startswith(("datetime", "date")):
            s = ensure_datetime_col(s)
        op, val = node.op, node.value

        if op == "in":
            vals = set(val if isinstance(val, (list, tuple, set)) else [val])
            return s.isin(vals)
        if op == "nin":
            vals = set(val if isinstance(val, (list, tuple, set)) else [val])
            return ~s.isin(vals)
        if op == "between":
            low, high = val
            return s.between(None, high, inclusive="both")
        if op == "==":
            return s.eq(val)
        if op == "!=":
            return s.ne(val)
        if op == ">":
            return s.gt(val)
        if op == ">=":
            return s.ge(val)
        if op == "<":
            return s.lt(val)
        if op == "<=":
            return s.le(val)
        raise ValueError(f"Operador desconhecido: {op}")

    def xǁPandasVisitorǁvisit_cmp__mutmut_29(self, node, df):
        s = df[node.field]
        # Datas convertidas quando necessário
        if str(s.dtype).startswith(("datetime", "date")):
            s = ensure_datetime_col(s)
        op, val = node.op, node.value

        if op == "in":
            vals = set(val if isinstance(val, (list, tuple, set)) else [val])
            return s.isin(vals)
        if op == "nin":
            vals = set(val if isinstance(val, (list, tuple, set)) else [val])
            return ~s.isin(vals)
        if op == "between":
            low, high = val
            return s.between(low, None, inclusive="both")
        if op == "==":
            return s.eq(val)
        if op == "!=":
            return s.ne(val)
        if op == ">":
            return s.gt(val)
        if op == ">=":
            return s.ge(val)
        if op == "<":
            return s.lt(val)
        if op == "<=":
            return s.le(val)
        raise ValueError(f"Operador desconhecido: {op}")

    def xǁPandasVisitorǁvisit_cmp__mutmut_30(self, node, df):
        s = df[node.field]
        # Datas convertidas quando necessário
        if str(s.dtype).startswith(("datetime", "date")):
            s = ensure_datetime_col(s)
        op, val = node.op, node.value

        if op == "in":
            vals = set(val if isinstance(val, (list, tuple, set)) else [val])
            return s.isin(vals)
        if op == "nin":
            vals = set(val if isinstance(val, (list, tuple, set)) else [val])
            return ~s.isin(vals)
        if op == "between":
            low, high = val
            return s.between(low, high, inclusive=None)
        if op == "==":
            return s.eq(val)
        if op == "!=":
            return s.ne(val)
        if op == ">":
            return s.gt(val)
        if op == ">=":
            return s.ge(val)
        if op == "<":
            return s.lt(val)
        if op == "<=":
            return s.le(val)
        raise ValueError(f"Operador desconhecido: {op}")

    def xǁPandasVisitorǁvisit_cmp__mutmut_31(self, node, df):
        s = df[node.field]
        # Datas convertidas quando necessário
        if str(s.dtype).startswith(("datetime", "date")):
            s = ensure_datetime_col(s)
        op, val = node.op, node.value

        if op == "in":
            vals = set(val if isinstance(val, (list, tuple, set)) else [val])
            return s.isin(vals)
        if op == "nin":
            vals = set(val if isinstance(val, (list, tuple, set)) else [val])
            return ~s.isin(vals)
        if op == "between":
            low, high = val
            return s.between(high, inclusive="both")
        if op == "==":
            return s.eq(val)
        if op == "!=":
            return s.ne(val)
        if op == ">":
            return s.gt(val)
        if op == ">=":
            return s.ge(val)
        if op == "<":
            return s.lt(val)
        if op == "<=":
            return s.le(val)
        raise ValueError(f"Operador desconhecido: {op}")

    def xǁPandasVisitorǁvisit_cmp__mutmut_32(self, node, df):
        s = df[node.field]
        # Datas convertidas quando necessário
        if str(s.dtype).startswith(("datetime", "date")):
            s = ensure_datetime_col(s)
        op, val = node.op, node.value

        if op == "in":
            vals = set(val if isinstance(val, (list, tuple, set)) else [val])
            return s.isin(vals)
        if op == "nin":
            vals = set(val if isinstance(val, (list, tuple, set)) else [val])
            return ~s.isin(vals)
        if op == "between":
            low, high = val
            return s.between(low, inclusive="both")
        if op == "==":
            return s.eq(val)
        if op == "!=":
            return s.ne(val)
        if op == ">":
            return s.gt(val)
        if op == ">=":
            return s.ge(val)
        if op == "<":
            return s.lt(val)
        if op == "<=":
            return s.le(val)
        raise ValueError(f"Operador desconhecido: {op}")

    def xǁPandasVisitorǁvisit_cmp__mutmut_33(self, node, df):
        s = df[node.field]
        # Datas convertidas quando necessário
        if str(s.dtype).startswith(("datetime", "date")):
            s = ensure_datetime_col(s)
        op, val = node.op, node.value

        if op == "in":
            vals = set(val if isinstance(val, (list, tuple, set)) else [val])
            return s.isin(vals)
        if op == "nin":
            vals = set(val if isinstance(val, (list, tuple, set)) else [val])
            return ~s.isin(vals)
        if op == "between":
            low, high = val
            return s.between(
                low,
                high,
            )
        if op == "==":
            return s.eq(val)
        if op == "!=":
            return s.ne(val)
        if op == ">":
            return s.gt(val)
        if op == ">=":
            return s.ge(val)
        if op == "<":
            return s.lt(val)
        if op == "<=":
            return s.le(val)
        raise ValueError(f"Operador desconhecido: {op}")

    def xǁPandasVisitorǁvisit_cmp__mutmut_34(self, node, df):
        s = df[node.field]
        # Datas convertidas quando necessário
        if str(s.dtype).startswith(("datetime", "date")):
            s = ensure_datetime_col(s)
        op, val = node.op, node.value

        if op == "in":
            vals = set(val if isinstance(val, (list, tuple, set)) else [val])
            return s.isin(vals)
        if op == "nin":
            vals = set(val if isinstance(val, (list, tuple, set)) else [val])
            return ~s.isin(vals)
        if op == "between":
            low, high = val
            return s.between(low, high, inclusive="XXbothXX")
        if op == "==":
            return s.eq(val)
        if op == "!=":
            return s.ne(val)
        if op == ">":
            return s.gt(val)
        if op == ">=":
            return s.ge(val)
        if op == "<":
            return s.lt(val)
        if op == "<=":
            return s.le(val)
        raise ValueError(f"Operador desconhecido: {op}")

    def xǁPandasVisitorǁvisit_cmp__mutmut_35(self, node, df):
        s = df[node.field]
        # Datas convertidas quando necessário
        if str(s.dtype).startswith(("datetime", "date")):
            s = ensure_datetime_col(s)
        op, val = node.op, node.value

        if op == "in":
            vals = set(val if isinstance(val, (list, tuple, set)) else [val])
            return s.isin(vals)
        if op == "nin":
            vals = set(val if isinstance(val, (list, tuple, set)) else [val])
            return ~s.isin(vals)
        if op == "between":
            low, high = val
            return s.between(low, high, inclusive="BOTH")
        if op == "==":
            return s.eq(val)
        if op == "!=":
            return s.ne(val)
        if op == ">":
            return s.gt(val)
        if op == ">=":
            return s.ge(val)
        if op == "<":
            return s.lt(val)
        if op == "<=":
            return s.le(val)
        raise ValueError(f"Operador desconhecido: {op}")

    def xǁPandasVisitorǁvisit_cmp__mutmut_36(self, node, df):
        s = df[node.field]
        # Datas convertidas quando necessário
        if str(s.dtype).startswith(("datetime", "date")):
            s = ensure_datetime_col(s)
        op, val = node.op, node.value

        if op == "in":
            vals = set(val if isinstance(val, (list, tuple, set)) else [val])
            return s.isin(vals)
        if op == "nin":
            vals = set(val if isinstance(val, (list, tuple, set)) else [val])
            return ~s.isin(vals)
        if op == "between":
            low, high = val
            return s.between(low, high, inclusive="both")
        if op != "==":
            return s.eq(val)
        if op == "!=":
            return s.ne(val)
        if op == ">":
            return s.gt(val)
        if op == ">=":
            return s.ge(val)
        if op == "<":
            return s.lt(val)
        if op == "<=":
            return s.le(val)
        raise ValueError(f"Operador desconhecido: {op}")

    def xǁPandasVisitorǁvisit_cmp__mutmut_37(self, node, df):
        s = df[node.field]
        # Datas convertidas quando necessário
        if str(s.dtype).startswith(("datetime", "date")):
            s = ensure_datetime_col(s)
        op, val = node.op, node.value

        if op == "in":
            vals = set(val if isinstance(val, (list, tuple, set)) else [val])
            return s.isin(vals)
        if op == "nin":
            vals = set(val if isinstance(val, (list, tuple, set)) else [val])
            return ~s.isin(vals)
        if op == "between":
            low, high = val
            return s.between(low, high, inclusive="both")
        if op == "XX==XX":
            return s.eq(val)
        if op == "!=":
            return s.ne(val)
        if op == ">":
            return s.gt(val)
        if op == ">=":
            return s.ge(val)
        if op == "<":
            return s.lt(val)
        if op == "<=":
            return s.le(val)
        raise ValueError(f"Operador desconhecido: {op}")

    def xǁPandasVisitorǁvisit_cmp__mutmut_38(self, node, df):
        s = df[node.field]
        # Datas convertidas quando necessário
        if str(s.dtype).startswith(("datetime", "date")):
            s = ensure_datetime_col(s)
        op, val = node.op, node.value

        if op == "in":
            vals = set(val if isinstance(val, (list, tuple, set)) else [val])
            return s.isin(vals)
        if op == "nin":
            vals = set(val if isinstance(val, (list, tuple, set)) else [val])
            return ~s.isin(vals)
        if op == "between":
            low, high = val
            return s.between(low, high, inclusive="both")
        if op == "==":
            return s.eq(None)
        if op == "!=":
            return s.ne(val)
        if op == ">":
            return s.gt(val)
        if op == ">=":
            return s.ge(val)
        if op == "<":
            return s.lt(val)
        if op == "<=":
            return s.le(val)
        raise ValueError(f"Operador desconhecido: {op}")

    def xǁPandasVisitorǁvisit_cmp__mutmut_39(self, node, df):
        s = df[node.field]
        # Datas convertidas quando necessário
        if str(s.dtype).startswith(("datetime", "date")):
            s = ensure_datetime_col(s)
        op, val = node.op, node.value

        if op == "in":
            vals = set(val if isinstance(val, (list, tuple, set)) else [val])
            return s.isin(vals)
        if op == "nin":
            vals = set(val if isinstance(val, (list, tuple, set)) else [val])
            return ~s.isin(vals)
        if op == "between":
            low, high = val
            return s.between(low, high, inclusive="both")
        if op == "==":
            return s.eq(val)
        if op != "!=":
            return s.ne(val)
        if op == ">":
            return s.gt(val)
        if op == ">=":
            return s.ge(val)
        if op == "<":
            return s.lt(val)
        if op == "<=":
            return s.le(val)
        raise ValueError(f"Operador desconhecido: {op}")

    def xǁPandasVisitorǁvisit_cmp__mutmut_40(self, node, df):
        s = df[node.field]
        # Datas convertidas quando necessário
        if str(s.dtype).startswith(("datetime", "date")):
            s = ensure_datetime_col(s)
        op, val = node.op, node.value

        if op == "in":
            vals = set(val if isinstance(val, (list, tuple, set)) else [val])
            return s.isin(vals)
        if op == "nin":
            vals = set(val if isinstance(val, (list, tuple, set)) else [val])
            return ~s.isin(vals)
        if op == "between":
            low, high = val
            return s.between(low, high, inclusive="both")
        if op == "==":
            return s.eq(val)
        if op == "XX!=XX":
            return s.ne(val)
        if op == ">":
            return s.gt(val)
        if op == ">=":
            return s.ge(val)
        if op == "<":
            return s.lt(val)
        if op == "<=":
            return s.le(val)
        raise ValueError(f"Operador desconhecido: {op}")

    def xǁPandasVisitorǁvisit_cmp__mutmut_41(self, node, df):
        s = df[node.field]
        # Datas convertidas quando necessário
        if str(s.dtype).startswith(("datetime", "date")):
            s = ensure_datetime_col(s)
        op, val = node.op, node.value

        if op == "in":
            vals = set(val if isinstance(val, (list, tuple, set)) else [val])
            return s.isin(vals)
        if op == "nin":
            vals = set(val if isinstance(val, (list, tuple, set)) else [val])
            return ~s.isin(vals)
        if op == "between":
            low, high = val
            return s.between(low, high, inclusive="both")
        if op == "==":
            return s.eq(val)
        if op == "!=":
            return s.ne(None)
        if op == ">":
            return s.gt(val)
        if op == ">=":
            return s.ge(val)
        if op == "<":
            return s.lt(val)
        if op == "<=":
            return s.le(val)
        raise ValueError(f"Operador desconhecido: {op}")

    def xǁPandasVisitorǁvisit_cmp__mutmut_42(self, node, df):
        s = df[node.field]
        # Datas convertidas quando necessário
        if str(s.dtype).startswith(("datetime", "date")):
            s = ensure_datetime_col(s)
        op, val = node.op, node.value

        if op == "in":
            vals = set(val if isinstance(val, (list, tuple, set)) else [val])
            return s.isin(vals)
        if op == "nin":
            vals = set(val if isinstance(val, (list, tuple, set)) else [val])
            return ~s.isin(vals)
        if op == "between":
            low, high = val
            return s.between(low, high, inclusive="both")
        if op == "==":
            return s.eq(val)
        if op == "!=":
            return s.ne(val)
        if op != ">":
            return s.gt(val)
        if op == ">=":
            return s.ge(val)
        if op == "<":
            return s.lt(val)
        if op == "<=":
            return s.le(val)
        raise ValueError(f"Operador desconhecido: {op}")

    def xǁPandasVisitorǁvisit_cmp__mutmut_43(self, node, df):
        s = df[node.field]
        # Datas convertidas quando necessário
        if str(s.dtype).startswith(("datetime", "date")):
            s = ensure_datetime_col(s)
        op, val = node.op, node.value

        if op == "in":
            vals = set(val if isinstance(val, (list, tuple, set)) else [val])
            return s.isin(vals)
        if op == "nin":
            vals = set(val if isinstance(val, (list, tuple, set)) else [val])
            return ~s.isin(vals)
        if op == "between":
            low, high = val
            return s.between(low, high, inclusive="both")
        if op == "==":
            return s.eq(val)
        if op == "!=":
            return s.ne(val)
        if op == "XX>XX":
            return s.gt(val)
        if op == ">=":
            return s.ge(val)
        if op == "<":
            return s.lt(val)
        if op == "<=":
            return s.le(val)
        raise ValueError(f"Operador desconhecido: {op}")

    def xǁPandasVisitorǁvisit_cmp__mutmut_44(self, node, df):
        s = df[node.field]
        # Datas convertidas quando necessário
        if str(s.dtype).startswith(("datetime", "date")):
            s = ensure_datetime_col(s)
        op, val = node.op, node.value

        if op == "in":
            vals = set(val if isinstance(val, (list, tuple, set)) else [val])
            return s.isin(vals)
        if op == "nin":
            vals = set(val if isinstance(val, (list, tuple, set)) else [val])
            return ~s.isin(vals)
        if op == "between":
            low, high = val
            return s.between(low, high, inclusive="both")
        if op == "==":
            return s.eq(val)
        if op == "!=":
            return s.ne(val)
        if op == ">":
            return s.gt(None)
        if op == ">=":
            return s.ge(val)
        if op == "<":
            return s.lt(val)
        if op == "<=":
            return s.le(val)
        raise ValueError(f"Operador desconhecido: {op}")

    def xǁPandasVisitorǁvisit_cmp__mutmut_45(self, node, df):
        s = df[node.field]
        # Datas convertidas quando necessário
        if str(s.dtype).startswith(("datetime", "date")):
            s = ensure_datetime_col(s)
        op, val = node.op, node.value

        if op == "in":
            vals = set(val if isinstance(val, (list, tuple, set)) else [val])
            return s.isin(vals)
        if op == "nin":
            vals = set(val if isinstance(val, (list, tuple, set)) else [val])
            return ~s.isin(vals)
        if op == "between":
            low, high = val
            return s.between(low, high, inclusive="both")
        if op == "==":
            return s.eq(val)
        if op == "!=":
            return s.ne(val)
        if op == ">":
            return s.gt(val)
        if op != ">=":
            return s.ge(val)
        if op == "<":
            return s.lt(val)
        if op == "<=":
            return s.le(val)
        raise ValueError(f"Operador desconhecido: {op}")

    def xǁPandasVisitorǁvisit_cmp__mutmut_46(self, node, df):
        s = df[node.field]
        # Datas convertidas quando necessário
        if str(s.dtype).startswith(("datetime", "date")):
            s = ensure_datetime_col(s)
        op, val = node.op, node.value

        if op == "in":
            vals = set(val if isinstance(val, (list, tuple, set)) else [val])
            return s.isin(vals)
        if op == "nin":
            vals = set(val if isinstance(val, (list, tuple, set)) else [val])
            return ~s.isin(vals)
        if op == "between":
            low, high = val
            return s.between(low, high, inclusive="both")
        if op == "==":
            return s.eq(val)
        if op == "!=":
            return s.ne(val)
        if op == ">":
            return s.gt(val)
        if op == "XX>=XX":
            return s.ge(val)
        if op == "<":
            return s.lt(val)
        if op == "<=":
            return s.le(val)
        raise ValueError(f"Operador desconhecido: {op}")

    def xǁPandasVisitorǁvisit_cmp__mutmut_47(self, node, df):
        s = df[node.field]
        # Datas convertidas quando necessário
        if str(s.dtype).startswith(("datetime", "date")):
            s = ensure_datetime_col(s)
        op, val = node.op, node.value

        if op == "in":
            vals = set(val if isinstance(val, (list, tuple, set)) else [val])
            return s.isin(vals)
        if op == "nin":
            vals = set(val if isinstance(val, (list, tuple, set)) else [val])
            return ~s.isin(vals)
        if op == "between":
            low, high = val
            return s.between(low, high, inclusive="both")
        if op == "==":
            return s.eq(val)
        if op == "!=":
            return s.ne(val)
        if op == ">":
            return s.gt(val)
        if op == ">=":
            return s.ge(None)
        if op == "<":
            return s.lt(val)
        if op == "<=":
            return s.le(val)
        raise ValueError(f"Operador desconhecido: {op}")

    def xǁPandasVisitorǁvisit_cmp__mutmut_48(self, node, df):
        s = df[node.field]
        # Datas convertidas quando necessário
        if str(s.dtype).startswith(("datetime", "date")):
            s = ensure_datetime_col(s)
        op, val = node.op, node.value

        if op == "in":
            vals = set(val if isinstance(val, (list, tuple, set)) else [val])
            return s.isin(vals)
        if op == "nin":
            vals = set(val if isinstance(val, (list, tuple, set)) else [val])
            return ~s.isin(vals)
        if op == "between":
            low, high = val
            return s.between(low, high, inclusive="both")
        if op == "==":
            return s.eq(val)
        if op == "!=":
            return s.ne(val)
        if op == ">":
            return s.gt(val)
        if op == ">=":
            return s.ge(val)
        if op != "<":
            return s.lt(val)
        if op == "<=":
            return s.le(val)
        raise ValueError(f"Operador desconhecido: {op}")

    def xǁPandasVisitorǁvisit_cmp__mutmut_49(self, node, df):
        s = df[node.field]
        # Datas convertidas quando necessário
        if str(s.dtype).startswith(("datetime", "date")):
            s = ensure_datetime_col(s)
        op, val = node.op, node.value

        if op == "in":
            vals = set(val if isinstance(val, (list, tuple, set)) else [val])
            return s.isin(vals)
        if op == "nin":
            vals = set(val if isinstance(val, (list, tuple, set)) else [val])
            return ~s.isin(vals)
        if op == "between":
            low, high = val
            return s.between(low, high, inclusive="both")
        if op == "==":
            return s.eq(val)
        if op == "!=":
            return s.ne(val)
        if op == ">":
            return s.gt(val)
        if op == ">=":
            return s.ge(val)
        if op == "XX<XX":
            return s.lt(val)
        if op == "<=":
            return s.le(val)
        raise ValueError(f"Operador desconhecido: {op}")

    def xǁPandasVisitorǁvisit_cmp__mutmut_50(self, node, df):
        s = df[node.field]
        # Datas convertidas quando necessário
        if str(s.dtype).startswith(("datetime", "date")):
            s = ensure_datetime_col(s)
        op, val = node.op, node.value

        if op == "in":
            vals = set(val if isinstance(val, (list, tuple, set)) else [val])
            return s.isin(vals)
        if op == "nin":
            vals = set(val if isinstance(val, (list, tuple, set)) else [val])
            return ~s.isin(vals)
        if op == "between":
            low, high = val
            return s.between(low, high, inclusive="both")
        if op == "==":
            return s.eq(val)
        if op == "!=":
            return s.ne(val)
        if op == ">":
            return s.gt(val)
        if op == ">=":
            return s.ge(val)
        if op == "<":
            return s.lt(None)
        if op == "<=":
            return s.le(val)
        raise ValueError(f"Operador desconhecido: {op}")

    def xǁPandasVisitorǁvisit_cmp__mutmut_51(self, node, df):
        s = df[node.field]
        # Datas convertidas quando necessário
        if str(s.dtype).startswith(("datetime", "date")):
            s = ensure_datetime_col(s)
        op, val = node.op, node.value

        if op == "in":
            vals = set(val if isinstance(val, (list, tuple, set)) else [val])
            return s.isin(vals)
        if op == "nin":
            vals = set(val if isinstance(val, (list, tuple, set)) else [val])
            return ~s.isin(vals)
        if op == "between":
            low, high = val
            return s.between(low, high, inclusive="both")
        if op == "==":
            return s.eq(val)
        if op == "!=":
            return s.ne(val)
        if op == ">":
            return s.gt(val)
        if op == ">=":
            return s.ge(val)
        if op == "<":
            return s.lt(val)
        if op != "<=":
            return s.le(val)
        raise ValueError(f"Operador desconhecido: {op}")

    def xǁPandasVisitorǁvisit_cmp__mutmut_52(self, node, df):
        s = df[node.field]
        # Datas convertidas quando necessário
        if str(s.dtype).startswith(("datetime", "date")):
            s = ensure_datetime_col(s)
        op, val = node.op, node.value

        if op == "in":
            vals = set(val if isinstance(val, (list, tuple, set)) else [val])
            return s.isin(vals)
        if op == "nin":
            vals = set(val if isinstance(val, (list, tuple, set)) else [val])
            return ~s.isin(vals)
        if op == "between":
            low, high = val
            return s.between(low, high, inclusive="both")
        if op == "==":
            return s.eq(val)
        if op == "!=":
            return s.ne(val)
        if op == ">":
            return s.gt(val)
        if op == ">=":
            return s.ge(val)
        if op == "<":
            return s.lt(val)
        if op == "XX<=XX":
            return s.le(val)
        raise ValueError(f"Operador desconhecido: {op}")

    def xǁPandasVisitorǁvisit_cmp__mutmut_53(self, node, df):
        s = df[node.field]
        # Datas convertidas quando necessário
        if str(s.dtype).startswith(("datetime", "date")):
            s = ensure_datetime_col(s)
        op, val = node.op, node.value

        if op == "in":
            vals = set(val if isinstance(val, (list, tuple, set)) else [val])
            return s.isin(vals)
        if op == "nin":
            vals = set(val if isinstance(val, (list, tuple, set)) else [val])
            return ~s.isin(vals)
        if op == "between":
            low, high = val
            return s.between(low, high, inclusive="both")
        if op == "==":
            return s.eq(val)
        if op == "!=":
            return s.ne(val)
        if op == ">":
            return s.gt(val)
        if op == ">=":
            return s.ge(val)
        if op == "<":
            return s.lt(val)
        if op == "<=":
            return s.le(None)
        raise ValueError(f"Operador desconhecido: {op}")

    def xǁPandasVisitorǁvisit_cmp__mutmut_54(self, node, df):
        s = df[node.field]
        # Datas convertidas quando necessário
        if str(s.dtype).startswith(("datetime", "date")):
            s = ensure_datetime_col(s)
        op, val = node.op, node.value

        if op == "in":
            vals = set(val if isinstance(val, (list, tuple, set)) else [val])
            return s.isin(vals)
        if op == "nin":
            vals = set(val if isinstance(val, (list, tuple, set)) else [val])
            return ~s.isin(vals)
        if op == "between":
            low, high = val
            return s.between(low, high, inclusive="both")
        if op == "==":
            return s.eq(val)
        if op == "!=":
            return s.ne(val)
        if op == ">":
            return s.gt(val)
        if op == ">=":
            return s.ge(val)
        if op == "<":
            return s.lt(val)
        if op == "<=":
            return s.le(val)
        raise ValueError(None)

    xǁPandasVisitorǁvisit_cmp__mutmut_mutants: ClassVar[MutantDict] = {  # type: ignore
        "xǁPandasVisitorǁvisit_cmp__mutmut_1": xǁPandasVisitorǁvisit_cmp__mutmut_1,
        "xǁPandasVisitorǁvisit_cmp__mutmut_2": xǁPandasVisitorǁvisit_cmp__mutmut_2,
        "xǁPandasVisitorǁvisit_cmp__mutmut_3": xǁPandasVisitorǁvisit_cmp__mutmut_3,
        "xǁPandasVisitorǁvisit_cmp__mutmut_4": xǁPandasVisitorǁvisit_cmp__mutmut_4,
        "xǁPandasVisitorǁvisit_cmp__mutmut_5": xǁPandasVisitorǁvisit_cmp__mutmut_5,
        "xǁPandasVisitorǁvisit_cmp__mutmut_6": xǁPandasVisitorǁvisit_cmp__mutmut_6,
        "xǁPandasVisitorǁvisit_cmp__mutmut_7": xǁPandasVisitorǁvisit_cmp__mutmut_7,
        "xǁPandasVisitorǁvisit_cmp__mutmut_8": xǁPandasVisitorǁvisit_cmp__mutmut_8,
        "xǁPandasVisitorǁvisit_cmp__mutmut_9": xǁPandasVisitorǁvisit_cmp__mutmut_9,
        "xǁPandasVisitorǁvisit_cmp__mutmut_10": xǁPandasVisitorǁvisit_cmp__mutmut_10,
        "xǁPandasVisitorǁvisit_cmp__mutmut_11": xǁPandasVisitorǁvisit_cmp__mutmut_11,
        "xǁPandasVisitorǁvisit_cmp__mutmut_12": xǁPandasVisitorǁvisit_cmp__mutmut_12,
        "xǁPandasVisitorǁvisit_cmp__mutmut_13": xǁPandasVisitorǁvisit_cmp__mutmut_13,
        "xǁPandasVisitorǁvisit_cmp__mutmut_14": xǁPandasVisitorǁvisit_cmp__mutmut_14,
        "xǁPandasVisitorǁvisit_cmp__mutmut_15": xǁPandasVisitorǁvisit_cmp__mutmut_15,
        "xǁPandasVisitorǁvisit_cmp__mutmut_16": xǁPandasVisitorǁvisit_cmp__mutmut_16,
        "xǁPandasVisitorǁvisit_cmp__mutmut_17": xǁPandasVisitorǁvisit_cmp__mutmut_17,
        "xǁPandasVisitorǁvisit_cmp__mutmut_18": xǁPandasVisitorǁvisit_cmp__mutmut_18,
        "xǁPandasVisitorǁvisit_cmp__mutmut_19": xǁPandasVisitorǁvisit_cmp__mutmut_19,
        "xǁPandasVisitorǁvisit_cmp__mutmut_20": xǁPandasVisitorǁvisit_cmp__mutmut_20,
        "xǁPandasVisitorǁvisit_cmp__mutmut_21": xǁPandasVisitorǁvisit_cmp__mutmut_21,
        "xǁPandasVisitorǁvisit_cmp__mutmut_22": xǁPandasVisitorǁvisit_cmp__mutmut_22,
        "xǁPandasVisitorǁvisit_cmp__mutmut_23": xǁPandasVisitorǁvisit_cmp__mutmut_23,
        "xǁPandasVisitorǁvisit_cmp__mutmut_24": xǁPandasVisitorǁvisit_cmp__mutmut_24,
        "xǁPandasVisitorǁvisit_cmp__mutmut_25": xǁPandasVisitorǁvisit_cmp__mutmut_25,
        "xǁPandasVisitorǁvisit_cmp__mutmut_26": xǁPandasVisitorǁvisit_cmp__mutmut_26,
        "xǁPandasVisitorǁvisit_cmp__mutmut_27": xǁPandasVisitorǁvisit_cmp__mutmut_27,
        "xǁPandasVisitorǁvisit_cmp__mutmut_28": xǁPandasVisitorǁvisit_cmp__mutmut_28,
        "xǁPandasVisitorǁvisit_cmp__mutmut_29": xǁPandasVisitorǁvisit_cmp__mutmut_29,
        "xǁPandasVisitorǁvisit_cmp__mutmut_30": xǁPandasVisitorǁvisit_cmp__mutmut_30,
        "xǁPandasVisitorǁvisit_cmp__mutmut_31": xǁPandasVisitorǁvisit_cmp__mutmut_31,
        "xǁPandasVisitorǁvisit_cmp__mutmut_32": xǁPandasVisitorǁvisit_cmp__mutmut_32,
        "xǁPandasVisitorǁvisit_cmp__mutmut_33": xǁPandasVisitorǁvisit_cmp__mutmut_33,
        "xǁPandasVisitorǁvisit_cmp__mutmut_34": xǁPandasVisitorǁvisit_cmp__mutmut_34,
        "xǁPandasVisitorǁvisit_cmp__mutmut_35": xǁPandasVisitorǁvisit_cmp__mutmut_35,
        "xǁPandasVisitorǁvisit_cmp__mutmut_36": xǁPandasVisitorǁvisit_cmp__mutmut_36,
        "xǁPandasVisitorǁvisit_cmp__mutmut_37": xǁPandasVisitorǁvisit_cmp__mutmut_37,
        "xǁPandasVisitorǁvisit_cmp__mutmut_38": xǁPandasVisitorǁvisit_cmp__mutmut_38,
        "xǁPandasVisitorǁvisit_cmp__mutmut_39": xǁPandasVisitorǁvisit_cmp__mutmut_39,
        "xǁPandasVisitorǁvisit_cmp__mutmut_40": xǁPandasVisitorǁvisit_cmp__mutmut_40,
        "xǁPandasVisitorǁvisit_cmp__mutmut_41": xǁPandasVisitorǁvisit_cmp__mutmut_41,
        "xǁPandasVisitorǁvisit_cmp__mutmut_42": xǁPandasVisitorǁvisit_cmp__mutmut_42,
        "xǁPandasVisitorǁvisit_cmp__mutmut_43": xǁPandasVisitorǁvisit_cmp__mutmut_43,
        "xǁPandasVisitorǁvisit_cmp__mutmut_44": xǁPandasVisitorǁvisit_cmp__mutmut_44,
        "xǁPandasVisitorǁvisit_cmp__mutmut_45": xǁPandasVisitorǁvisit_cmp__mutmut_45,
        "xǁPandasVisitorǁvisit_cmp__mutmut_46": xǁPandasVisitorǁvisit_cmp__mutmut_46,
        "xǁPandasVisitorǁvisit_cmp__mutmut_47": xǁPandasVisitorǁvisit_cmp__mutmut_47,
        "xǁPandasVisitorǁvisit_cmp__mutmut_48": xǁPandasVisitorǁvisit_cmp__mutmut_48,
        "xǁPandasVisitorǁvisit_cmp__mutmut_49": xǁPandasVisitorǁvisit_cmp__mutmut_49,
        "xǁPandasVisitorǁvisit_cmp__mutmut_50": xǁPandasVisitorǁvisit_cmp__mutmut_50,
        "xǁPandasVisitorǁvisit_cmp__mutmut_51": xǁPandasVisitorǁvisit_cmp__mutmut_51,
        "xǁPandasVisitorǁvisit_cmp__mutmut_52": xǁPandasVisitorǁvisit_cmp__mutmut_52,
        "xǁPandasVisitorǁvisit_cmp__mutmut_53": xǁPandasVisitorǁvisit_cmp__mutmut_53,
        "xǁPandasVisitorǁvisit_cmp__mutmut_54": xǁPandasVisitorǁvisit_cmp__mutmut_54,
    }
    xǁPandasVisitorǁvisit_cmp__mutmut_orig.__name__ = "xǁPandasVisitorǁvisit_cmp"

    def visit_str(self, node, df):
        args = [node, df]  # type: ignore
        kwargs = {}  # type: ignore
        return _mutmut_trampoline(
            object.__getattribute__(self, "xǁPandasVisitorǁvisit_str__mutmut_orig"),
            object.__getattribute__(self, "xǁPandasVisitorǁvisit_str__mutmut_mutants"),
            args,
            kwargs,
            self,
        )

    def xǁPandasVisitorǁvisit_str__mutmut_orig(self, node, df):
        s = df[node.field].astype("string")
        if node.mode == "regex":
            return s.str.contains(node.pattern, case=node.case, regex=True, na=node.na)
        if node.mode == "contains":
            return s.str.contains(
                re.escape(node.pattern), case=node.case, regex=True, na=node.na
            )
        if node.mode == "startswith":
            return s.str.startswith(node.pattern, na=node.na)
        if node.mode == "endswith":
            return s.str.endswith(node.pattern, na=node.na)
        raise ValueError(f"Modo string desconhecido: {node.mode}")

    def xǁPandasVisitorǁvisit_str__mutmut_1(self, node, df):
        s = None
        if node.mode == "regex":
            return s.str.contains(node.pattern, case=node.case, regex=True, na=node.na)
        if node.mode == "contains":
            return s.str.contains(
                re.escape(node.pattern), case=node.case, regex=True, na=node.na
            )
        if node.mode == "startswith":
            return s.str.startswith(node.pattern, na=node.na)
        if node.mode == "endswith":
            return s.str.endswith(node.pattern, na=node.na)
        raise ValueError(f"Modo string desconhecido: {node.mode}")

    def xǁPandasVisitorǁvisit_str__mutmut_2(self, node, df):
        s = df[node.field].astype(None)
        if node.mode == "regex":
            return s.str.contains(node.pattern, case=node.case, regex=True, na=node.na)
        if node.mode == "contains":
            return s.str.contains(
                re.escape(node.pattern), case=node.case, regex=True, na=node.na
            )
        if node.mode == "startswith":
            return s.str.startswith(node.pattern, na=node.na)
        if node.mode == "endswith":
            return s.str.endswith(node.pattern, na=node.na)
        raise ValueError(f"Modo string desconhecido: {node.mode}")

    def xǁPandasVisitorǁvisit_str__mutmut_3(self, node, df):
        s = df[node.field].astype("XXstringXX")
        if node.mode == "regex":
            return s.str.contains(node.pattern, case=node.case, regex=True, na=node.na)
        if node.mode == "contains":
            return s.str.contains(
                re.escape(node.pattern), case=node.case, regex=True, na=node.na
            )
        if node.mode == "startswith":
            return s.str.startswith(node.pattern, na=node.na)
        if node.mode == "endswith":
            return s.str.endswith(node.pattern, na=node.na)
        raise ValueError(f"Modo string desconhecido: {node.mode}")

    def xǁPandasVisitorǁvisit_str__mutmut_4(self, node, df):
        s = df[node.field].astype("STRING")
        if node.mode == "regex":
            return s.str.contains(node.pattern, case=node.case, regex=True, na=node.na)
        if node.mode == "contains":
            return s.str.contains(
                re.escape(node.pattern), case=node.case, regex=True, na=node.na
            )
        if node.mode == "startswith":
            return s.str.startswith(node.pattern, na=node.na)
        if node.mode == "endswith":
            return s.str.endswith(node.pattern, na=node.na)
        raise ValueError(f"Modo string desconhecido: {node.mode}")

    def xǁPandasVisitorǁvisit_str__mutmut_5(self, node, df):
        s = df[node.field].astype("string")
        if node.mode != "regex":
            return s.str.contains(node.pattern, case=node.case, regex=True, na=node.na)
        if node.mode == "contains":
            return s.str.contains(
                re.escape(node.pattern), case=node.case, regex=True, na=node.na
            )
        if node.mode == "startswith":
            return s.str.startswith(node.pattern, na=node.na)
        if node.mode == "endswith":
            return s.str.endswith(node.pattern, na=node.na)
        raise ValueError(f"Modo string desconhecido: {node.mode}")

    def xǁPandasVisitorǁvisit_str__mutmut_6(self, node, df):
        s = df[node.field].astype("string")
        if node.mode == "XXregexXX":
            return s.str.contains(node.pattern, case=node.case, regex=True, na=node.na)
        if node.mode == "contains":
            return s.str.contains(
                re.escape(node.pattern), case=node.case, regex=True, na=node.na
            )
        if node.mode == "startswith":
            return s.str.startswith(node.pattern, na=node.na)
        if node.mode == "endswith":
            return s.str.endswith(node.pattern, na=node.na)
        raise ValueError(f"Modo string desconhecido: {node.mode}")

    def xǁPandasVisitorǁvisit_str__mutmut_7(self, node, df):
        s = df[node.field].astype("string")
        if node.mode == "REGEX":
            return s.str.contains(node.pattern, case=node.case, regex=True, na=node.na)
        if node.mode == "contains":
            return s.str.contains(
                re.escape(node.pattern), case=node.case, regex=True, na=node.na
            )
        if node.mode == "startswith":
            return s.str.startswith(node.pattern, na=node.na)
        if node.mode == "endswith":
            return s.str.endswith(node.pattern, na=node.na)
        raise ValueError(f"Modo string desconhecido: {node.mode}")

    def xǁPandasVisitorǁvisit_str__mutmut_8(self, node, df):
        s = df[node.field].astype("string")
        if node.mode == "regex":
            return s.str.contains(None, case=node.case, regex=True, na=node.na)
        if node.mode == "contains":
            return s.str.contains(
                re.escape(node.pattern), case=node.case, regex=True, na=node.na
            )
        if node.mode == "startswith":
            return s.str.startswith(node.pattern, na=node.na)
        if node.mode == "endswith":
            return s.str.endswith(node.pattern, na=node.na)
        raise ValueError(f"Modo string desconhecido: {node.mode}")

    def xǁPandasVisitorǁvisit_str__mutmut_9(self, node, df):
        s = df[node.field].astype("string")
        if node.mode == "regex":
            return s.str.contains(node.pattern, case=None, regex=True, na=node.na)
        if node.mode == "contains":
            return s.str.contains(
                re.escape(node.pattern), case=node.case, regex=True, na=node.na
            )
        if node.mode == "startswith":
            return s.str.startswith(node.pattern, na=node.na)
        if node.mode == "endswith":
            return s.str.endswith(node.pattern, na=node.na)
        raise ValueError(f"Modo string desconhecido: {node.mode}")

    def xǁPandasVisitorǁvisit_str__mutmut_10(self, node, df):
        s = df[node.field].astype("string")
        if node.mode == "regex":
            return s.str.contains(node.pattern, case=node.case, regex=None, na=node.na)
        if node.mode == "contains":
            return s.str.contains(
                re.escape(node.pattern), case=node.case, regex=True, na=node.na
            )
        if node.mode == "startswith":
            return s.str.startswith(node.pattern, na=node.na)
        if node.mode == "endswith":
            return s.str.endswith(node.pattern, na=node.na)
        raise ValueError(f"Modo string desconhecido: {node.mode}")

    def xǁPandasVisitorǁvisit_str__mutmut_11(self, node, df):
        s = df[node.field].astype("string")
        if node.mode == "regex":
            return s.str.contains(node.pattern, case=node.case, regex=True, na=None)
        if node.mode == "contains":
            return s.str.contains(
                re.escape(node.pattern), case=node.case, regex=True, na=node.na
            )
        if node.mode == "startswith":
            return s.str.startswith(node.pattern, na=node.na)
        if node.mode == "endswith":
            return s.str.endswith(node.pattern, na=node.na)
        raise ValueError(f"Modo string desconhecido: {node.mode}")

    def xǁPandasVisitorǁvisit_str__mutmut_12(self, node, df):
        s = df[node.field].astype("string")
        if node.mode == "regex":
            return s.str.contains(case=node.case, regex=True, na=node.na)
        if node.mode == "contains":
            return s.str.contains(
                re.escape(node.pattern), case=node.case, regex=True, na=node.na
            )
        if node.mode == "startswith":
            return s.str.startswith(node.pattern, na=node.na)
        if node.mode == "endswith":
            return s.str.endswith(node.pattern, na=node.na)
        raise ValueError(f"Modo string desconhecido: {node.mode}")

    def xǁPandasVisitorǁvisit_str__mutmut_13(self, node, df):
        s = df[node.field].astype("string")
        if node.mode == "regex":
            return s.str.contains(node.pattern, regex=True, na=node.na)
        if node.mode == "contains":
            return s.str.contains(
                re.escape(node.pattern), case=node.case, regex=True, na=node.na
            )
        if node.mode == "startswith":
            return s.str.startswith(node.pattern, na=node.na)
        if node.mode == "endswith":
            return s.str.endswith(node.pattern, na=node.na)
        raise ValueError(f"Modo string desconhecido: {node.mode}")

    def xǁPandasVisitorǁvisit_str__mutmut_14(self, node, df):
        s = df[node.field].astype("string")
        if node.mode == "regex":
            return s.str.contains(node.pattern, case=node.case, na=node.na)
        if node.mode == "contains":
            return s.str.contains(
                re.escape(node.pattern), case=node.case, regex=True, na=node.na
            )
        if node.mode == "startswith":
            return s.str.startswith(node.pattern, na=node.na)
        if node.mode == "endswith":
            return s.str.endswith(node.pattern, na=node.na)
        raise ValueError(f"Modo string desconhecido: {node.mode}")

    def xǁPandasVisitorǁvisit_str__mutmut_15(self, node, df):
        s = df[node.field].astype("string")
        if node.mode == "regex":
            return s.str.contains(
                node.pattern,
                case=node.case,
                regex=True,
            )
        if node.mode == "contains":
            return s.str.contains(
                re.escape(node.pattern), case=node.case, regex=True, na=node.na
            )
        if node.mode == "startswith":
            return s.str.startswith(node.pattern, na=node.na)
        if node.mode == "endswith":
            return s.str.endswith(node.pattern, na=node.na)
        raise ValueError(f"Modo string desconhecido: {node.mode}")

    def xǁPandasVisitorǁvisit_str__mutmut_16(self, node, df):
        s = df[node.field].astype("string")
        if node.mode == "regex":
            return s.str.contains(node.pattern, case=node.case, regex=False, na=node.na)
        if node.mode == "contains":
            return s.str.contains(
                re.escape(node.pattern), case=node.case, regex=True, na=node.na
            )
        if node.mode == "startswith":
            return s.str.startswith(node.pattern, na=node.na)
        if node.mode == "endswith":
            return s.str.endswith(node.pattern, na=node.na)
        raise ValueError(f"Modo string desconhecido: {node.mode}")

    def xǁPandasVisitorǁvisit_str__mutmut_17(self, node, df):
        s = df[node.field].astype("string")
        if node.mode == "regex":
            return s.str.contains(node.pattern, case=node.case, regex=True, na=node.na)
        if node.mode != "contains":
            return s.str.contains(
                re.escape(node.pattern), case=node.case, regex=True, na=node.na
            )
        if node.mode == "startswith":
            return s.str.startswith(node.pattern, na=node.na)
        if node.mode == "endswith":
            return s.str.endswith(node.pattern, na=node.na)
        raise ValueError(f"Modo string desconhecido: {node.mode}")

    def xǁPandasVisitorǁvisit_str__mutmut_18(self, node, df):
        s = df[node.field].astype("string")
        if node.mode == "regex":
            return s.str.contains(node.pattern, case=node.case, regex=True, na=node.na)
        if node.mode == "XXcontainsXX":
            return s.str.contains(
                re.escape(node.pattern), case=node.case, regex=True, na=node.na
            )
        if node.mode == "startswith":
            return s.str.startswith(node.pattern, na=node.na)
        if node.mode == "endswith":
            return s.str.endswith(node.pattern, na=node.na)
        raise ValueError(f"Modo string desconhecido: {node.mode}")

    def xǁPandasVisitorǁvisit_str__mutmut_19(self, node, df):
        s = df[node.field].astype("string")
        if node.mode == "regex":
            return s.str.contains(node.pattern, case=node.case, regex=True, na=node.na)
        if node.mode == "CONTAINS":
            return s.str.contains(
                re.escape(node.pattern), case=node.case, regex=True, na=node.na
            )
        if node.mode == "startswith":
            return s.str.startswith(node.pattern, na=node.na)
        if node.mode == "endswith":
            return s.str.endswith(node.pattern, na=node.na)
        raise ValueError(f"Modo string desconhecido: {node.mode}")

    def xǁPandasVisitorǁvisit_str__mutmut_20(self, node, df):
        s = df[node.field].astype("string")
        if node.mode == "regex":
            return s.str.contains(node.pattern, case=node.case, regex=True, na=node.na)
        if node.mode == "contains":
            return s.str.contains(None, case=node.case, regex=True, na=node.na)
        if node.mode == "startswith":
            return s.str.startswith(node.pattern, na=node.na)
        if node.mode == "endswith":
            return s.str.endswith(node.pattern, na=node.na)
        raise ValueError(f"Modo string desconhecido: {node.mode}")

    def xǁPandasVisitorǁvisit_str__mutmut_21(self, node, df):
        s = df[node.field].astype("string")
        if node.mode == "regex":
            return s.str.contains(node.pattern, case=node.case, regex=True, na=node.na)
        if node.mode == "contains":
            return s.str.contains(
                re.escape(node.pattern), case=None, regex=True, na=node.na
            )
        if node.mode == "startswith":
            return s.str.startswith(node.pattern, na=node.na)
        if node.mode == "endswith":
            return s.str.endswith(node.pattern, na=node.na)
        raise ValueError(f"Modo string desconhecido: {node.mode}")

    def xǁPandasVisitorǁvisit_str__mutmut_22(self, node, df):
        s = df[node.field].astype("string")
        if node.mode == "regex":
            return s.str.contains(node.pattern, case=node.case, regex=True, na=node.na)
        if node.mode == "contains":
            return s.str.contains(
                re.escape(node.pattern), case=node.case, regex=None, na=node.na
            )
        if node.mode == "startswith":
            return s.str.startswith(node.pattern, na=node.na)
        if node.mode == "endswith":
            return s.str.endswith(node.pattern, na=node.na)
        raise ValueError(f"Modo string desconhecido: {node.mode}")

    def xǁPandasVisitorǁvisit_str__mutmut_23(self, node, df):
        s = df[node.field].astype("string")
        if node.mode == "regex":
            return s.str.contains(node.pattern, case=node.case, regex=True, na=node.na)
        if node.mode == "contains":
            return s.str.contains(
                re.escape(node.pattern), case=node.case, regex=True, na=None
            )
        if node.mode == "startswith":
            return s.str.startswith(node.pattern, na=node.na)
        if node.mode == "endswith":
            return s.str.endswith(node.pattern, na=node.na)
        raise ValueError(f"Modo string desconhecido: {node.mode}")

    def xǁPandasVisitorǁvisit_str__mutmut_24(self, node, df):
        s = df[node.field].astype("string")
        if node.mode == "regex":
            return s.str.contains(node.pattern, case=node.case, regex=True, na=node.na)
        if node.mode == "contains":
            return s.str.contains(case=node.case, regex=True, na=node.na)
        if node.mode == "startswith":
            return s.str.startswith(node.pattern, na=node.na)
        if node.mode == "endswith":
            return s.str.endswith(node.pattern, na=node.na)
        raise ValueError(f"Modo string desconhecido: {node.mode}")

    def xǁPandasVisitorǁvisit_str__mutmut_25(self, node, df):
        s = df[node.field].astype("string")
        if node.mode == "regex":
            return s.str.contains(node.pattern, case=node.case, regex=True, na=node.na)
        if node.mode == "contains":
            return s.str.contains(re.escape(node.pattern), regex=True, na=node.na)
        if node.mode == "startswith":
            return s.str.startswith(node.pattern, na=node.na)
        if node.mode == "endswith":
            return s.str.endswith(node.pattern, na=node.na)
        raise ValueError(f"Modo string desconhecido: {node.mode}")

    def xǁPandasVisitorǁvisit_str__mutmut_26(self, node, df):
        s = df[node.field].astype("string")
        if node.mode == "regex":
            return s.str.contains(node.pattern, case=node.case, regex=True, na=node.na)
        if node.mode == "contains":
            return s.str.contains(re.escape(node.pattern), case=node.case, na=node.na)
        if node.mode == "startswith":
            return s.str.startswith(node.pattern, na=node.na)
        if node.mode == "endswith":
            return s.str.endswith(node.pattern, na=node.na)
        raise ValueError(f"Modo string desconhecido: {node.mode}")

    def xǁPandasVisitorǁvisit_str__mutmut_27(self, node, df):
        s = df[node.field].astype("string")
        if node.mode == "regex":
            return s.str.contains(node.pattern, case=node.case, regex=True, na=node.na)
        if node.mode == "contains":
            return s.str.contains(
                re.escape(node.pattern),
                case=node.case,
                regex=True,
            )
        if node.mode == "startswith":
            return s.str.startswith(node.pattern, na=node.na)
        if node.mode == "endswith":
            return s.str.endswith(node.pattern, na=node.na)
        raise ValueError(f"Modo string desconhecido: {node.mode}")

    def xǁPandasVisitorǁvisit_str__mutmut_28(self, node, df):
        s = df[node.field].astype("string")
        if node.mode == "regex":
            return s.str.contains(node.pattern, case=node.case, regex=True, na=node.na)
        if node.mode == "contains":
            return s.str.contains(
                re.escape(None), case=node.case, regex=True, na=node.na
            )
        if node.mode == "startswith":
            return s.str.startswith(node.pattern, na=node.na)
        if node.mode == "endswith":
            return s.str.endswith(node.pattern, na=node.na)
        raise ValueError(f"Modo string desconhecido: {node.mode}")

    def xǁPandasVisitorǁvisit_str__mutmut_29(self, node, df):
        s = df[node.field].astype("string")
        if node.mode == "regex":
            return s.str.contains(node.pattern, case=node.case, regex=True, na=node.na)
        if node.mode == "contains":
            return s.str.contains(
                re.escape(node.pattern), case=node.case, regex=False, na=node.na
            )
        if node.mode == "startswith":
            return s.str.startswith(node.pattern, na=node.na)
        if node.mode == "endswith":
            return s.str.endswith(node.pattern, na=node.na)
        raise ValueError(f"Modo string desconhecido: {node.mode}")

    def xǁPandasVisitorǁvisit_str__mutmut_30(self, node, df):
        s = df[node.field].astype("string")
        if node.mode == "regex":
            return s.str.contains(node.pattern, case=node.case, regex=True, na=node.na)
        if node.mode == "contains":
            return s.str.contains(
                re.escape(node.pattern), case=node.case, regex=True, na=node.na
            )
        if node.mode != "startswith":
            return s.str.startswith(node.pattern, na=node.na)
        if node.mode == "endswith":
            return s.str.endswith(node.pattern, na=node.na)
        raise ValueError(f"Modo string desconhecido: {node.mode}")

    def xǁPandasVisitorǁvisit_str__mutmut_31(self, node, df):
        s = df[node.field].astype("string")
        if node.mode == "regex":
            return s.str.contains(node.pattern, case=node.case, regex=True, na=node.na)
        if node.mode == "contains":
            return s.str.contains(
                re.escape(node.pattern), case=node.case, regex=True, na=node.na
            )
        if node.mode == "XXstartswithXX":
            return s.str.startswith(node.pattern, na=node.na)
        if node.mode == "endswith":
            return s.str.endswith(node.pattern, na=node.na)
        raise ValueError(f"Modo string desconhecido: {node.mode}")

    def xǁPandasVisitorǁvisit_str__mutmut_32(self, node, df):
        s = df[node.field].astype("string")
        if node.mode == "regex":
            return s.str.contains(node.pattern, case=node.case, regex=True, na=node.na)
        if node.mode == "contains":
            return s.str.contains(
                re.escape(node.pattern), case=node.case, regex=True, na=node.na
            )
        if node.mode == "STARTSWITH":
            return s.str.startswith(node.pattern, na=node.na)
        if node.mode == "endswith":
            return s.str.endswith(node.pattern, na=node.na)
        raise ValueError(f"Modo string desconhecido: {node.mode}")

    def xǁPandasVisitorǁvisit_str__mutmut_33(self, node, df):
        s = df[node.field].astype("string")
        if node.mode == "regex":
            return s.str.contains(node.pattern, case=node.case, regex=True, na=node.na)
        if node.mode == "contains":
            return s.str.contains(
                re.escape(node.pattern), case=node.case, regex=True, na=node.na
            )
        if node.mode == "startswith":
            return s.str.startswith(None, na=node.na)
        if node.mode == "endswith":
            return s.str.endswith(node.pattern, na=node.na)
        raise ValueError(f"Modo string desconhecido: {node.mode}")

    def xǁPandasVisitorǁvisit_str__mutmut_34(self, node, df):
        s = df[node.field].astype("string")
        if node.mode == "regex":
            return s.str.contains(node.pattern, case=node.case, regex=True, na=node.na)
        if node.mode == "contains":
            return s.str.contains(
                re.escape(node.pattern), case=node.case, regex=True, na=node.na
            )
        if node.mode == "startswith":
            return s.str.startswith(node.pattern, na=None)
        if node.mode == "endswith":
            return s.str.endswith(node.pattern, na=node.na)
        raise ValueError(f"Modo string desconhecido: {node.mode}")

    def xǁPandasVisitorǁvisit_str__mutmut_35(self, node, df):
        s = df[node.field].astype("string")
        if node.mode == "regex":
            return s.str.contains(node.pattern, case=node.case, regex=True, na=node.na)
        if node.mode == "contains":
            return s.str.contains(
                re.escape(node.pattern), case=node.case, regex=True, na=node.na
            )
        if node.mode == "startswith":
            return s.str.startswith(na=node.na)
        if node.mode == "endswith":
            return s.str.endswith(node.pattern, na=node.na)
        raise ValueError(f"Modo string desconhecido: {node.mode}")

    def xǁPandasVisitorǁvisit_str__mutmut_36(self, node, df):
        s = df[node.field].astype("string")
        if node.mode == "regex":
            return s.str.contains(node.pattern, case=node.case, regex=True, na=node.na)
        if node.mode == "contains":
            return s.str.contains(
                re.escape(node.pattern), case=node.case, regex=True, na=node.na
            )
        if node.mode == "startswith":
            return s.str.startswith(
                node.pattern,
            )
        if node.mode == "endswith":
            return s.str.endswith(node.pattern, na=node.na)
        raise ValueError(f"Modo string desconhecido: {node.mode}")

    def xǁPandasVisitorǁvisit_str__mutmut_37(self, node, df):
        s = df[node.field].astype("string")
        if node.mode == "regex":
            return s.str.contains(node.pattern, case=node.case, regex=True, na=node.na)
        if node.mode == "contains":
            return s.str.contains(
                re.escape(node.pattern), case=node.case, regex=True, na=node.na
            )
        if node.mode == "startswith":
            return s.str.startswith(node.pattern, na=node.na)
        if node.mode != "endswith":
            return s.str.endswith(node.pattern, na=node.na)
        raise ValueError(f"Modo string desconhecido: {node.mode}")

    def xǁPandasVisitorǁvisit_str__mutmut_38(self, node, df):
        s = df[node.field].astype("string")
        if node.mode == "regex":
            return s.str.contains(node.pattern, case=node.case, regex=True, na=node.na)
        if node.mode == "contains":
            return s.str.contains(
                re.escape(node.pattern), case=node.case, regex=True, na=node.na
            )
        if node.mode == "startswith":
            return s.str.startswith(node.pattern, na=node.na)
        if node.mode == "XXendswithXX":
            return s.str.endswith(node.pattern, na=node.na)
        raise ValueError(f"Modo string desconhecido: {node.mode}")

    def xǁPandasVisitorǁvisit_str__mutmut_39(self, node, df):
        s = df[node.field].astype("string")
        if node.mode == "regex":
            return s.str.contains(node.pattern, case=node.case, regex=True, na=node.na)
        if node.mode == "contains":
            return s.str.contains(
                re.escape(node.pattern), case=node.case, regex=True, na=node.na
            )
        if node.mode == "startswith":
            return s.str.startswith(node.pattern, na=node.na)
        if node.mode == "ENDSWITH":
            return s.str.endswith(node.pattern, na=node.na)
        raise ValueError(f"Modo string desconhecido: {node.mode}")

    def xǁPandasVisitorǁvisit_str__mutmut_40(self, node, df):
        s = df[node.field].astype("string")
        if node.mode == "regex":
            return s.str.contains(node.pattern, case=node.case, regex=True, na=node.na)
        if node.mode == "contains":
            return s.str.contains(
                re.escape(node.pattern), case=node.case, regex=True, na=node.na
            )
        if node.mode == "startswith":
            return s.str.startswith(node.pattern, na=node.na)
        if node.mode == "endswith":
            return s.str.endswith(None, na=node.na)
        raise ValueError(f"Modo string desconhecido: {node.mode}")

    def xǁPandasVisitorǁvisit_str__mutmut_41(self, node, df):
        s = df[node.field].astype("string")
        if node.mode == "regex":
            return s.str.contains(node.pattern, case=node.case, regex=True, na=node.na)
        if node.mode == "contains":
            return s.str.contains(
                re.escape(node.pattern), case=node.case, regex=True, na=node.na
            )
        if node.mode == "startswith":
            return s.str.startswith(node.pattern, na=node.na)
        if node.mode == "endswith":
            return s.str.endswith(node.pattern, na=None)
        raise ValueError(f"Modo string desconhecido: {node.mode}")

    def xǁPandasVisitorǁvisit_str__mutmut_42(self, node, df):
        s = df[node.field].astype("string")
        if node.mode == "regex":
            return s.str.contains(node.pattern, case=node.case, regex=True, na=node.na)
        if node.mode == "contains":
            return s.str.contains(
                re.escape(node.pattern), case=node.case, regex=True, na=node.na
            )
        if node.mode == "startswith":
            return s.str.startswith(node.pattern, na=node.na)
        if node.mode == "endswith":
            return s.str.endswith(na=node.na)
        raise ValueError(f"Modo string desconhecido: {node.mode}")

    def xǁPandasVisitorǁvisit_str__mutmut_43(self, node, df):
        s = df[node.field].astype("string")
        if node.mode == "regex":
            return s.str.contains(node.pattern, case=node.case, regex=True, na=node.na)
        if node.mode == "contains":
            return s.str.contains(
                re.escape(node.pattern), case=node.case, regex=True, na=node.na
            )
        if node.mode == "startswith":
            return s.str.startswith(node.pattern, na=node.na)
        if node.mode == "endswith":
            return s.str.endswith(
                node.pattern,
            )
        raise ValueError(f"Modo string desconhecido: {node.mode}")

    def xǁPandasVisitorǁvisit_str__mutmut_44(self, node, df):
        s = df[node.field].astype("string")
        if node.mode == "regex":
            return s.str.contains(node.pattern, case=node.case, regex=True, na=node.na)
        if node.mode == "contains":
            return s.str.contains(
                re.escape(node.pattern), case=node.case, regex=True, na=node.na
            )
        if node.mode == "startswith":
            return s.str.startswith(node.pattern, na=node.na)
        if node.mode == "endswith":
            return s.str.endswith(node.pattern, na=node.na)
        raise ValueError(None)

    xǁPandasVisitorǁvisit_str__mutmut_mutants: ClassVar[MutantDict] = {  # type: ignore
        "xǁPandasVisitorǁvisit_str__mutmut_1": xǁPandasVisitorǁvisit_str__mutmut_1,
        "xǁPandasVisitorǁvisit_str__mutmut_2": xǁPandasVisitorǁvisit_str__mutmut_2,
        "xǁPandasVisitorǁvisit_str__mutmut_3": xǁPandasVisitorǁvisit_str__mutmut_3,
        "xǁPandasVisitorǁvisit_str__mutmut_4": xǁPandasVisitorǁvisit_str__mutmut_4,
        "xǁPandasVisitorǁvisit_str__mutmut_5": xǁPandasVisitorǁvisit_str__mutmut_5,
        "xǁPandasVisitorǁvisit_str__mutmut_6": xǁPandasVisitorǁvisit_str__mutmut_6,
        "xǁPandasVisitorǁvisit_str__mutmut_7": xǁPandasVisitorǁvisit_str__mutmut_7,
        "xǁPandasVisitorǁvisit_str__mutmut_8": xǁPandasVisitorǁvisit_str__mutmut_8,
        "xǁPandasVisitorǁvisit_str__mutmut_9": xǁPandasVisitorǁvisit_str__mutmut_9,
        "xǁPandasVisitorǁvisit_str__mutmut_10": xǁPandasVisitorǁvisit_str__mutmut_10,
        "xǁPandasVisitorǁvisit_str__mutmut_11": xǁPandasVisitorǁvisit_str__mutmut_11,
        "xǁPandasVisitorǁvisit_str__mutmut_12": xǁPandasVisitorǁvisit_str__mutmut_12,
        "xǁPandasVisitorǁvisit_str__mutmut_13": xǁPandasVisitorǁvisit_str__mutmut_13,
        "xǁPandasVisitorǁvisit_str__mutmut_14": xǁPandasVisitorǁvisit_str__mutmut_14,
        "xǁPandasVisitorǁvisit_str__mutmut_15": xǁPandasVisitorǁvisit_str__mutmut_15,
        "xǁPandasVisitorǁvisit_str__mutmut_16": xǁPandasVisitorǁvisit_str__mutmut_16,
        "xǁPandasVisitorǁvisit_str__mutmut_17": xǁPandasVisitorǁvisit_str__mutmut_17,
        "xǁPandasVisitorǁvisit_str__mutmut_18": xǁPandasVisitorǁvisit_str__mutmut_18,
        "xǁPandasVisitorǁvisit_str__mutmut_19": xǁPandasVisitorǁvisit_str__mutmut_19,
        "xǁPandasVisitorǁvisit_str__mutmut_20": xǁPandasVisitorǁvisit_str__mutmut_20,
        "xǁPandasVisitorǁvisit_str__mutmut_21": xǁPandasVisitorǁvisit_str__mutmut_21,
        "xǁPandasVisitorǁvisit_str__mutmut_22": xǁPandasVisitorǁvisit_str__mutmut_22,
        "xǁPandasVisitorǁvisit_str__mutmut_23": xǁPandasVisitorǁvisit_str__mutmut_23,
        "xǁPandasVisitorǁvisit_str__mutmut_24": xǁPandasVisitorǁvisit_str__mutmut_24,
        "xǁPandasVisitorǁvisit_str__mutmut_25": xǁPandasVisitorǁvisit_str__mutmut_25,
        "xǁPandasVisitorǁvisit_str__mutmut_26": xǁPandasVisitorǁvisit_str__mutmut_26,
        "xǁPandasVisitorǁvisit_str__mutmut_27": xǁPandasVisitorǁvisit_str__mutmut_27,
        "xǁPandasVisitorǁvisit_str__mutmut_28": xǁPandasVisitorǁvisit_str__mutmut_28,
        "xǁPandasVisitorǁvisit_str__mutmut_29": xǁPandasVisitorǁvisit_str__mutmut_29,
        "xǁPandasVisitorǁvisit_str__mutmut_30": xǁPandasVisitorǁvisit_str__mutmut_30,
        "xǁPandasVisitorǁvisit_str__mutmut_31": xǁPandasVisitorǁvisit_str__mutmut_31,
        "xǁPandasVisitorǁvisit_str__mutmut_32": xǁPandasVisitorǁvisit_str__mutmut_32,
        "xǁPandasVisitorǁvisit_str__mutmut_33": xǁPandasVisitorǁvisit_str__mutmut_33,
        "xǁPandasVisitorǁvisit_str__mutmut_34": xǁPandasVisitorǁvisit_str__mutmut_34,
        "xǁPandasVisitorǁvisit_str__mutmut_35": xǁPandasVisitorǁvisit_str__mutmut_35,
        "xǁPandasVisitorǁvisit_str__mutmut_36": xǁPandasVisitorǁvisit_str__mutmut_36,
        "xǁPandasVisitorǁvisit_str__mutmut_37": xǁPandasVisitorǁvisit_str__mutmut_37,
        "xǁPandasVisitorǁvisit_str__mutmut_38": xǁPandasVisitorǁvisit_str__mutmut_38,
        "xǁPandasVisitorǁvisit_str__mutmut_39": xǁPandasVisitorǁvisit_str__mutmut_39,
        "xǁPandasVisitorǁvisit_str__mutmut_40": xǁPandasVisitorǁvisit_str__mutmut_40,
        "xǁPandasVisitorǁvisit_str__mutmut_41": xǁPandasVisitorǁvisit_str__mutmut_41,
        "xǁPandasVisitorǁvisit_str__mutmut_42": xǁPandasVisitorǁvisit_str__mutmut_42,
        "xǁPandasVisitorǁvisit_str__mutmut_43": xǁPandasVisitorǁvisit_str__mutmut_43,
        "xǁPandasVisitorǁvisit_str__mutmut_44": xǁPandasVisitorǁvisit_str__mutmut_44,
    }
    xǁPandasVisitorǁvisit_str__mutmut_orig.__name__ = "xǁPandasVisitorǁvisit_str"

    def visit_list_any(self, node, df):
        args = [node, df]  # type: ignore
        kwargs = {}  # type: ignore
        return _mutmut_trampoline(
            object.__getattribute__(
                self, "xǁPandasVisitorǁvisit_list_any__mutmut_orig"
            ),
            object.__getattribute__(
                self, "xǁPandasVisitorǁvisit_list_any__mutmut_mutants"
            ),
            args,
            kwargs,
            self,
        )

    def xǁPandasVisitorǁvisit_list_any__mutmut_orig(self, node, df):
        """Suporta listas de strings em JSON. Converte None->[] e padroniza."""
        s = ensure_list_col(df[node.field])
        if node.op == "contains":
            x = str(node.value)
            return s.apply(lambda xs: any(x == str(i) for i in xs))
        if node.op == "in":
            vals = {
                str(v)
                for v in (
                    node.value
                    if isinstance(node.value, (list, tuple, set))
                    else [node.value]
                )
            }
            return s.apply(lambda xs: any(str(i) in vals for i in xs))
        if node.op == "overlap":
            vals = {str(v) for v in node.value}
            return s.apply(lambda xs: bool(vals.intersection({str(i) for i in xs})))
        raise ValueError(f"Operador lista desconhecido: {node.op}")

    def xǁPandasVisitorǁvisit_list_any__mutmut_1(self, node, df):
        """Suporta listas de strings em JSON. Converte None->[] e padroniza."""
        s = None
        if node.op == "contains":
            x = str(node.value)
            return s.apply(lambda xs: any(x == str(i) for i in xs))
        if node.op == "in":
            vals = {
                str(v)
                for v in (
                    node.value
                    if isinstance(node.value, (list, tuple, set))
                    else [node.value]
                )
            }
            return s.apply(lambda xs: any(str(i) in vals for i in xs))
        if node.op == "overlap":
            vals = {str(v) for v in node.value}
            return s.apply(lambda xs: bool(vals.intersection({str(i) for i in xs})))
        raise ValueError(f"Operador lista desconhecido: {node.op}")

    def xǁPandasVisitorǁvisit_list_any__mutmut_2(self, node, df):
        """Suporta listas de strings em JSON. Converte None->[] e padroniza."""
        s = ensure_list_col(None)
        if node.op == "contains":
            x = str(node.value)
            return s.apply(lambda xs: any(x == str(i) for i in xs))
        if node.op == "in":
            vals = {
                str(v)
                for v in (
                    node.value
                    if isinstance(node.value, (list, tuple, set))
                    else [node.value]
                )
            }
            return s.apply(lambda xs: any(str(i) in vals for i in xs))
        if node.op == "overlap":
            vals = {str(v) for v in node.value}
            return s.apply(lambda xs: bool(vals.intersection({str(i) for i in xs})))
        raise ValueError(f"Operador lista desconhecido: {node.op}")

    def xǁPandasVisitorǁvisit_list_any__mutmut_3(self, node, df):
        """Suporta listas de strings em JSON. Converte None->[] e padroniza."""
        s = ensure_list_col(df[node.field])
        if node.op != "contains":
            x = str(node.value)
            return s.apply(lambda xs: any(x == str(i) for i in xs))
        if node.op == "in":
            vals = {
                str(v)
                for v in (
                    node.value
                    if isinstance(node.value, (list, tuple, set))
                    else [node.value]
                )
            }
            return s.apply(lambda xs: any(str(i) in vals for i in xs))
        if node.op == "overlap":
            vals = {str(v) for v in node.value}
            return s.apply(lambda xs: bool(vals.intersection({str(i) for i in xs})))
        raise ValueError(f"Operador lista desconhecido: {node.op}")

    def xǁPandasVisitorǁvisit_list_any__mutmut_4(self, node, df):
        """Suporta listas de strings em JSON. Converte None->[] e padroniza."""
        s = ensure_list_col(df[node.field])
        if node.op == "XXcontainsXX":
            x = str(node.value)
            return s.apply(lambda xs: any(x == str(i) for i in xs))
        if node.op == "in":
            vals = {
                str(v)
                for v in (
                    node.value
                    if isinstance(node.value, (list, tuple, set))
                    else [node.value]
                )
            }
            return s.apply(lambda xs: any(str(i) in vals for i in xs))
        if node.op == "overlap":
            vals = {str(v) for v in node.value}
            return s.apply(lambda xs: bool(vals.intersection({str(i) for i in xs})))
        raise ValueError(f"Operador lista desconhecido: {node.op}")

    def xǁPandasVisitorǁvisit_list_any__mutmut_5(self, node, df):
        """Suporta listas de strings em JSON. Converte None->[] e padroniza."""
        s = ensure_list_col(df[node.field])
        if node.op == "CONTAINS":
            x = str(node.value)
            return s.apply(lambda xs: any(x == str(i) for i in xs))
        if node.op == "in":
            vals = {
                str(v)
                for v in (
                    node.value
                    if isinstance(node.value, (list, tuple, set))
                    else [node.value]
                )
            }
            return s.apply(lambda xs: any(str(i) in vals for i in xs))
        if node.op == "overlap":
            vals = {str(v) for v in node.value}
            return s.apply(lambda xs: bool(vals.intersection({str(i) for i in xs})))
        raise ValueError(f"Operador lista desconhecido: {node.op}")

    def xǁPandasVisitorǁvisit_list_any__mutmut_6(self, node, df):
        """Suporta listas de strings em JSON. Converte None->[] e padroniza."""
        s = ensure_list_col(df[node.field])
        if node.op == "contains":
            x = None
            return s.apply(lambda xs: any(x == str(i) for i in xs))
        if node.op == "in":
            vals = {
                str(v)
                for v in (
                    node.value
                    if isinstance(node.value, (list, tuple, set))
                    else [node.value]
                )
            }
            return s.apply(lambda xs: any(str(i) in vals for i in xs))
        if node.op == "overlap":
            vals = {str(v) for v in node.value}
            return s.apply(lambda xs: bool(vals.intersection({str(i) for i in xs})))
        raise ValueError(f"Operador lista desconhecido: {node.op}")

    def xǁPandasVisitorǁvisit_list_any__mutmut_7(self, node, df):
        """Suporta listas de strings em JSON. Converte None->[] e padroniza."""
        s = ensure_list_col(df[node.field])
        if node.op == "contains":
            x = str(None)
            return s.apply(lambda xs: any(x == str(i) for i in xs))
        if node.op == "in":
            vals = {
                str(v)
                for v in (
                    node.value
                    if isinstance(node.value, (list, tuple, set))
                    else [node.value]
                )
            }
            return s.apply(lambda xs: any(str(i) in vals for i in xs))
        if node.op == "overlap":
            vals = {str(v) for v in node.value}
            return s.apply(lambda xs: bool(vals.intersection({str(i) for i in xs})))
        raise ValueError(f"Operador lista desconhecido: {node.op}")

    def xǁPandasVisitorǁvisit_list_any__mutmut_8(self, node, df):
        """Suporta listas de strings em JSON. Converte None->[] e padroniza."""
        s = ensure_list_col(df[node.field])
        if node.op == "contains":
            x = str(node.value)
            return s.apply(None)
        if node.op == "in":
            vals = {
                str(v)
                for v in (
                    node.value
                    if isinstance(node.value, (list, tuple, set))
                    else [node.value]
                )
            }
            return s.apply(lambda xs: any(str(i) in vals for i in xs))
        if node.op == "overlap":
            vals = {str(v) for v in node.value}
            return s.apply(lambda xs: bool(vals.intersection({str(i) for i in xs})))
        raise ValueError(f"Operador lista desconhecido: {node.op}")

    def xǁPandasVisitorǁvisit_list_any__mutmut_9(self, node, df):
        """Suporta listas de strings em JSON. Converte None->[] e padroniza."""
        s = ensure_list_col(df[node.field])
        if node.op == "contains":
            x = str(node.value)
            return s.apply(lambda xs: None)
        if node.op == "in":
            vals = {
                str(v)
                for v in (
                    node.value
                    if isinstance(node.value, (list, tuple, set))
                    else [node.value]
                )
            }
            return s.apply(lambda xs: any(str(i) in vals for i in xs))
        if node.op == "overlap":
            vals = {str(v) for v in node.value}
            return s.apply(lambda xs: bool(vals.intersection({str(i) for i in xs})))
        raise ValueError(f"Operador lista desconhecido: {node.op}")

    def xǁPandasVisitorǁvisit_list_any__mutmut_10(self, node, df):
        """Suporta listas de strings em JSON. Converte None->[] e padroniza."""
        s = ensure_list_col(df[node.field])
        if node.op == "contains":
            x = str(node.value)
            return s.apply(lambda xs: any(None))
        if node.op == "in":
            vals = {
                str(v)
                for v in (
                    node.value
                    if isinstance(node.value, (list, tuple, set))
                    else [node.value]
                )
            }
            return s.apply(lambda xs: any(str(i) in vals for i in xs))
        if node.op == "overlap":
            vals = {str(v) for v in node.value}
            return s.apply(lambda xs: bool(vals.intersection({str(i) for i in xs})))
        raise ValueError(f"Operador lista desconhecido: {node.op}")

    def xǁPandasVisitorǁvisit_list_any__mutmut_11(self, node, df):
        """Suporta listas de strings em JSON. Converte None->[] e padroniza."""
        s = ensure_list_col(df[node.field])
        if node.op == "contains":
            x = str(node.value)
            return s.apply(lambda xs: any(x != str(i) for i in xs))
        if node.op == "in":
            vals = {
                str(v)
                for v in (
                    node.value
                    if isinstance(node.value, (list, tuple, set))
                    else [node.value]
                )
            }
            return s.apply(lambda xs: any(str(i) in vals for i in xs))
        if node.op == "overlap":
            vals = {str(v) for v in node.value}
            return s.apply(lambda xs: bool(vals.intersection({str(i) for i in xs})))
        raise ValueError(f"Operador lista desconhecido: {node.op}")

    def xǁPandasVisitorǁvisit_list_any__mutmut_12(self, node, df):
        """Suporta listas de strings em JSON. Converte None->[] e padroniza."""
        s = ensure_list_col(df[node.field])
        if node.op == "contains":
            x = str(node.value)
            return s.apply(lambda xs: any(x == str(None) for i in xs))
        if node.op == "in":
            vals = {
                str(v)
                for v in (
                    node.value
                    if isinstance(node.value, (list, tuple, set))
                    else [node.value]
                )
            }
            return s.apply(lambda xs: any(str(i) in vals for i in xs))
        if node.op == "overlap":
            vals = {str(v) for v in node.value}
            return s.apply(lambda xs: bool(vals.intersection({str(i) for i in xs})))
        raise ValueError(f"Operador lista desconhecido: {node.op}")

    def xǁPandasVisitorǁvisit_list_any__mutmut_13(self, node, df):
        """Suporta listas de strings em JSON. Converte None->[] e padroniza."""
        s = ensure_list_col(df[node.field])
        if node.op == "contains":
            x = str(node.value)
            return s.apply(lambda xs: any(x == str(i) for i in xs))
        if node.op != "in":
            vals = {
                str(v)
                for v in (
                    node.value
                    if isinstance(node.value, (list, tuple, set))
                    else [node.value]
                )
            }
            return s.apply(lambda xs: any(str(i) in vals for i in xs))
        if node.op == "overlap":
            vals = {str(v) for v in node.value}
            return s.apply(lambda xs: bool(vals.intersection({str(i) for i in xs})))
        raise ValueError(f"Operador lista desconhecido: {node.op}")

    def xǁPandasVisitorǁvisit_list_any__mutmut_14(self, node, df):
        """Suporta listas de strings em JSON. Converte None->[] e padroniza."""
        s = ensure_list_col(df[node.field])
        if node.op == "contains":
            x = str(node.value)
            return s.apply(lambda xs: any(x == str(i) for i in xs))
        if node.op == "XXinXX":
            vals = {
                str(v)
                for v in (
                    node.value
                    if isinstance(node.value, (list, tuple, set))
                    else [node.value]
                )
            }
            return s.apply(lambda xs: any(str(i) in vals for i in xs))
        if node.op == "overlap":
            vals = {str(v) for v in node.value}
            return s.apply(lambda xs: bool(vals.intersection({str(i) for i in xs})))
        raise ValueError(f"Operador lista desconhecido: {node.op}")

    def xǁPandasVisitorǁvisit_list_any__mutmut_15(self, node, df):
        """Suporta listas de strings em JSON. Converte None->[] e padroniza."""
        s = ensure_list_col(df[node.field])
        if node.op == "contains":
            x = str(node.value)
            return s.apply(lambda xs: any(x == str(i) for i in xs))
        if node.op == "IN":
            vals = {
                str(v)
                for v in (
                    node.value
                    if isinstance(node.value, (list, tuple, set))
                    else [node.value]
                )
            }
            return s.apply(lambda xs: any(str(i) in vals for i in xs))
        if node.op == "overlap":
            vals = {str(v) for v in node.value}
            return s.apply(lambda xs: bool(vals.intersection({str(i) for i in xs})))
        raise ValueError(f"Operador lista desconhecido: {node.op}")

    def xǁPandasVisitorǁvisit_list_any__mutmut_16(self, node, df):
        """Suporta listas de strings em JSON. Converte None->[] e padroniza."""
        s = ensure_list_col(df[node.field])
        if node.op == "contains":
            x = str(node.value)
            return s.apply(lambda xs: any(x == str(i) for i in xs))
        if node.op == "in":
            vals = None
            return s.apply(lambda xs: any(str(i) in vals for i in xs))
        if node.op == "overlap":
            vals = {str(v) for v in node.value}
            return s.apply(lambda xs: bool(vals.intersection({str(i) for i in xs})))
        raise ValueError(f"Operador lista desconhecido: {node.op}")

    def xǁPandasVisitorǁvisit_list_any__mutmut_17(self, node, df):
        """Suporta listas de strings em JSON. Converte None->[] e padroniza."""
        s = ensure_list_col(df[node.field])
        if node.op == "contains":
            x = str(node.value)
            return s.apply(lambda xs: any(x == str(i) for i in xs))
        if node.op == "in":
            vals = {
                str(None)
                for v in (
                    node.value
                    if isinstance(node.value, (list, tuple, set))
                    else [node.value]
                )
            }
            return s.apply(lambda xs: any(str(i) in vals for i in xs))
        if node.op == "overlap":
            vals = {str(v) for v in node.value}
            return s.apply(lambda xs: bool(vals.intersection({str(i) for i in xs})))
        raise ValueError(f"Operador lista desconhecido: {node.op}")

    def xǁPandasVisitorǁvisit_list_any__mutmut_18(self, node, df):
        """Suporta listas de strings em JSON. Converte None->[] e padroniza."""
        s = ensure_list_col(df[node.field])
        if node.op == "contains":
            x = str(node.value)
            return s.apply(lambda xs: any(x == str(i) for i in xs))
        if node.op == "in":
            vals = {
                str(v)
                for v in (
                    node.value
                    if isinstance(node.value, (list, tuple, set))
                    else [node.value]
                )
            }
            return s.apply(None)
        if node.op == "overlap":
            vals = {str(v) for v in node.value}
            return s.apply(lambda xs: bool(vals.intersection({str(i) for i in xs})))
        raise ValueError(f"Operador lista desconhecido: {node.op}")

    def xǁPandasVisitorǁvisit_list_any__mutmut_19(self, node, df):
        """Suporta listas de strings em JSON. Converte None->[] e padroniza."""
        s = ensure_list_col(df[node.field])
        if node.op == "contains":
            x = str(node.value)
            return s.apply(lambda xs: any(x == str(i) for i in xs))
        if node.op == "in":
            vals = {
                str(v)
                for v in (
                    node.value
                    if isinstance(node.value, (list, tuple, set))
                    else [node.value]
                )
            }
            return s.apply(lambda xs: None)
        if node.op == "overlap":
            vals = {str(v) for v in node.value}
            return s.apply(lambda xs: bool(vals.intersection({str(i) for i in xs})))
        raise ValueError(f"Operador lista desconhecido: {node.op}")

    def xǁPandasVisitorǁvisit_list_any__mutmut_20(self, node, df):
        """Suporta listas de strings em JSON. Converte None->[] e padroniza."""
        s = ensure_list_col(df[node.field])
        if node.op == "contains":
            x = str(node.value)
            return s.apply(lambda xs: any(x == str(i) for i in xs))
        if node.op == "in":
            vals = {
                str(v)
                for v in (
                    node.value
                    if isinstance(node.value, (list, tuple, set))
                    else [node.value]
                )
            }
            return s.apply(lambda xs: any(None))
        if node.op == "overlap":
            vals = {str(v) for v in node.value}
            return s.apply(lambda xs: bool(vals.intersection({str(i) for i in xs})))
        raise ValueError(f"Operador lista desconhecido: {node.op}")

    def xǁPandasVisitorǁvisit_list_any__mutmut_21(self, node, df):
        """Suporta listas de strings em JSON. Converte None->[] e padroniza."""
        s = ensure_list_col(df[node.field])
        if node.op == "contains":
            x = str(node.value)
            return s.apply(lambda xs: any(x == str(i) for i in xs))
        if node.op == "in":
            vals = {
                str(v)
                for v in (
                    node.value
                    if isinstance(node.value, (list, tuple, set))
                    else [node.value]
                )
            }
            return s.apply(lambda xs: any(str(None) in vals for i in xs))
        if node.op == "overlap":
            vals = {str(v) for v in node.value}
            return s.apply(lambda xs: bool(vals.intersection({str(i) for i in xs})))
        raise ValueError(f"Operador lista desconhecido: {node.op}")

    def xǁPandasVisitorǁvisit_list_any__mutmut_22(self, node, df):
        """Suporta listas de strings em JSON. Converte None->[] e padroniza."""
        s = ensure_list_col(df[node.field])
        if node.op == "contains":
            x = str(node.value)
            return s.apply(lambda xs: any(x == str(i) for i in xs))
        if node.op == "in":
            vals = {
                str(v)
                for v in (
                    node.value
                    if isinstance(node.value, (list, tuple, set))
                    else [node.value]
                )
            }
            return s.apply(lambda xs: any(str(i) not in vals for i in xs))
        if node.op == "overlap":
            vals = {str(v) for v in node.value}
            return s.apply(lambda xs: bool(vals.intersection({str(i) for i in xs})))
        raise ValueError(f"Operador lista desconhecido: {node.op}")

    def xǁPandasVisitorǁvisit_list_any__mutmut_23(self, node, df):
        """Suporta listas de strings em JSON. Converte None->[] e padroniza."""
        s = ensure_list_col(df[node.field])
        if node.op == "contains":
            x = str(node.value)
            return s.apply(lambda xs: any(x == str(i) for i in xs))
        if node.op == "in":
            vals = {
                str(v)
                for v in (
                    node.value
                    if isinstance(node.value, (list, tuple, set))
                    else [node.value]
                )
            }
            return s.apply(lambda xs: any(str(i) in vals for i in xs))
        if node.op != "overlap":
            vals = {str(v) for v in node.value}
            return s.apply(lambda xs: bool(vals.intersection({str(i) for i in xs})))
        raise ValueError(f"Operador lista desconhecido: {node.op}")

    def xǁPandasVisitorǁvisit_list_any__mutmut_24(self, node, df):
        """Suporta listas de strings em JSON. Converte None->[] e padroniza."""
        s = ensure_list_col(df[node.field])
        if node.op == "contains":
            x = str(node.value)
            return s.apply(lambda xs: any(x == str(i) for i in xs))
        if node.op == "in":
            vals = {
                str(v)
                for v in (
                    node.value
                    if isinstance(node.value, (list, tuple, set))
                    else [node.value]
                )
            }
            return s.apply(lambda xs: any(str(i) in vals for i in xs))
        if node.op == "XXoverlapXX":
            vals = {str(v) for v in node.value}
            return s.apply(lambda xs: bool(vals.intersection({str(i) for i in xs})))
        raise ValueError(f"Operador lista desconhecido: {node.op}")

    def xǁPandasVisitorǁvisit_list_any__mutmut_25(self, node, df):
        """Suporta listas de strings em JSON. Converte None->[] e padroniza."""
        s = ensure_list_col(df[node.field])
        if node.op == "contains":
            x = str(node.value)
            return s.apply(lambda xs: any(x == str(i) for i in xs))
        if node.op == "in":
            vals = {
                str(v)
                for v in (
                    node.value
                    if isinstance(node.value, (list, tuple, set))
                    else [node.value]
                )
            }
            return s.apply(lambda xs: any(str(i) in vals for i in xs))
        if node.op == "OVERLAP":
            vals = {str(v) for v in node.value}
            return s.apply(lambda xs: bool(vals.intersection({str(i) for i in xs})))
        raise ValueError(f"Operador lista desconhecido: {node.op}")

    def xǁPandasVisitorǁvisit_list_any__mutmut_26(self, node, df):
        """Suporta listas de strings em JSON. Converte None->[] e padroniza."""
        s = ensure_list_col(df[node.field])
        if node.op == "contains":
            x = str(node.value)
            return s.apply(lambda xs: any(x == str(i) for i in xs))
        if node.op == "in":
            vals = {
                str(v)
                for v in (
                    node.value
                    if isinstance(node.value, (list, tuple, set))
                    else [node.value]
                )
            }
            return s.apply(lambda xs: any(str(i) in vals for i in xs))
        if node.op == "overlap":
            vals = None
            return s.apply(lambda xs: bool(vals.intersection({str(i) for i in xs})))
        raise ValueError(f"Operador lista desconhecido: {node.op}")

    def xǁPandasVisitorǁvisit_list_any__mutmut_27(self, node, df):
        """Suporta listas de strings em JSON. Converte None->[] e padroniza."""
        s = ensure_list_col(df[node.field])
        if node.op == "contains":
            x = str(node.value)
            return s.apply(lambda xs: any(x == str(i) for i in xs))
        if node.op == "in":
            vals = {
                str(v)
                for v in (
                    node.value
                    if isinstance(node.value, (list, tuple, set))
                    else [node.value]
                )
            }
            return s.apply(lambda xs: any(str(i) in vals for i in xs))
        if node.op == "overlap":
            vals = {str(None) for v in node.value}
            return s.apply(lambda xs: bool(vals.intersection({str(i) for i in xs})))
        raise ValueError(f"Operador lista desconhecido: {node.op}")

    def xǁPandasVisitorǁvisit_list_any__mutmut_28(self, node, df):
        """Suporta listas de strings em JSON. Converte None->[] e padroniza."""
        s = ensure_list_col(df[node.field])
        if node.op == "contains":
            x = str(node.value)
            return s.apply(lambda xs: any(x == str(i) for i in xs))
        if node.op == "in":
            vals = {
                str(v)
                for v in (
                    node.value
                    if isinstance(node.value, (list, tuple, set))
                    else [node.value]
                )
            }
            return s.apply(lambda xs: any(str(i) in vals for i in xs))
        if node.op == "overlap":
            vals = {str(v) for v in node.value}
            return s.apply(None)
        raise ValueError(f"Operador lista desconhecido: {node.op}")

    def xǁPandasVisitorǁvisit_list_any__mutmut_29(self, node, df):
        """Suporta listas de strings em JSON. Converte None->[] e padroniza."""
        s = ensure_list_col(df[node.field])
        if node.op == "contains":
            x = str(node.value)
            return s.apply(lambda xs: any(x == str(i) for i in xs))
        if node.op == "in":
            vals = {
                str(v)
                for v in (
                    node.value
                    if isinstance(node.value, (list, tuple, set))
                    else [node.value]
                )
            }
            return s.apply(lambda xs: any(str(i) in vals for i in xs))
        if node.op == "overlap":
            vals = {str(v) for v in node.value}
            return s.apply(lambda xs: None)
        raise ValueError(f"Operador lista desconhecido: {node.op}")

    def xǁPandasVisitorǁvisit_list_any__mutmut_30(self, node, df):
        """Suporta listas de strings em JSON. Converte None->[] e padroniza."""
        s = ensure_list_col(df[node.field])
        if node.op == "contains":
            x = str(node.value)
            return s.apply(lambda xs: any(x == str(i) for i in xs))
        if node.op == "in":
            vals = {
                str(v)
                for v in (
                    node.value
                    if isinstance(node.value, (list, tuple, set))
                    else [node.value]
                )
            }
            return s.apply(lambda xs: any(str(i) in vals for i in xs))
        if node.op == "overlap":
            vals = {str(v) for v in node.value}
            return s.apply(lambda xs: bool(None))
        raise ValueError(f"Operador lista desconhecido: {node.op}")

    def xǁPandasVisitorǁvisit_list_any__mutmut_31(self, node, df):
        """Suporta listas de strings em JSON. Converte None->[] e padroniza."""
        s = ensure_list_col(df[node.field])
        if node.op == "contains":
            x = str(node.value)
            return s.apply(lambda xs: any(x == str(i) for i in xs))
        if node.op == "in":
            vals = {
                str(v)
                for v in (
                    node.value
                    if isinstance(node.value, (list, tuple, set))
                    else [node.value]
                )
            }
            return s.apply(lambda xs: any(str(i) in vals for i in xs))
        if node.op == "overlap":
            vals = {str(v) for v in node.value}
            return s.apply(lambda xs: bool(vals.intersection(None)))
        raise ValueError(f"Operador lista desconhecido: {node.op}")

    def xǁPandasVisitorǁvisit_list_any__mutmut_32(self, node, df):
        """Suporta listas de strings em JSON. Converte None->[] e padroniza."""
        s = ensure_list_col(df[node.field])
        if node.op == "contains":
            x = str(node.value)
            return s.apply(lambda xs: any(x == str(i) for i in xs))
        if node.op == "in":
            vals = {
                str(v)
                for v in (
                    node.value
                    if isinstance(node.value, (list, tuple, set))
                    else [node.value]
                )
            }
            return s.apply(lambda xs: any(str(i) in vals for i in xs))
        if node.op == "overlap":
            vals = {str(v) for v in node.value}
            return s.apply(lambda xs: bool(vals.intersection({str(None) for i in xs})))
        raise ValueError(f"Operador lista desconhecido: {node.op}")

    def xǁPandasVisitorǁvisit_list_any__mutmut_33(self, node, df):
        """Suporta listas de strings em JSON. Converte None->[] e padroniza."""
        s = ensure_list_col(df[node.field])
        if node.op == "contains":
            x = str(node.value)
            return s.apply(lambda xs: any(x == str(i) for i in xs))
        if node.op == "in":
            vals = {
                str(v)
                for v in (
                    node.value
                    if isinstance(node.value, (list, tuple, set))
                    else [node.value]
                )
            }
            return s.apply(lambda xs: any(str(i) in vals for i in xs))
        if node.op == "overlap":
            vals = {str(v) for v in node.value}
            return s.apply(lambda xs: bool(vals.intersection({str(i) for i in xs})))
        raise ValueError(None)

    xǁPandasVisitorǁvisit_list_any__mutmut_mutants: ClassVar[MutantDict] = {  # type: ignore
        "xǁPandasVisitorǁvisit_list_any__mutmut_1": xǁPandasVisitorǁvisit_list_any__mutmut_1,
        "xǁPandasVisitorǁvisit_list_any__mutmut_2": xǁPandasVisitorǁvisit_list_any__mutmut_2,
        "xǁPandasVisitorǁvisit_list_any__mutmut_3": xǁPandasVisitorǁvisit_list_any__mutmut_3,
        "xǁPandasVisitorǁvisit_list_any__mutmut_4": xǁPandasVisitorǁvisit_list_any__mutmut_4,
        "xǁPandasVisitorǁvisit_list_any__mutmut_5": xǁPandasVisitorǁvisit_list_any__mutmut_5,
        "xǁPandasVisitorǁvisit_list_any__mutmut_6": xǁPandasVisitorǁvisit_list_any__mutmut_6,
        "xǁPandasVisitorǁvisit_list_any__mutmut_7": xǁPandasVisitorǁvisit_list_any__mutmut_7,
        "xǁPandasVisitorǁvisit_list_any__mutmut_8": xǁPandasVisitorǁvisit_list_any__mutmut_8,
        "xǁPandasVisitorǁvisit_list_any__mutmut_9": xǁPandasVisitorǁvisit_list_any__mutmut_9,
        "xǁPandasVisitorǁvisit_list_any__mutmut_10": xǁPandasVisitorǁvisit_list_any__mutmut_10,
        "xǁPandasVisitorǁvisit_list_any__mutmut_11": xǁPandasVisitorǁvisit_list_any__mutmut_11,
        "xǁPandasVisitorǁvisit_list_any__mutmut_12": xǁPandasVisitorǁvisit_list_any__mutmut_12,
        "xǁPandasVisitorǁvisit_list_any__mutmut_13": xǁPandasVisitorǁvisit_list_any__mutmut_13,
        "xǁPandasVisitorǁvisit_list_any__mutmut_14": xǁPandasVisitorǁvisit_list_any__mutmut_14,
        "xǁPandasVisitorǁvisit_list_any__mutmut_15": xǁPandasVisitorǁvisit_list_any__mutmut_15,
        "xǁPandasVisitorǁvisit_list_any__mutmut_16": xǁPandasVisitorǁvisit_list_any__mutmut_16,
        "xǁPandasVisitorǁvisit_list_any__mutmut_17": xǁPandasVisitorǁvisit_list_any__mutmut_17,
        "xǁPandasVisitorǁvisit_list_any__mutmut_18": xǁPandasVisitorǁvisit_list_any__mutmut_18,
        "xǁPandasVisitorǁvisit_list_any__mutmut_19": xǁPandasVisitorǁvisit_list_any__mutmut_19,
        "xǁPandasVisitorǁvisit_list_any__mutmut_20": xǁPandasVisitorǁvisit_list_any__mutmut_20,
        "xǁPandasVisitorǁvisit_list_any__mutmut_21": xǁPandasVisitorǁvisit_list_any__mutmut_21,
        "xǁPandasVisitorǁvisit_list_any__mutmut_22": xǁPandasVisitorǁvisit_list_any__mutmut_22,
        "xǁPandasVisitorǁvisit_list_any__mutmut_23": xǁPandasVisitorǁvisit_list_any__mutmut_23,
        "xǁPandasVisitorǁvisit_list_any__mutmut_24": xǁPandasVisitorǁvisit_list_any__mutmut_24,
        "xǁPandasVisitorǁvisit_list_any__mutmut_25": xǁPandasVisitorǁvisit_list_any__mutmut_25,
        "xǁPandasVisitorǁvisit_list_any__mutmut_26": xǁPandasVisitorǁvisit_list_any__mutmut_26,
        "xǁPandasVisitorǁvisit_list_any__mutmut_27": xǁPandasVisitorǁvisit_list_any__mutmut_27,
        "xǁPandasVisitorǁvisit_list_any__mutmut_28": xǁPandasVisitorǁvisit_list_any__mutmut_28,
        "xǁPandasVisitorǁvisit_list_any__mutmut_29": xǁPandasVisitorǁvisit_list_any__mutmut_29,
        "xǁPandasVisitorǁvisit_list_any__mutmut_30": xǁPandasVisitorǁvisit_list_any__mutmut_30,
        "xǁPandasVisitorǁvisit_list_any__mutmut_31": xǁPandasVisitorǁvisit_list_any__mutmut_31,
        "xǁPandasVisitorǁvisit_list_any__mutmut_32": xǁPandasVisitorǁvisit_list_any__mutmut_32,
        "xǁPandasVisitorǁvisit_list_any__mutmut_33": xǁPandasVisitorǁvisit_list_any__mutmut_33,
    }
    xǁPandasVisitorǁvisit_list_any__mutmut_orig.__name__ = (
        "xǁPandasVisitorǁvisit_list_any"
    )
