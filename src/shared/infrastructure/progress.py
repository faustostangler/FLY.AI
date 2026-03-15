import time
from typing import List, Any


class ProgressReporter:
    """
    SOTA Progress Reporter that maintains the legacy formatting style
    while providing a clean, object-oriented API for modern DDD applications.
    """

    def __init__(self, total: int):
        self.total = total
        self.start_time = time.monotonic()

    def _format_seconds(self, seconds: float) -> str:
        hours, remainder = divmod(int(seconds), 3600)
        minutes, seconds_int = divmod(remainder, 60)
        return f"{int(hours)}h{int(minutes):02}m{int(seconds_int):02}s"

    def get_formatted_progress(
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
