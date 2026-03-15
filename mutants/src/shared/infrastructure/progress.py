import time
from typing import List, Any
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


class ProgressReporter:
    """
    SOTA Progress Reporter that maintains the legacy formatting style
    while providing a clean, object-oriented API for modern DDD applications.
    """

    def __init__(self, total: int):
        args = [total]  # type: ignore
        kwargs = {}  # type: ignore
        return _mutmut_trampoline(
            object.__getattribute__(self, "xǁProgressReporterǁ__init____mutmut_orig"),
            object.__getattribute__(
                self, "xǁProgressReporterǁ__init____mutmut_mutants"
            ),
            args,
            kwargs,
            self,
        )

    def xǁProgressReporterǁ__init____mutmut_orig(self, total: int):
        self.total = total
        self.start_time = time.monotonic()

    def xǁProgressReporterǁ__init____mutmut_1(self, total: int):
        self.total = None
        self.start_time = time.monotonic()

    def xǁProgressReporterǁ__init____mutmut_2(self, total: int):
        self.total = total
        self.start_time = None

    xǁProgressReporterǁ__init____mutmut_mutants: ClassVar[MutantDict] = {  # type: ignore
        "xǁProgressReporterǁ__init____mutmut_1": xǁProgressReporterǁ__init____mutmut_1,
        "xǁProgressReporterǁ__init____mutmut_2": xǁProgressReporterǁ__init____mutmut_2,
    }
    xǁProgressReporterǁ__init____mutmut_orig.__name__ = "xǁProgressReporterǁ__init__"

    def _format_seconds(self, seconds: float) -> str:
        args = [seconds]  # type: ignore
        kwargs = {}  # type: ignore
        return _mutmut_trampoline(
            object.__getattribute__(
                self, "xǁProgressReporterǁ_format_seconds__mutmut_orig"
            ),
            object.__getattribute__(
                self, "xǁProgressReporterǁ_format_seconds__mutmut_mutants"
            ),
            args,
            kwargs,
            self,
        )

    def xǁProgressReporterǁ_format_seconds__mutmut_orig(self, seconds: float) -> str:
        hours, remainder = divmod(int(seconds), 3600)
        minutes, seconds_int = divmod(remainder, 60)
        return f"{int(hours)}h{int(minutes):02}m{int(seconds_int):02}s"

    def xǁProgressReporterǁ_format_seconds__mutmut_1(self, seconds: float) -> str:
        hours, remainder = None
        minutes, seconds_int = divmod(remainder, 60)
        return f"{int(hours)}h{int(minutes):02}m{int(seconds_int):02}s"

    def xǁProgressReporterǁ_format_seconds__mutmut_2(self, seconds: float) -> str:
        hours, remainder = divmod(None, 3600)
        minutes, seconds_int = divmod(remainder, 60)
        return f"{int(hours)}h{int(minutes):02}m{int(seconds_int):02}s"

    def xǁProgressReporterǁ_format_seconds__mutmut_3(self, seconds: float) -> str:
        hours, remainder = divmod(int(seconds), None)
        minutes, seconds_int = divmod(remainder, 60)
        return f"{int(hours)}h{int(minutes):02}m{int(seconds_int):02}s"

    def xǁProgressReporterǁ_format_seconds__mutmut_4(self, seconds: float) -> str:
        hours, remainder = divmod(3600)
        minutes, seconds_int = divmod(remainder, 60)
        return f"{int(hours)}h{int(minutes):02}m{int(seconds_int):02}s"

    def xǁProgressReporterǁ_format_seconds__mutmut_5(self, seconds: float) -> str:
        hours, remainder = divmod(
            int(seconds),
        )
        minutes, seconds_int = divmod(remainder, 60)
        return f"{int(hours)}h{int(minutes):02}m{int(seconds_int):02}s"

    def xǁProgressReporterǁ_format_seconds__mutmut_6(self, seconds: float) -> str:
        hours, remainder = divmod(int(None), 3600)
        minutes, seconds_int = divmod(remainder, 60)
        return f"{int(hours)}h{int(minutes):02}m{int(seconds_int):02}s"

    def xǁProgressReporterǁ_format_seconds__mutmut_7(self, seconds: float) -> str:
        hours, remainder = divmod(int(seconds), 3601)
        minutes, seconds_int = divmod(remainder, 60)
        return f"{int(hours)}h{int(minutes):02}m{int(seconds_int):02}s"

    def xǁProgressReporterǁ_format_seconds__mutmut_8(self, seconds: float) -> str:
        hours, remainder = divmod(int(seconds), 3600)
        minutes, seconds_int = None
        return f"{int(hours)}h{int(minutes):02}m{int(seconds_int):02}s"

    def xǁProgressReporterǁ_format_seconds__mutmut_9(self, seconds: float) -> str:
        hours, remainder = divmod(int(seconds), 3600)
        minutes, seconds_int = divmod(None, 60)
        return f"{int(hours)}h{int(minutes):02}m{int(seconds_int):02}s"

    def xǁProgressReporterǁ_format_seconds__mutmut_10(self, seconds: float) -> str:
        hours, remainder = divmod(int(seconds), 3600)
        minutes, seconds_int = divmod(remainder, None)
        return f"{int(hours)}h{int(minutes):02}m{int(seconds_int):02}s"

    def xǁProgressReporterǁ_format_seconds__mutmut_11(self, seconds: float) -> str:
        hours, remainder = divmod(int(seconds), 3600)
        minutes, seconds_int = divmod(60)
        return f"{int(hours)}h{int(minutes):02}m{int(seconds_int):02}s"

    def xǁProgressReporterǁ_format_seconds__mutmut_12(self, seconds: float) -> str:
        hours, remainder = divmod(int(seconds), 3600)
        minutes, seconds_int = divmod(
            remainder,
        )
        return f"{int(hours)}h{int(minutes):02}m{int(seconds_int):02}s"

    def xǁProgressReporterǁ_format_seconds__mutmut_13(self, seconds: float) -> str:
        hours, remainder = divmod(int(seconds), 3600)
        minutes, seconds_int = divmod(remainder, 61)
        return f"{int(hours)}h{int(minutes):02}m{int(seconds_int):02}s"

    def xǁProgressReporterǁ_format_seconds__mutmut_14(self, seconds: float) -> str:
        hours, remainder = divmod(int(seconds), 3600)
        minutes, seconds_int = divmod(remainder, 60)
        return f"{int(None)}h{int(minutes):02}m{int(seconds_int):02}s"

    def xǁProgressReporterǁ_format_seconds__mutmut_15(self, seconds: float) -> str:
        hours, remainder = divmod(int(seconds), 3600)
        minutes, seconds_int = divmod(remainder, 60)
        return f"{int(hours)}h{int(None):02}m{int(seconds_int):02}s"

    def xǁProgressReporterǁ_format_seconds__mutmut_16(self, seconds: float) -> str:
        hours, remainder = divmod(int(seconds), 3600)
        minutes, seconds_int = divmod(remainder, 60)
        return f"{int(hours)}h{int(minutes):02}m{int(None):02}s"

    xǁProgressReporterǁ_format_seconds__mutmut_mutants: ClassVar[MutantDict] = {  # type: ignore
        "xǁProgressReporterǁ_format_seconds__mutmut_1": xǁProgressReporterǁ_format_seconds__mutmut_1,
        "xǁProgressReporterǁ_format_seconds__mutmut_2": xǁProgressReporterǁ_format_seconds__mutmut_2,
        "xǁProgressReporterǁ_format_seconds__mutmut_3": xǁProgressReporterǁ_format_seconds__mutmut_3,
        "xǁProgressReporterǁ_format_seconds__mutmut_4": xǁProgressReporterǁ_format_seconds__mutmut_4,
        "xǁProgressReporterǁ_format_seconds__mutmut_5": xǁProgressReporterǁ_format_seconds__mutmut_5,
        "xǁProgressReporterǁ_format_seconds__mutmut_6": xǁProgressReporterǁ_format_seconds__mutmut_6,
        "xǁProgressReporterǁ_format_seconds__mutmut_7": xǁProgressReporterǁ_format_seconds__mutmut_7,
        "xǁProgressReporterǁ_format_seconds__mutmut_8": xǁProgressReporterǁ_format_seconds__mutmut_8,
        "xǁProgressReporterǁ_format_seconds__mutmut_9": xǁProgressReporterǁ_format_seconds__mutmut_9,
        "xǁProgressReporterǁ_format_seconds__mutmut_10": xǁProgressReporterǁ_format_seconds__mutmut_10,
        "xǁProgressReporterǁ_format_seconds__mutmut_11": xǁProgressReporterǁ_format_seconds__mutmut_11,
        "xǁProgressReporterǁ_format_seconds__mutmut_12": xǁProgressReporterǁ_format_seconds__mutmut_12,
        "xǁProgressReporterǁ_format_seconds__mutmut_13": xǁProgressReporterǁ_format_seconds__mutmut_13,
        "xǁProgressReporterǁ_format_seconds__mutmut_14": xǁProgressReporterǁ_format_seconds__mutmut_14,
        "xǁProgressReporterǁ_format_seconds__mutmut_15": xǁProgressReporterǁ_format_seconds__mutmut_15,
        "xǁProgressReporterǁ_format_seconds__mutmut_16": xǁProgressReporterǁ_format_seconds__mutmut_16,
    }
    xǁProgressReporterǁ_format_seconds__mutmut_orig.__name__ = (
        "xǁProgressReporterǁ_format_seconds"
    )

    def get_formatted_progress(
        self, current_index: int, extra_info: List[Any] = None
    ) -> str:
        args = [current_index, extra_info]  # type: ignore
        kwargs = {}  # type: ignore
        return _mutmut_trampoline(
            object.__getattribute__(
                self, "xǁProgressReporterǁget_formatted_progress__mutmut_orig"
            ),
            object.__getattribute__(
                self, "xǁProgressReporterǁget_formatted_progress__mutmut_mutants"
            ),
            args,
            kwargs,
            self,
        )

    def xǁProgressReporterǁget_formatted_progress__mutmut_orig(
        self, current_index: int, extra_info: List[Any] = None
    ) -> str:
        """
        Calculates metrics and returns the legacy-style formatted string.
        Format: Percentage% (Done+Remaining), AvgTimes per item, Total = Elapsed + Remaining Info
        """
        completed = current_index + 1
        remaining = self.total - completed
        percentage = completed / self.total if self.total > 0 else 0

        elapsed = time.monotonic() - self.start_time
        avg_time = elapsed / completed if completed > 0 else 0
        remaining_time = remaining * avg_time
        total_estimated = elapsed + remaining_time

        progress_str = (
            f"{percentage:.2%} ({completed}+{remaining}), "
            f"{avg_time:.4f}s/item, "
            f"{self._format_seconds(total_estimated)} = "
            f"{self._format_seconds(elapsed)} + "
            f"{self._format_seconds(remaining_time)}"
        )

        if extra_info:
            extra_str = " ".join(map(str, extra_info))
            return f"{progress_str} {extra_str}"

        return progress_str

    def xǁProgressReporterǁget_formatted_progress__mutmut_1(
        self, current_index: int, extra_info: List[Any] = None
    ) -> str:
        """
        Calculates metrics and returns the legacy-style formatted string.
        Format: Percentage% (Done+Remaining), AvgTimes per item, Total = Elapsed + Remaining Info
        """
        completed = None
        remaining = self.total - completed
        percentage = completed / self.total if self.total > 0 else 0

        elapsed = time.monotonic() - self.start_time
        avg_time = elapsed / completed if completed > 0 else 0
        remaining_time = remaining * avg_time
        total_estimated = elapsed + remaining_time

        progress_str = (
            f"{percentage:.2%} ({completed}+{remaining}), "
            f"{avg_time:.4f}s/item, "
            f"{self._format_seconds(total_estimated)} = "
            f"{self._format_seconds(elapsed)} + "
            f"{self._format_seconds(remaining_time)}"
        )

        if extra_info:
            extra_str = " ".join(map(str, extra_info))
            return f"{progress_str} {extra_str}"

        return progress_str

    def xǁProgressReporterǁget_formatted_progress__mutmut_2(
        self, current_index: int, extra_info: List[Any] = None
    ) -> str:
        """
        Calculates metrics and returns the legacy-style formatted string.
        Format: Percentage% (Done+Remaining), AvgTimes per item, Total = Elapsed + Remaining Info
        """
        completed = current_index - 1
        remaining = self.total - completed
        percentage = completed / self.total if self.total > 0 else 0

        elapsed = time.monotonic() - self.start_time
        avg_time = elapsed / completed if completed > 0 else 0
        remaining_time = remaining * avg_time
        total_estimated = elapsed + remaining_time

        progress_str = (
            f"{percentage:.2%} ({completed}+{remaining}), "
            f"{avg_time:.4f}s/item, "
            f"{self._format_seconds(total_estimated)} = "
            f"{self._format_seconds(elapsed)} + "
            f"{self._format_seconds(remaining_time)}"
        )

        if extra_info:
            extra_str = " ".join(map(str, extra_info))
            return f"{progress_str} {extra_str}"

        return progress_str

    def xǁProgressReporterǁget_formatted_progress__mutmut_3(
        self, current_index: int, extra_info: List[Any] = None
    ) -> str:
        """
        Calculates metrics and returns the legacy-style formatted string.
        Format: Percentage% (Done+Remaining), AvgTimes per item, Total = Elapsed + Remaining Info
        """
        completed = current_index + 2
        remaining = self.total - completed
        percentage = completed / self.total if self.total > 0 else 0

        elapsed = time.monotonic() - self.start_time
        avg_time = elapsed / completed if completed > 0 else 0
        remaining_time = remaining * avg_time
        total_estimated = elapsed + remaining_time

        progress_str = (
            f"{percentage:.2%} ({completed}+{remaining}), "
            f"{avg_time:.4f}s/item, "
            f"{self._format_seconds(total_estimated)} = "
            f"{self._format_seconds(elapsed)} + "
            f"{self._format_seconds(remaining_time)}"
        )

        if extra_info:
            extra_str = " ".join(map(str, extra_info))
            return f"{progress_str} {extra_str}"

        return progress_str

    def xǁProgressReporterǁget_formatted_progress__mutmut_4(
        self, current_index: int, extra_info: List[Any] = None
    ) -> str:
        """
        Calculates metrics and returns the legacy-style formatted string.
        Format: Percentage% (Done+Remaining), AvgTimes per item, Total = Elapsed + Remaining Info
        """
        completed = current_index + 1
        remaining = None
        percentage = completed / self.total if self.total > 0 else 0

        elapsed = time.monotonic() - self.start_time
        avg_time = elapsed / completed if completed > 0 else 0
        remaining_time = remaining * avg_time
        total_estimated = elapsed + remaining_time

        progress_str = (
            f"{percentage:.2%} ({completed}+{remaining}), "
            f"{avg_time:.4f}s/item, "
            f"{self._format_seconds(total_estimated)} = "
            f"{self._format_seconds(elapsed)} + "
            f"{self._format_seconds(remaining_time)}"
        )

        if extra_info:
            extra_str = " ".join(map(str, extra_info))
            return f"{progress_str} {extra_str}"

        return progress_str

    def xǁProgressReporterǁget_formatted_progress__mutmut_5(
        self, current_index: int, extra_info: List[Any] = None
    ) -> str:
        """
        Calculates metrics and returns the legacy-style formatted string.
        Format: Percentage% (Done+Remaining), AvgTimes per item, Total = Elapsed + Remaining Info
        """
        completed = current_index + 1
        remaining = self.total + completed
        percentage = completed / self.total if self.total > 0 else 0

        elapsed = time.monotonic() - self.start_time
        avg_time = elapsed / completed if completed > 0 else 0
        remaining_time = remaining * avg_time
        total_estimated = elapsed + remaining_time

        progress_str = (
            f"{percentage:.2%} ({completed}+{remaining}), "
            f"{avg_time:.4f}s/item, "
            f"{self._format_seconds(total_estimated)} = "
            f"{self._format_seconds(elapsed)} + "
            f"{self._format_seconds(remaining_time)}"
        )

        if extra_info:
            extra_str = " ".join(map(str, extra_info))
            return f"{progress_str} {extra_str}"

        return progress_str

    def xǁProgressReporterǁget_formatted_progress__mutmut_6(
        self, current_index: int, extra_info: List[Any] = None
    ) -> str:
        """
        Calculates metrics and returns the legacy-style formatted string.
        Format: Percentage% (Done+Remaining), AvgTimes per item, Total = Elapsed + Remaining Info
        """
        completed = current_index + 1
        remaining = self.total - completed
        percentage = None

        elapsed = time.monotonic() - self.start_time
        avg_time = elapsed / completed if completed > 0 else 0
        remaining_time = remaining * avg_time
        total_estimated = elapsed + remaining_time

        progress_str = (
            f"{percentage:.2%} ({completed}+{remaining}), "
            f"{avg_time:.4f}s/item, "
            f"{self._format_seconds(total_estimated)} = "
            f"{self._format_seconds(elapsed)} + "
            f"{self._format_seconds(remaining_time)}"
        )

        if extra_info:
            extra_str = " ".join(map(str, extra_info))
            return f"{progress_str} {extra_str}"

        return progress_str

    def xǁProgressReporterǁget_formatted_progress__mutmut_7(
        self, current_index: int, extra_info: List[Any] = None
    ) -> str:
        """
        Calculates metrics and returns the legacy-style formatted string.
        Format: Percentage% (Done+Remaining), AvgTimes per item, Total = Elapsed + Remaining Info
        """
        completed = current_index + 1
        remaining = self.total - completed
        percentage = completed * self.total if self.total > 0 else 0

        elapsed = time.monotonic() - self.start_time
        avg_time = elapsed / completed if completed > 0 else 0
        remaining_time = remaining * avg_time
        total_estimated = elapsed + remaining_time

        progress_str = (
            f"{percentage:.2%} ({completed}+{remaining}), "
            f"{avg_time:.4f}s/item, "
            f"{self._format_seconds(total_estimated)} = "
            f"{self._format_seconds(elapsed)} + "
            f"{self._format_seconds(remaining_time)}"
        )

        if extra_info:
            extra_str = " ".join(map(str, extra_info))
            return f"{progress_str} {extra_str}"

        return progress_str

    def xǁProgressReporterǁget_formatted_progress__mutmut_8(
        self, current_index: int, extra_info: List[Any] = None
    ) -> str:
        """
        Calculates metrics and returns the legacy-style formatted string.
        Format: Percentage% (Done+Remaining), AvgTimes per item, Total = Elapsed + Remaining Info
        """
        completed = current_index + 1
        remaining = self.total - completed
        percentage = completed / self.total if self.total >= 0 else 0

        elapsed = time.monotonic() - self.start_time
        avg_time = elapsed / completed if completed > 0 else 0
        remaining_time = remaining * avg_time
        total_estimated = elapsed + remaining_time

        progress_str = (
            f"{percentage:.2%} ({completed}+{remaining}), "
            f"{avg_time:.4f}s/item, "
            f"{self._format_seconds(total_estimated)} = "
            f"{self._format_seconds(elapsed)} + "
            f"{self._format_seconds(remaining_time)}"
        )

        if extra_info:
            extra_str = " ".join(map(str, extra_info))
            return f"{progress_str} {extra_str}"

        return progress_str

    def xǁProgressReporterǁget_formatted_progress__mutmut_9(
        self, current_index: int, extra_info: List[Any] = None
    ) -> str:
        """
        Calculates metrics and returns the legacy-style formatted string.
        Format: Percentage% (Done+Remaining), AvgTimes per item, Total = Elapsed + Remaining Info
        """
        completed = current_index + 1
        remaining = self.total - completed
        percentage = completed / self.total if self.total > 1 else 0

        elapsed = time.monotonic() - self.start_time
        avg_time = elapsed / completed if completed > 0 else 0
        remaining_time = remaining * avg_time
        total_estimated = elapsed + remaining_time

        progress_str = (
            f"{percentage:.2%} ({completed}+{remaining}), "
            f"{avg_time:.4f}s/item, "
            f"{self._format_seconds(total_estimated)} = "
            f"{self._format_seconds(elapsed)} + "
            f"{self._format_seconds(remaining_time)}"
        )

        if extra_info:
            extra_str = " ".join(map(str, extra_info))
            return f"{progress_str} {extra_str}"

        return progress_str

    def xǁProgressReporterǁget_formatted_progress__mutmut_10(
        self, current_index: int, extra_info: List[Any] = None
    ) -> str:
        """
        Calculates metrics and returns the legacy-style formatted string.
        Format: Percentage% (Done+Remaining), AvgTimes per item, Total = Elapsed + Remaining Info
        """
        completed = current_index + 1
        remaining = self.total - completed
        percentage = completed / self.total if self.total > 0 else 1

        elapsed = time.monotonic() - self.start_time
        avg_time = elapsed / completed if completed > 0 else 0
        remaining_time = remaining * avg_time
        total_estimated = elapsed + remaining_time

        progress_str = (
            f"{percentage:.2%} ({completed}+{remaining}), "
            f"{avg_time:.4f}s/item, "
            f"{self._format_seconds(total_estimated)} = "
            f"{self._format_seconds(elapsed)} + "
            f"{self._format_seconds(remaining_time)}"
        )

        if extra_info:
            extra_str = " ".join(map(str, extra_info))
            return f"{progress_str} {extra_str}"

        return progress_str

    def xǁProgressReporterǁget_formatted_progress__mutmut_11(
        self, current_index: int, extra_info: List[Any] = None
    ) -> str:
        """
        Calculates metrics and returns the legacy-style formatted string.
        Format: Percentage% (Done+Remaining), AvgTimes per item, Total = Elapsed + Remaining Info
        """
        completed = current_index + 1
        remaining = self.total - completed
        percentage = completed / self.total if self.total > 0 else 0

        elapsed = None
        avg_time = elapsed / completed if completed > 0 else 0
        remaining_time = remaining * avg_time
        total_estimated = elapsed + remaining_time

        progress_str = (
            f"{percentage:.2%} ({completed}+{remaining}), "
            f"{avg_time:.4f}s/item, "
            f"{self._format_seconds(total_estimated)} = "
            f"{self._format_seconds(elapsed)} + "
            f"{self._format_seconds(remaining_time)}"
        )

        if extra_info:
            extra_str = " ".join(map(str, extra_info))
            return f"{progress_str} {extra_str}"

        return progress_str

    def xǁProgressReporterǁget_formatted_progress__mutmut_12(
        self, current_index: int, extra_info: List[Any] = None
    ) -> str:
        """
        Calculates metrics and returns the legacy-style formatted string.
        Format: Percentage% (Done+Remaining), AvgTimes per item, Total = Elapsed + Remaining Info
        """
        completed = current_index + 1
        remaining = self.total - completed
        percentage = completed / self.total if self.total > 0 else 0

        elapsed = time.monotonic() + self.start_time
        avg_time = elapsed / completed if completed > 0 else 0
        remaining_time = remaining * avg_time
        total_estimated = elapsed + remaining_time

        progress_str = (
            f"{percentage:.2%} ({completed}+{remaining}), "
            f"{avg_time:.4f}s/item, "
            f"{self._format_seconds(total_estimated)} = "
            f"{self._format_seconds(elapsed)} + "
            f"{self._format_seconds(remaining_time)}"
        )

        if extra_info:
            extra_str = " ".join(map(str, extra_info))
            return f"{progress_str} {extra_str}"

        return progress_str

    def xǁProgressReporterǁget_formatted_progress__mutmut_13(
        self, current_index: int, extra_info: List[Any] = None
    ) -> str:
        """
        Calculates metrics and returns the legacy-style formatted string.
        Format: Percentage% (Done+Remaining), AvgTimes per item, Total = Elapsed + Remaining Info
        """
        completed = current_index + 1
        remaining = self.total - completed
        percentage = completed / self.total if self.total > 0 else 0

        elapsed = time.monotonic() - self.start_time
        avg_time = None
        remaining_time = remaining * avg_time
        total_estimated = elapsed + remaining_time

        progress_str = (
            f"{percentage:.2%} ({completed}+{remaining}), "
            f"{avg_time:.4f}s/item, "
            f"{self._format_seconds(total_estimated)} = "
            f"{self._format_seconds(elapsed)} + "
            f"{self._format_seconds(remaining_time)}"
        )

        if extra_info:
            extra_str = " ".join(map(str, extra_info))
            return f"{progress_str} {extra_str}"

        return progress_str

    def xǁProgressReporterǁget_formatted_progress__mutmut_14(
        self, current_index: int, extra_info: List[Any] = None
    ) -> str:
        """
        Calculates metrics and returns the legacy-style formatted string.
        Format: Percentage% (Done+Remaining), AvgTimes per item, Total = Elapsed + Remaining Info
        """
        completed = current_index + 1
        remaining = self.total - completed
        percentage = completed / self.total if self.total > 0 else 0

        elapsed = time.monotonic() - self.start_time
        avg_time = elapsed * completed if completed > 0 else 0
        remaining_time = remaining * avg_time
        total_estimated = elapsed + remaining_time

        progress_str = (
            f"{percentage:.2%} ({completed}+{remaining}), "
            f"{avg_time:.4f}s/item, "
            f"{self._format_seconds(total_estimated)} = "
            f"{self._format_seconds(elapsed)} + "
            f"{self._format_seconds(remaining_time)}"
        )

        if extra_info:
            extra_str = " ".join(map(str, extra_info))
            return f"{progress_str} {extra_str}"

        return progress_str

    def xǁProgressReporterǁget_formatted_progress__mutmut_15(
        self, current_index: int, extra_info: List[Any] = None
    ) -> str:
        """
        Calculates metrics and returns the legacy-style formatted string.
        Format: Percentage% (Done+Remaining), AvgTimes per item, Total = Elapsed + Remaining Info
        """
        completed = current_index + 1
        remaining = self.total - completed
        percentage = completed / self.total if self.total > 0 else 0

        elapsed = time.monotonic() - self.start_time
        avg_time = elapsed / completed if completed >= 0 else 0
        remaining_time = remaining * avg_time
        total_estimated = elapsed + remaining_time

        progress_str = (
            f"{percentage:.2%} ({completed}+{remaining}), "
            f"{avg_time:.4f}s/item, "
            f"{self._format_seconds(total_estimated)} = "
            f"{self._format_seconds(elapsed)} + "
            f"{self._format_seconds(remaining_time)}"
        )

        if extra_info:
            extra_str = " ".join(map(str, extra_info))
            return f"{progress_str} {extra_str}"

        return progress_str

    def xǁProgressReporterǁget_formatted_progress__mutmut_16(
        self, current_index: int, extra_info: List[Any] = None
    ) -> str:
        """
        Calculates metrics and returns the legacy-style formatted string.
        Format: Percentage% (Done+Remaining), AvgTimes per item, Total = Elapsed + Remaining Info
        """
        completed = current_index + 1
        remaining = self.total - completed
        percentage = completed / self.total if self.total > 0 else 0

        elapsed = time.monotonic() - self.start_time
        avg_time = elapsed / completed if completed > 1 else 0
        remaining_time = remaining * avg_time
        total_estimated = elapsed + remaining_time

        progress_str = (
            f"{percentage:.2%} ({completed}+{remaining}), "
            f"{avg_time:.4f}s/item, "
            f"{self._format_seconds(total_estimated)} = "
            f"{self._format_seconds(elapsed)} + "
            f"{self._format_seconds(remaining_time)}"
        )

        if extra_info:
            extra_str = " ".join(map(str, extra_info))
            return f"{progress_str} {extra_str}"

        return progress_str

    def xǁProgressReporterǁget_formatted_progress__mutmut_17(
        self, current_index: int, extra_info: List[Any] = None
    ) -> str:
        """
        Calculates metrics and returns the legacy-style formatted string.
        Format: Percentage% (Done+Remaining), AvgTimes per item, Total = Elapsed + Remaining Info
        """
        completed = current_index + 1
        remaining = self.total - completed
        percentage = completed / self.total if self.total > 0 else 0

        elapsed = time.monotonic() - self.start_time
        avg_time = elapsed / completed if completed > 0 else 1
        remaining_time = remaining * avg_time
        total_estimated = elapsed + remaining_time

        progress_str = (
            f"{percentage:.2%} ({completed}+{remaining}), "
            f"{avg_time:.4f}s/item, "
            f"{self._format_seconds(total_estimated)} = "
            f"{self._format_seconds(elapsed)} + "
            f"{self._format_seconds(remaining_time)}"
        )

        if extra_info:
            extra_str = " ".join(map(str, extra_info))
            return f"{progress_str} {extra_str}"

        return progress_str

    def xǁProgressReporterǁget_formatted_progress__mutmut_18(
        self, current_index: int, extra_info: List[Any] = None
    ) -> str:
        """
        Calculates metrics and returns the legacy-style formatted string.
        Format: Percentage% (Done+Remaining), AvgTimes per item, Total = Elapsed + Remaining Info
        """
        completed = current_index + 1
        remaining = self.total - completed
        percentage = completed / self.total if self.total > 0 else 0

        elapsed = time.monotonic() - self.start_time
        avg_time = elapsed / completed if completed > 0 else 0
        remaining_time = None
        total_estimated = elapsed + remaining_time

        progress_str = (
            f"{percentage:.2%} ({completed}+{remaining}), "
            f"{avg_time:.4f}s/item, "
            f"{self._format_seconds(total_estimated)} = "
            f"{self._format_seconds(elapsed)} + "
            f"{self._format_seconds(remaining_time)}"
        )

        if extra_info:
            extra_str = " ".join(map(str, extra_info))
            return f"{progress_str} {extra_str}"

        return progress_str

    def xǁProgressReporterǁget_formatted_progress__mutmut_19(
        self, current_index: int, extra_info: List[Any] = None
    ) -> str:
        """
        Calculates metrics and returns the legacy-style formatted string.
        Format: Percentage% (Done+Remaining), AvgTimes per item, Total = Elapsed + Remaining Info
        """
        completed = current_index + 1
        remaining = self.total - completed
        percentage = completed / self.total if self.total > 0 else 0

        elapsed = time.monotonic() - self.start_time
        avg_time = elapsed / completed if completed > 0 else 0
        remaining_time = remaining / avg_time
        total_estimated = elapsed + remaining_time

        progress_str = (
            f"{percentage:.2%} ({completed}+{remaining}), "
            f"{avg_time:.4f}s/item, "
            f"{self._format_seconds(total_estimated)} = "
            f"{self._format_seconds(elapsed)} + "
            f"{self._format_seconds(remaining_time)}"
        )

        if extra_info:
            extra_str = " ".join(map(str, extra_info))
            return f"{progress_str} {extra_str}"

        return progress_str

    def xǁProgressReporterǁget_formatted_progress__mutmut_20(
        self, current_index: int, extra_info: List[Any] = None
    ) -> str:
        """
        Calculates metrics and returns the legacy-style formatted string.
        Format: Percentage% (Done+Remaining), AvgTimes per item, Total = Elapsed + Remaining Info
        """
        completed = current_index + 1
        remaining = self.total - completed
        percentage = completed / self.total if self.total > 0 else 0

        elapsed = time.monotonic() - self.start_time
        avg_time = elapsed / completed if completed > 0 else 0
        remaining_time = remaining * avg_time
        total_estimated = None

        progress_str = (
            f"{percentage:.2%} ({completed}+{remaining}), "
            f"{avg_time:.4f}s/item, "
            f"{self._format_seconds(total_estimated)} = "
            f"{self._format_seconds(elapsed)} + "
            f"{self._format_seconds(remaining_time)}"
        )

        if extra_info:
            extra_str = " ".join(map(str, extra_info))
            return f"{progress_str} {extra_str}"

        return progress_str

    def xǁProgressReporterǁget_formatted_progress__mutmut_21(
        self, current_index: int, extra_info: List[Any] = None
    ) -> str:
        """
        Calculates metrics and returns the legacy-style formatted string.
        Format: Percentage% (Done+Remaining), AvgTimes per item, Total = Elapsed + Remaining Info
        """
        completed = current_index + 1
        remaining = self.total - completed
        percentage = completed / self.total if self.total > 0 else 0

        elapsed = time.monotonic() - self.start_time
        avg_time = elapsed / completed if completed > 0 else 0
        remaining_time = remaining * avg_time
        total_estimated = elapsed - remaining_time

        progress_str = (
            f"{percentage:.2%} ({completed}+{remaining}), "
            f"{avg_time:.4f}s/item, "
            f"{self._format_seconds(total_estimated)} = "
            f"{self._format_seconds(elapsed)} + "
            f"{self._format_seconds(remaining_time)}"
        )

        if extra_info:
            extra_str = " ".join(map(str, extra_info))
            return f"{progress_str} {extra_str}"

        return progress_str

    def xǁProgressReporterǁget_formatted_progress__mutmut_22(
        self, current_index: int, extra_info: List[Any] = None
    ) -> str:
        """
        Calculates metrics and returns the legacy-style formatted string.
        Format: Percentage% (Done+Remaining), AvgTimes per item, Total = Elapsed + Remaining Info
        """
        completed = current_index + 1
        remaining = self.total - completed
        percentage = completed / self.total if self.total > 0 else 0

        elapsed = time.monotonic() - self.start_time
        avg_time = elapsed / completed if completed > 0 else 0
        remaining_time = remaining * avg_time
        total_estimated = elapsed + remaining_time

        progress_str = None

        if extra_info:
            extra_str = " ".join(map(str, extra_info))
            return f"{progress_str} {extra_str}"

        return progress_str

    def xǁProgressReporterǁget_formatted_progress__mutmut_23(
        self, current_index: int, extra_info: List[Any] = None
    ) -> str:
        """
        Calculates metrics and returns the legacy-style formatted string.
        Format: Percentage% (Done+Remaining), AvgTimes per item, Total = Elapsed + Remaining Info
        """
        completed = current_index + 1
        remaining = self.total - completed
        percentage = completed / self.total if self.total > 0 else 0

        elapsed = time.monotonic() - self.start_time
        avg_time = elapsed / completed if completed > 0 else 0
        remaining_time = remaining * avg_time
        total_estimated = elapsed + remaining_time

        progress_str = (
            f"{percentage:.2%} ({completed}+{remaining}), "
            f"{avg_time:.4f}s/item, "
            f"{self._format_seconds(None)} = "
            f"{self._format_seconds(elapsed)} + "
            f"{self._format_seconds(remaining_time)}"
        )

        if extra_info:
            extra_str = " ".join(map(str, extra_info))
            return f"{progress_str} {extra_str}"

        return progress_str

    def xǁProgressReporterǁget_formatted_progress__mutmut_24(
        self, current_index: int, extra_info: List[Any] = None
    ) -> str:
        """
        Calculates metrics and returns the legacy-style formatted string.
        Format: Percentage% (Done+Remaining), AvgTimes per item, Total = Elapsed + Remaining Info
        """
        completed = current_index + 1
        remaining = self.total - completed
        percentage = completed / self.total if self.total > 0 else 0

        elapsed = time.monotonic() - self.start_time
        avg_time = elapsed / completed if completed > 0 else 0
        remaining_time = remaining * avg_time
        total_estimated = elapsed + remaining_time

        progress_str = (
            f"{percentage:.2%} ({completed}+{remaining}), "
            f"{avg_time:.4f}s/item, "
            f"{self._format_seconds(total_estimated)} = "
            f"{self._format_seconds(None)} + "
            f"{self._format_seconds(remaining_time)}"
        )

        if extra_info:
            extra_str = " ".join(map(str, extra_info))
            return f"{progress_str} {extra_str}"

        return progress_str

    def xǁProgressReporterǁget_formatted_progress__mutmut_25(
        self, current_index: int, extra_info: List[Any] = None
    ) -> str:
        """
        Calculates metrics and returns the legacy-style formatted string.
        Format: Percentage% (Done+Remaining), AvgTimes per item, Total = Elapsed + Remaining Info
        """
        completed = current_index + 1
        remaining = self.total - completed
        percentage = completed / self.total if self.total > 0 else 0

        elapsed = time.monotonic() - self.start_time
        avg_time = elapsed / completed if completed > 0 else 0
        remaining_time = remaining * avg_time
        total_estimated = elapsed + remaining_time

        progress_str = (
            f"{percentage:.2%} ({completed}+{remaining}), "
            f"{avg_time:.4f}s/item, "
            f"{self._format_seconds(total_estimated)} = "
            f"{self._format_seconds(elapsed)} + "
            f"{self._format_seconds(None)}"
        )

        if extra_info:
            extra_str = " ".join(map(str, extra_info))
            return f"{progress_str} {extra_str}"

        return progress_str

    def xǁProgressReporterǁget_formatted_progress__mutmut_26(
        self, current_index: int, extra_info: List[Any] = None
    ) -> str:
        """
        Calculates metrics and returns the legacy-style formatted string.
        Format: Percentage% (Done+Remaining), AvgTimes per item, Total = Elapsed + Remaining Info
        """
        completed = current_index + 1
        remaining = self.total - completed
        percentage = completed / self.total if self.total > 0 else 0

        elapsed = time.monotonic() - self.start_time
        avg_time = elapsed / completed if completed > 0 else 0
        remaining_time = remaining * avg_time
        total_estimated = elapsed + remaining_time

        progress_str = (
            f"{percentage:.2%} ({completed}+{remaining}), "
            f"{avg_time:.4f}s/item, "
            f"{self._format_seconds(total_estimated)} = "
            f"{self._format_seconds(elapsed)} + "
            f"{self._format_seconds(remaining_time)}"
        )

        if extra_info:
            extra_str = None
            return f"{progress_str} {extra_str}"

        return progress_str

    def xǁProgressReporterǁget_formatted_progress__mutmut_27(
        self, current_index: int, extra_info: List[Any] = None
    ) -> str:
        """
        Calculates metrics and returns the legacy-style formatted string.
        Format: Percentage% (Done+Remaining), AvgTimes per item, Total = Elapsed + Remaining Info
        """
        completed = current_index + 1
        remaining = self.total - completed
        percentage = completed / self.total if self.total > 0 else 0

        elapsed = time.monotonic() - self.start_time
        avg_time = elapsed / completed if completed > 0 else 0
        remaining_time = remaining * avg_time
        total_estimated = elapsed + remaining_time

        progress_str = (
            f"{percentage:.2%} ({completed}+{remaining}), "
            f"{avg_time:.4f}s/item, "
            f"{self._format_seconds(total_estimated)} = "
            f"{self._format_seconds(elapsed)} + "
            f"{self._format_seconds(remaining_time)}"
        )

        if extra_info:
            extra_str = " ".join(None)
            return f"{progress_str} {extra_str}"

        return progress_str

    def xǁProgressReporterǁget_formatted_progress__mutmut_28(
        self, current_index: int, extra_info: List[Any] = None
    ) -> str:
        """
        Calculates metrics and returns the legacy-style formatted string.
        Format: Percentage% (Done+Remaining), AvgTimes per item, Total = Elapsed + Remaining Info
        """
        completed = current_index + 1
        remaining = self.total - completed
        percentage = completed / self.total if self.total > 0 else 0

        elapsed = time.monotonic() - self.start_time
        avg_time = elapsed / completed if completed > 0 else 0
        remaining_time = remaining * avg_time
        total_estimated = elapsed + remaining_time

        progress_str = (
            f"{percentage:.2%} ({completed}+{remaining}), "
            f"{avg_time:.4f}s/item, "
            f"{self._format_seconds(total_estimated)} = "
            f"{self._format_seconds(elapsed)} + "
            f"{self._format_seconds(remaining_time)}"
        )

        if extra_info:
            extra_str = "XX XX".join(map(str, extra_info))
            return f"{progress_str} {extra_str}"

        return progress_str

    def xǁProgressReporterǁget_formatted_progress__mutmut_29(
        self, current_index: int, extra_info: List[Any] = None
    ) -> str:
        """
        Calculates metrics and returns the legacy-style formatted string.
        Format: Percentage% (Done+Remaining), AvgTimes per item, Total = Elapsed + Remaining Info
        """
        completed = current_index + 1
        remaining = self.total - completed
        percentage = completed / self.total if self.total > 0 else 0

        elapsed = time.monotonic() - self.start_time
        avg_time = elapsed / completed if completed > 0 else 0
        remaining_time = remaining * avg_time
        total_estimated = elapsed + remaining_time

        progress_str = (
            f"{percentage:.2%} ({completed}+{remaining}), "
            f"{avg_time:.4f}s/item, "
            f"{self._format_seconds(total_estimated)} = "
            f"{self._format_seconds(elapsed)} + "
            f"{self._format_seconds(remaining_time)}"
        )

        if extra_info:
            extra_str = " ".join(map(None, extra_info))
            return f"{progress_str} {extra_str}"

        return progress_str

    def xǁProgressReporterǁget_formatted_progress__mutmut_30(
        self, current_index: int, extra_info: List[Any] = None
    ) -> str:
        """
        Calculates metrics and returns the legacy-style formatted string.
        Format: Percentage% (Done+Remaining), AvgTimes per item, Total = Elapsed + Remaining Info
        """
        completed = current_index + 1
        remaining = self.total - completed
        percentage = completed / self.total if self.total > 0 else 0

        elapsed = time.monotonic() - self.start_time
        avg_time = elapsed / completed if completed > 0 else 0
        remaining_time = remaining * avg_time
        total_estimated = elapsed + remaining_time

        progress_str = (
            f"{percentage:.2%} ({completed}+{remaining}), "
            f"{avg_time:.4f}s/item, "
            f"{self._format_seconds(total_estimated)} = "
            f"{self._format_seconds(elapsed)} + "
            f"{self._format_seconds(remaining_time)}"
        )

        if extra_info:
            extra_str = " ".join(map(str, None))
            return f"{progress_str} {extra_str}"

        return progress_str

    def xǁProgressReporterǁget_formatted_progress__mutmut_31(
        self, current_index: int, extra_info: List[Any] = None
    ) -> str:
        """
        Calculates metrics and returns the legacy-style formatted string.
        Format: Percentage% (Done+Remaining), AvgTimes per item, Total = Elapsed + Remaining Info
        """
        completed = current_index + 1
        remaining = self.total - completed
        percentage = completed / self.total if self.total > 0 else 0

        elapsed = time.monotonic() - self.start_time
        avg_time = elapsed / completed if completed > 0 else 0
        remaining_time = remaining * avg_time
        total_estimated = elapsed + remaining_time

        progress_str = (
            f"{percentage:.2%} ({completed}+{remaining}), "
            f"{avg_time:.4f}s/item, "
            f"{self._format_seconds(total_estimated)} = "
            f"{self._format_seconds(elapsed)} + "
            f"{self._format_seconds(remaining_time)}"
        )

        if extra_info:
            extra_str = " ".join(map(extra_info))
            return f"{progress_str} {extra_str}"

        return progress_str

    def xǁProgressReporterǁget_formatted_progress__mutmut_32(
        self, current_index: int, extra_info: List[Any] = None
    ) -> str:
        """
        Calculates metrics and returns the legacy-style formatted string.
        Format: Percentage% (Done+Remaining), AvgTimes per item, Total = Elapsed + Remaining Info
        """
        completed = current_index + 1
        remaining = self.total - completed
        percentage = completed / self.total if self.total > 0 else 0

        elapsed = time.monotonic() - self.start_time
        avg_time = elapsed / completed if completed > 0 else 0
        remaining_time = remaining * avg_time
        total_estimated = elapsed + remaining_time

        progress_str = (
            f"{percentage:.2%} ({completed}+{remaining}), "
            f"{avg_time:.4f}s/item, "
            f"{self._format_seconds(total_estimated)} = "
            f"{self._format_seconds(elapsed)} + "
            f"{self._format_seconds(remaining_time)}"
        )

        if extra_info:
            extra_str = " ".join(
                map(
                    str,
                )
            )
            return f"{progress_str} {extra_str}"

        return progress_str

    xǁProgressReporterǁget_formatted_progress__mutmut_mutants: ClassVar[MutantDict] = {  # type: ignore
        "xǁProgressReporterǁget_formatted_progress__mutmut_1": xǁProgressReporterǁget_formatted_progress__mutmut_1,
        "xǁProgressReporterǁget_formatted_progress__mutmut_2": xǁProgressReporterǁget_formatted_progress__mutmut_2,
        "xǁProgressReporterǁget_formatted_progress__mutmut_3": xǁProgressReporterǁget_formatted_progress__mutmut_3,
        "xǁProgressReporterǁget_formatted_progress__mutmut_4": xǁProgressReporterǁget_formatted_progress__mutmut_4,
        "xǁProgressReporterǁget_formatted_progress__mutmut_5": xǁProgressReporterǁget_formatted_progress__mutmut_5,
        "xǁProgressReporterǁget_formatted_progress__mutmut_6": xǁProgressReporterǁget_formatted_progress__mutmut_6,
        "xǁProgressReporterǁget_formatted_progress__mutmut_7": xǁProgressReporterǁget_formatted_progress__mutmut_7,
        "xǁProgressReporterǁget_formatted_progress__mutmut_8": xǁProgressReporterǁget_formatted_progress__mutmut_8,
        "xǁProgressReporterǁget_formatted_progress__mutmut_9": xǁProgressReporterǁget_formatted_progress__mutmut_9,
        "xǁProgressReporterǁget_formatted_progress__mutmut_10": xǁProgressReporterǁget_formatted_progress__mutmut_10,
        "xǁProgressReporterǁget_formatted_progress__mutmut_11": xǁProgressReporterǁget_formatted_progress__mutmut_11,
        "xǁProgressReporterǁget_formatted_progress__mutmut_12": xǁProgressReporterǁget_formatted_progress__mutmut_12,
        "xǁProgressReporterǁget_formatted_progress__mutmut_13": xǁProgressReporterǁget_formatted_progress__mutmut_13,
        "xǁProgressReporterǁget_formatted_progress__mutmut_14": xǁProgressReporterǁget_formatted_progress__mutmut_14,
        "xǁProgressReporterǁget_formatted_progress__mutmut_15": xǁProgressReporterǁget_formatted_progress__mutmut_15,
        "xǁProgressReporterǁget_formatted_progress__mutmut_16": xǁProgressReporterǁget_formatted_progress__mutmut_16,
        "xǁProgressReporterǁget_formatted_progress__mutmut_17": xǁProgressReporterǁget_formatted_progress__mutmut_17,
        "xǁProgressReporterǁget_formatted_progress__mutmut_18": xǁProgressReporterǁget_formatted_progress__mutmut_18,
        "xǁProgressReporterǁget_formatted_progress__mutmut_19": xǁProgressReporterǁget_formatted_progress__mutmut_19,
        "xǁProgressReporterǁget_formatted_progress__mutmut_20": xǁProgressReporterǁget_formatted_progress__mutmut_20,
        "xǁProgressReporterǁget_formatted_progress__mutmut_21": xǁProgressReporterǁget_formatted_progress__mutmut_21,
        "xǁProgressReporterǁget_formatted_progress__mutmut_22": xǁProgressReporterǁget_formatted_progress__mutmut_22,
        "xǁProgressReporterǁget_formatted_progress__mutmut_23": xǁProgressReporterǁget_formatted_progress__mutmut_23,
        "xǁProgressReporterǁget_formatted_progress__mutmut_24": xǁProgressReporterǁget_formatted_progress__mutmut_24,
        "xǁProgressReporterǁget_formatted_progress__mutmut_25": xǁProgressReporterǁget_formatted_progress__mutmut_25,
        "xǁProgressReporterǁget_formatted_progress__mutmut_26": xǁProgressReporterǁget_formatted_progress__mutmut_26,
        "xǁProgressReporterǁget_formatted_progress__mutmut_27": xǁProgressReporterǁget_formatted_progress__mutmut_27,
        "xǁProgressReporterǁget_formatted_progress__mutmut_28": xǁProgressReporterǁget_formatted_progress__mutmut_28,
        "xǁProgressReporterǁget_formatted_progress__mutmut_29": xǁProgressReporterǁget_formatted_progress__mutmut_29,
        "xǁProgressReporterǁget_formatted_progress__mutmut_30": xǁProgressReporterǁget_formatted_progress__mutmut_30,
        "xǁProgressReporterǁget_formatted_progress__mutmut_31": xǁProgressReporterǁget_formatted_progress__mutmut_31,
        "xǁProgressReporterǁget_formatted_progress__mutmut_32": xǁProgressReporterǁget_formatted_progress__mutmut_32,
    }
    xǁProgressReporterǁget_formatted_progress__mutmut_orig.__name__ = (
        "xǁProgressReporterǁget_formatted_progress"
    )
