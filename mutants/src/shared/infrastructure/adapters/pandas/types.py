# infrastructure/utils/types.py
import pandas as pd
from pandas.api.types import is_datetime64_any_dtype
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


def ensure_datetime_col(s: pd.Series) -> pd.Series:
    args = [s]  # type: ignore
    kwargs = {}  # type: ignore
    return _mutmut_trampoline(
        x_ensure_datetime_col__mutmut_orig,
        x_ensure_datetime_col__mutmut_mutants,
        args,
        kwargs,
        None,
    )


def x_ensure_datetime_col__mutmut_orig(s: pd.Series) -> pd.Series:
    return (
        s
        if is_datetime64_any_dtype(s)
        else pd.to_datetime(s, errors="coerce", format="mixed")
    )


def x_ensure_datetime_col__mutmut_1(s: pd.Series) -> pd.Series:
    return (
        s
        if is_datetime64_any_dtype(None)
        else pd.to_datetime(s, errors="coerce", format="mixed")
    )


def x_ensure_datetime_col__mutmut_2(s: pd.Series) -> pd.Series:
    return (
        s
        if is_datetime64_any_dtype(s)
        else pd.to_datetime(None, errors="coerce", format="mixed")
    )


def x_ensure_datetime_col__mutmut_3(s: pd.Series) -> pd.Series:
    return (
        s
        if is_datetime64_any_dtype(s)
        else pd.to_datetime(s, errors=None, format="mixed")
    )


def x_ensure_datetime_col__mutmut_4(s: pd.Series) -> pd.Series:
    return (
        s
        if is_datetime64_any_dtype(s)
        else pd.to_datetime(s, errors="coerce", format=None)
    )


def x_ensure_datetime_col__mutmut_5(s: pd.Series) -> pd.Series:
    return (
        s
        if is_datetime64_any_dtype(s)
        else pd.to_datetime(errors="coerce", format="mixed")
    )


def x_ensure_datetime_col__mutmut_6(s: pd.Series) -> pd.Series:
    return s if is_datetime64_any_dtype(s) else pd.to_datetime(s, format="mixed")


def x_ensure_datetime_col__mutmut_7(s: pd.Series) -> pd.Series:
    return (
        s
        if is_datetime64_any_dtype(s)
        else pd.to_datetime(
            s,
            errors="coerce",
        )
    )


def x_ensure_datetime_col__mutmut_8(s: pd.Series) -> pd.Series:
    return (
        s
        if is_datetime64_any_dtype(s)
        else pd.to_datetime(s, errors="XXcoerceXX", format="mixed")
    )


def x_ensure_datetime_col__mutmut_9(s: pd.Series) -> pd.Series:
    return (
        s
        if is_datetime64_any_dtype(s)
        else pd.to_datetime(s, errors="COERCE", format="mixed")
    )


def x_ensure_datetime_col__mutmut_10(s: pd.Series) -> pd.Series:
    return (
        s
        if is_datetime64_any_dtype(s)
        else pd.to_datetime(s, errors="coerce", format="XXmixedXX")
    )


def x_ensure_datetime_col__mutmut_11(s: pd.Series) -> pd.Series:
    return (
        s
        if is_datetime64_any_dtype(s)
        else pd.to_datetime(s, errors="coerce", format="MIXED")
    )


x_ensure_datetime_col__mutmut_mutants: ClassVar[MutantDict] = {  # type: ignore
    "x_ensure_datetime_col__mutmut_1": x_ensure_datetime_col__mutmut_1,
    "x_ensure_datetime_col__mutmut_2": x_ensure_datetime_col__mutmut_2,
    "x_ensure_datetime_col__mutmut_3": x_ensure_datetime_col__mutmut_3,
    "x_ensure_datetime_col__mutmut_4": x_ensure_datetime_col__mutmut_4,
    "x_ensure_datetime_col__mutmut_5": x_ensure_datetime_col__mutmut_5,
    "x_ensure_datetime_col__mutmut_6": x_ensure_datetime_col__mutmut_6,
    "x_ensure_datetime_col__mutmut_7": x_ensure_datetime_col__mutmut_7,
    "x_ensure_datetime_col__mutmut_8": x_ensure_datetime_col__mutmut_8,
    "x_ensure_datetime_col__mutmut_9": x_ensure_datetime_col__mutmut_9,
    "x_ensure_datetime_col__mutmut_10": x_ensure_datetime_col__mutmut_10,
    "x_ensure_datetime_col__mutmut_11": x_ensure_datetime_col__mutmut_11,
}
x_ensure_datetime_col__mutmut_orig.__name__ = "x_ensure_datetime_col"


def ensure_list_col(s: pd.Series) -> pd.Series:
    args = [s]  # type: ignore
    kwargs = {}  # type: ignore
    return _mutmut_trampoline(
        x_ensure_list_col__mutmut_orig,
        x_ensure_list_col__mutmut_mutants,
        args,
        kwargs,
        None,
    )


def x_ensure_list_col__mutmut_orig(s: pd.Series) -> pd.Series:
    return s.apply(
        lambda v: v if isinstance(v, (list, tuple)) else ([] if v is None else [v])
    )


def x_ensure_list_col__mutmut_1(s: pd.Series) -> pd.Series:
    return s.apply(None)


def x_ensure_list_col__mutmut_2(s: pd.Series) -> pd.Series:
    return s.apply(lambda v: None)


def x_ensure_list_col__mutmut_3(s: pd.Series) -> pd.Series:
    return s.apply(
        lambda v: v if isinstance(v, (list, tuple)) else ([] if v is not None else [v])
    )


x_ensure_list_col__mutmut_mutants: ClassVar[MutantDict] = {  # type: ignore
    "x_ensure_list_col__mutmut_1": x_ensure_list_col__mutmut_1,
    "x_ensure_list_col__mutmut_2": x_ensure_list_col__mutmut_2,
    "x_ensure_list_col__mutmut_3": x_ensure_list_col__mutmut_3,
}
x_ensure_list_col__mutmut_orig.__name__ = "x_ensure_list_col"
