import time
from shared.infrastructure.progress import ProgressReporter

def test_progress_reporter_initialization():
    reporter = ProgressReporter(total=100)
    assert reporter.total == 100
    assert reporter.start_time <= time.monotonic()

def test_progress_reporter_formatting():
    reporter = ProgressReporter(total=10)
    # Simulate some progress
    output = reporter.get_formatted_progress(current_index=0)
    # Format: Percentage% (Done+Remaining), AvgTimes per item, Total = Elapsed + Remaining Info
    # 10.00% (1+9), ...
    assert "10.00% (1+9)" in output
    assert "s/item" in output

def test_progress_reporter_extra_info():
    reporter = ProgressReporter(total=10)
    output = reporter.get_formatted_progress(current_index=0, extra_info=["FETCHING", "DATA"])
    assert "FETCHING DATA" in output

def test_progress_reporter_time_formatting():
    reporter = ProgressReporter(total=1)
    # 3661 seconds = 1h01m01s
    formatted = reporter._format_seconds(3661)
    assert formatted == "1h01m01s"

def test_progress_reporter_zero_total():
    reporter = ProgressReporter(total=0)
    output = reporter.get_formatted_progress(current_index=0)
    assert "(1+-1)" in output
    # Wait, current_index is usually 0..N-1.
    # If total is 0, it might be buggy but should not crash.
