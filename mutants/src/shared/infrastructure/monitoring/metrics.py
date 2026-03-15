import math
import os
from prometheus_client import Counter, Histogram, Gauge
from shared.infrastructure.config import settings
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

def get_buckets(min_val: float = 1, max_val: float = 100, step: float = 0.1):
    args = [min_val, max_val, step]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_get_buckets__mutmut_orig, x_get_buckets__mutmut_mutants, args, kwargs, None)

def x_get_buckets__mutmut_orig(min_val: float = 1, max_val: float = 100, step: float = 0.1):
    """Generates logarithmic buckets for Prometheus histograms.

    Logarithmic spacing is superior for request durations and payload sizes 
    across several orders of magnitude, providing higher resolution at lower values 
    where most requests fall, while still capturing long-tail outliers.

    Args:
        min_val (float): The starting value for the first bucket.
        max_val (float): The upper bound for the last bucket.
        step (float): The logarithmic step (base 10) between buckets.

    Returns:
        tuple[float]: A sequence of rounded bucket boundaries.

    Raises:
        ValueError: If min_val is non-positive, as log10 requires positive values.
    """
    if min_val <= 0:
        raise ValueError("min_val must be greater than 0 for logarithmic scale.")
    
    start_exp = math.log10(min_val)
    end_exp = math.log10(max_val)
    
    # +1e-9 to mitigate float precision issues during range calculation.
    num_steps = int((end_exp - start_exp) / step + 1e-9) + 1
    return tuple(round(10 ** (start_exp + i * step), 4) for i in range(num_steps))

def x_get_buckets__mutmut_1(min_val: float = 2, max_val: float = 100, step: float = 0.1):
    """Generates logarithmic buckets for Prometheus histograms.

    Logarithmic spacing is superior for request durations and payload sizes 
    across several orders of magnitude, providing higher resolution at lower values 
    where most requests fall, while still capturing long-tail outliers.

    Args:
        min_val (float): The starting value for the first bucket.
        max_val (float): The upper bound for the last bucket.
        step (float): The logarithmic step (base 10) between buckets.

    Returns:
        tuple[float]: A sequence of rounded bucket boundaries.

    Raises:
        ValueError: If min_val is non-positive, as log10 requires positive values.
    """
    if min_val <= 0:
        raise ValueError("min_val must be greater than 0 for logarithmic scale.")
    
    start_exp = math.log10(min_val)
    end_exp = math.log10(max_val)
    
    # +1e-9 to mitigate float precision issues during range calculation.
    num_steps = int((end_exp - start_exp) / step + 1e-9) + 1
    return tuple(round(10 ** (start_exp + i * step), 4) for i in range(num_steps))

def x_get_buckets__mutmut_2(min_val: float = 1, max_val: float = 101, step: float = 0.1):
    """Generates logarithmic buckets for Prometheus histograms.

    Logarithmic spacing is superior for request durations and payload sizes 
    across several orders of magnitude, providing higher resolution at lower values 
    where most requests fall, while still capturing long-tail outliers.

    Args:
        min_val (float): The starting value for the first bucket.
        max_val (float): The upper bound for the last bucket.
        step (float): The logarithmic step (base 10) between buckets.

    Returns:
        tuple[float]: A sequence of rounded bucket boundaries.

    Raises:
        ValueError: If min_val is non-positive, as log10 requires positive values.
    """
    if min_val <= 0:
        raise ValueError("min_val must be greater than 0 for logarithmic scale.")
    
    start_exp = math.log10(min_val)
    end_exp = math.log10(max_val)
    
    # +1e-9 to mitigate float precision issues during range calculation.
    num_steps = int((end_exp - start_exp) / step + 1e-9) + 1
    return tuple(round(10 ** (start_exp + i * step), 4) for i in range(num_steps))

def x_get_buckets__mutmut_3(min_val: float = 1, max_val: float = 100, step: float = 1.1):
    """Generates logarithmic buckets for Prometheus histograms.

    Logarithmic spacing is superior for request durations and payload sizes 
    across several orders of magnitude, providing higher resolution at lower values 
    where most requests fall, while still capturing long-tail outliers.

    Args:
        min_val (float): The starting value for the first bucket.
        max_val (float): The upper bound for the last bucket.
        step (float): The logarithmic step (base 10) between buckets.

    Returns:
        tuple[float]: A sequence of rounded bucket boundaries.

    Raises:
        ValueError: If min_val is non-positive, as log10 requires positive values.
    """
    if min_val <= 0:
        raise ValueError("min_val must be greater than 0 for logarithmic scale.")
    
    start_exp = math.log10(min_val)
    end_exp = math.log10(max_val)
    
    # +1e-9 to mitigate float precision issues during range calculation.
    num_steps = int((end_exp - start_exp) / step + 1e-9) + 1
    return tuple(round(10 ** (start_exp + i * step), 4) for i in range(num_steps))

def x_get_buckets__mutmut_4(min_val: float = 1, max_val: float = 100, step: float = 0.1):
    """Generates logarithmic buckets for Prometheus histograms.

    Logarithmic spacing is superior for request durations and payload sizes 
    across several orders of magnitude, providing higher resolution at lower values 
    where most requests fall, while still capturing long-tail outliers.

    Args:
        min_val (float): The starting value for the first bucket.
        max_val (float): The upper bound for the last bucket.
        step (float): The logarithmic step (base 10) between buckets.

    Returns:
        tuple[float]: A sequence of rounded bucket boundaries.

    Raises:
        ValueError: If min_val is non-positive, as log10 requires positive values.
    """
    if min_val < 0:
        raise ValueError("min_val must be greater than 0 for logarithmic scale.")
    
    start_exp = math.log10(min_val)
    end_exp = math.log10(max_val)
    
    # +1e-9 to mitigate float precision issues during range calculation.
    num_steps = int((end_exp - start_exp) / step + 1e-9) + 1
    return tuple(round(10 ** (start_exp + i * step), 4) for i in range(num_steps))

def x_get_buckets__mutmut_5(min_val: float = 1, max_val: float = 100, step: float = 0.1):
    """Generates logarithmic buckets for Prometheus histograms.

    Logarithmic spacing is superior for request durations and payload sizes 
    across several orders of magnitude, providing higher resolution at lower values 
    where most requests fall, while still capturing long-tail outliers.

    Args:
        min_val (float): The starting value for the first bucket.
        max_val (float): The upper bound for the last bucket.
        step (float): The logarithmic step (base 10) between buckets.

    Returns:
        tuple[float]: A sequence of rounded bucket boundaries.

    Raises:
        ValueError: If min_val is non-positive, as log10 requires positive values.
    """
    if min_val <= 1:
        raise ValueError("min_val must be greater than 0 for logarithmic scale.")
    
    start_exp = math.log10(min_val)
    end_exp = math.log10(max_val)
    
    # +1e-9 to mitigate float precision issues during range calculation.
    num_steps = int((end_exp - start_exp) / step + 1e-9) + 1
    return tuple(round(10 ** (start_exp + i * step), 4) for i in range(num_steps))

def x_get_buckets__mutmut_6(min_val: float = 1, max_val: float = 100, step: float = 0.1):
    """Generates logarithmic buckets for Prometheus histograms.

    Logarithmic spacing is superior for request durations and payload sizes 
    across several orders of magnitude, providing higher resolution at lower values 
    where most requests fall, while still capturing long-tail outliers.

    Args:
        min_val (float): The starting value for the first bucket.
        max_val (float): The upper bound for the last bucket.
        step (float): The logarithmic step (base 10) between buckets.

    Returns:
        tuple[float]: A sequence of rounded bucket boundaries.

    Raises:
        ValueError: If min_val is non-positive, as log10 requires positive values.
    """
    if min_val <= 0:
        raise ValueError(None)
    
    start_exp = math.log10(min_val)
    end_exp = math.log10(max_val)
    
    # +1e-9 to mitigate float precision issues during range calculation.
    num_steps = int((end_exp - start_exp) / step + 1e-9) + 1
    return tuple(round(10 ** (start_exp + i * step), 4) for i in range(num_steps))

def x_get_buckets__mutmut_7(min_val: float = 1, max_val: float = 100, step: float = 0.1):
    """Generates logarithmic buckets for Prometheus histograms.

    Logarithmic spacing is superior for request durations and payload sizes 
    across several orders of magnitude, providing higher resolution at lower values 
    where most requests fall, while still capturing long-tail outliers.

    Args:
        min_val (float): The starting value for the first bucket.
        max_val (float): The upper bound for the last bucket.
        step (float): The logarithmic step (base 10) between buckets.

    Returns:
        tuple[float]: A sequence of rounded bucket boundaries.

    Raises:
        ValueError: If min_val is non-positive, as log10 requires positive values.
    """
    if min_val <= 0:
        raise ValueError("XXmin_val must be greater than 0 for logarithmic scale.XX")
    
    start_exp = math.log10(min_val)
    end_exp = math.log10(max_val)
    
    # +1e-9 to mitigate float precision issues during range calculation.
    num_steps = int((end_exp - start_exp) / step + 1e-9) + 1
    return tuple(round(10 ** (start_exp + i * step), 4) for i in range(num_steps))

def x_get_buckets__mutmut_8(min_val: float = 1, max_val: float = 100, step: float = 0.1):
    """Generates logarithmic buckets for Prometheus histograms.

    Logarithmic spacing is superior for request durations and payload sizes 
    across several orders of magnitude, providing higher resolution at lower values 
    where most requests fall, while still capturing long-tail outliers.

    Args:
        min_val (float): The starting value for the first bucket.
        max_val (float): The upper bound for the last bucket.
        step (float): The logarithmic step (base 10) between buckets.

    Returns:
        tuple[float]: A sequence of rounded bucket boundaries.

    Raises:
        ValueError: If min_val is non-positive, as log10 requires positive values.
    """
    if min_val <= 0:
        raise ValueError("MIN_VAL MUST BE GREATER THAN 0 FOR LOGARITHMIC SCALE.")
    
    start_exp = math.log10(min_val)
    end_exp = math.log10(max_val)
    
    # +1e-9 to mitigate float precision issues during range calculation.
    num_steps = int((end_exp - start_exp) / step + 1e-9) + 1
    return tuple(round(10 ** (start_exp + i * step), 4) for i in range(num_steps))

def x_get_buckets__mutmut_9(min_val: float = 1, max_val: float = 100, step: float = 0.1):
    """Generates logarithmic buckets for Prometheus histograms.

    Logarithmic spacing is superior for request durations and payload sizes 
    across several orders of magnitude, providing higher resolution at lower values 
    where most requests fall, while still capturing long-tail outliers.

    Args:
        min_val (float): The starting value for the first bucket.
        max_val (float): The upper bound for the last bucket.
        step (float): The logarithmic step (base 10) between buckets.

    Returns:
        tuple[float]: A sequence of rounded bucket boundaries.

    Raises:
        ValueError: If min_val is non-positive, as log10 requires positive values.
    """
    if min_val <= 0:
        raise ValueError("min_val must be greater than 0 for logarithmic scale.")
    
    start_exp = None
    end_exp = math.log10(max_val)
    
    # +1e-9 to mitigate float precision issues during range calculation.
    num_steps = int((end_exp - start_exp) / step + 1e-9) + 1
    return tuple(round(10 ** (start_exp + i * step), 4) for i in range(num_steps))

def x_get_buckets__mutmut_10(min_val: float = 1, max_val: float = 100, step: float = 0.1):
    """Generates logarithmic buckets for Prometheus histograms.

    Logarithmic spacing is superior for request durations and payload sizes 
    across several orders of magnitude, providing higher resolution at lower values 
    where most requests fall, while still capturing long-tail outliers.

    Args:
        min_val (float): The starting value for the first bucket.
        max_val (float): The upper bound for the last bucket.
        step (float): The logarithmic step (base 10) between buckets.

    Returns:
        tuple[float]: A sequence of rounded bucket boundaries.

    Raises:
        ValueError: If min_val is non-positive, as log10 requires positive values.
    """
    if min_val <= 0:
        raise ValueError("min_val must be greater than 0 for logarithmic scale.")
    
    start_exp = math.log10(None)
    end_exp = math.log10(max_val)
    
    # +1e-9 to mitigate float precision issues during range calculation.
    num_steps = int((end_exp - start_exp) / step + 1e-9) + 1
    return tuple(round(10 ** (start_exp + i * step), 4) for i in range(num_steps))

def x_get_buckets__mutmut_11(min_val: float = 1, max_val: float = 100, step: float = 0.1):
    """Generates logarithmic buckets for Prometheus histograms.

    Logarithmic spacing is superior for request durations and payload sizes 
    across several orders of magnitude, providing higher resolution at lower values 
    where most requests fall, while still capturing long-tail outliers.

    Args:
        min_val (float): The starting value for the first bucket.
        max_val (float): The upper bound for the last bucket.
        step (float): The logarithmic step (base 10) between buckets.

    Returns:
        tuple[float]: A sequence of rounded bucket boundaries.

    Raises:
        ValueError: If min_val is non-positive, as log10 requires positive values.
    """
    if min_val <= 0:
        raise ValueError("min_val must be greater than 0 for logarithmic scale.")
    
    start_exp = math.log10(min_val)
    end_exp = None
    
    # +1e-9 to mitigate float precision issues during range calculation.
    num_steps = int((end_exp - start_exp) / step + 1e-9) + 1
    return tuple(round(10 ** (start_exp + i * step), 4) for i in range(num_steps))

def x_get_buckets__mutmut_12(min_val: float = 1, max_val: float = 100, step: float = 0.1):
    """Generates logarithmic buckets for Prometheus histograms.

    Logarithmic spacing is superior for request durations and payload sizes 
    across several orders of magnitude, providing higher resolution at lower values 
    where most requests fall, while still capturing long-tail outliers.

    Args:
        min_val (float): The starting value for the first bucket.
        max_val (float): The upper bound for the last bucket.
        step (float): The logarithmic step (base 10) between buckets.

    Returns:
        tuple[float]: A sequence of rounded bucket boundaries.

    Raises:
        ValueError: If min_val is non-positive, as log10 requires positive values.
    """
    if min_val <= 0:
        raise ValueError("min_val must be greater than 0 for logarithmic scale.")
    
    start_exp = math.log10(min_val)
    end_exp = math.log10(None)
    
    # +1e-9 to mitigate float precision issues during range calculation.
    num_steps = int((end_exp - start_exp) / step + 1e-9) + 1
    return tuple(round(10 ** (start_exp + i * step), 4) for i in range(num_steps))

def x_get_buckets__mutmut_13(min_val: float = 1, max_val: float = 100, step: float = 0.1):
    """Generates logarithmic buckets for Prometheus histograms.

    Logarithmic spacing is superior for request durations and payload sizes 
    across several orders of magnitude, providing higher resolution at lower values 
    where most requests fall, while still capturing long-tail outliers.

    Args:
        min_val (float): The starting value for the first bucket.
        max_val (float): The upper bound for the last bucket.
        step (float): The logarithmic step (base 10) between buckets.

    Returns:
        tuple[float]: A sequence of rounded bucket boundaries.

    Raises:
        ValueError: If min_val is non-positive, as log10 requires positive values.
    """
    if min_val <= 0:
        raise ValueError("min_val must be greater than 0 for logarithmic scale.")
    
    start_exp = math.log10(min_val)
    end_exp = math.log10(max_val)
    
    # +1e-9 to mitigate float precision issues during range calculation.
    num_steps = None
    return tuple(round(10 ** (start_exp + i * step), 4) for i in range(num_steps))

def x_get_buckets__mutmut_14(min_val: float = 1, max_val: float = 100, step: float = 0.1):
    """Generates logarithmic buckets for Prometheus histograms.

    Logarithmic spacing is superior for request durations and payload sizes 
    across several orders of magnitude, providing higher resolution at lower values 
    where most requests fall, while still capturing long-tail outliers.

    Args:
        min_val (float): The starting value for the first bucket.
        max_val (float): The upper bound for the last bucket.
        step (float): The logarithmic step (base 10) between buckets.

    Returns:
        tuple[float]: A sequence of rounded bucket boundaries.

    Raises:
        ValueError: If min_val is non-positive, as log10 requires positive values.
    """
    if min_val <= 0:
        raise ValueError("min_val must be greater than 0 for logarithmic scale.")
    
    start_exp = math.log10(min_val)
    end_exp = math.log10(max_val)
    
    # +1e-9 to mitigate float precision issues during range calculation.
    num_steps = int((end_exp - start_exp) / step + 1e-9) - 1
    return tuple(round(10 ** (start_exp + i * step), 4) for i in range(num_steps))

def x_get_buckets__mutmut_15(min_val: float = 1, max_val: float = 100, step: float = 0.1):
    """Generates logarithmic buckets for Prometheus histograms.

    Logarithmic spacing is superior for request durations and payload sizes 
    across several orders of magnitude, providing higher resolution at lower values 
    where most requests fall, while still capturing long-tail outliers.

    Args:
        min_val (float): The starting value for the first bucket.
        max_val (float): The upper bound for the last bucket.
        step (float): The logarithmic step (base 10) between buckets.

    Returns:
        tuple[float]: A sequence of rounded bucket boundaries.

    Raises:
        ValueError: If min_val is non-positive, as log10 requires positive values.
    """
    if min_val <= 0:
        raise ValueError("min_val must be greater than 0 for logarithmic scale.")
    
    start_exp = math.log10(min_val)
    end_exp = math.log10(max_val)
    
    # +1e-9 to mitigate float precision issues during range calculation.
    num_steps = int(None) + 1
    return tuple(round(10 ** (start_exp + i * step), 4) for i in range(num_steps))

def x_get_buckets__mutmut_16(min_val: float = 1, max_val: float = 100, step: float = 0.1):
    """Generates logarithmic buckets for Prometheus histograms.

    Logarithmic spacing is superior for request durations and payload sizes 
    across several orders of magnitude, providing higher resolution at lower values 
    where most requests fall, while still capturing long-tail outliers.

    Args:
        min_val (float): The starting value for the first bucket.
        max_val (float): The upper bound for the last bucket.
        step (float): The logarithmic step (base 10) between buckets.

    Returns:
        tuple[float]: A sequence of rounded bucket boundaries.

    Raises:
        ValueError: If min_val is non-positive, as log10 requires positive values.
    """
    if min_val <= 0:
        raise ValueError("min_val must be greater than 0 for logarithmic scale.")
    
    start_exp = math.log10(min_val)
    end_exp = math.log10(max_val)
    
    # +1e-9 to mitigate float precision issues during range calculation.
    num_steps = int((end_exp - start_exp) / step - 1e-9) + 1
    return tuple(round(10 ** (start_exp + i * step), 4) for i in range(num_steps))

def x_get_buckets__mutmut_17(min_val: float = 1, max_val: float = 100, step: float = 0.1):
    """Generates logarithmic buckets for Prometheus histograms.

    Logarithmic spacing is superior for request durations and payload sizes 
    across several orders of magnitude, providing higher resolution at lower values 
    where most requests fall, while still capturing long-tail outliers.

    Args:
        min_val (float): The starting value for the first bucket.
        max_val (float): The upper bound for the last bucket.
        step (float): The logarithmic step (base 10) between buckets.

    Returns:
        tuple[float]: A sequence of rounded bucket boundaries.

    Raises:
        ValueError: If min_val is non-positive, as log10 requires positive values.
    """
    if min_val <= 0:
        raise ValueError("min_val must be greater than 0 for logarithmic scale.")
    
    start_exp = math.log10(min_val)
    end_exp = math.log10(max_val)
    
    # +1e-9 to mitigate float precision issues during range calculation.
    num_steps = int((end_exp - start_exp) * step + 1e-9) + 1
    return tuple(round(10 ** (start_exp + i * step), 4) for i in range(num_steps))

def x_get_buckets__mutmut_18(min_val: float = 1, max_val: float = 100, step: float = 0.1):
    """Generates logarithmic buckets for Prometheus histograms.

    Logarithmic spacing is superior for request durations and payload sizes 
    across several orders of magnitude, providing higher resolution at lower values 
    where most requests fall, while still capturing long-tail outliers.

    Args:
        min_val (float): The starting value for the first bucket.
        max_val (float): The upper bound for the last bucket.
        step (float): The logarithmic step (base 10) between buckets.

    Returns:
        tuple[float]: A sequence of rounded bucket boundaries.

    Raises:
        ValueError: If min_val is non-positive, as log10 requires positive values.
    """
    if min_val <= 0:
        raise ValueError("min_val must be greater than 0 for logarithmic scale.")
    
    start_exp = math.log10(min_val)
    end_exp = math.log10(max_val)
    
    # +1e-9 to mitigate float precision issues during range calculation.
    num_steps = int((end_exp + start_exp) / step + 1e-9) + 1
    return tuple(round(10 ** (start_exp + i * step), 4) for i in range(num_steps))

def x_get_buckets__mutmut_19(min_val: float = 1, max_val: float = 100, step: float = 0.1):
    """Generates logarithmic buckets for Prometheus histograms.

    Logarithmic spacing is superior for request durations and payload sizes 
    across several orders of magnitude, providing higher resolution at lower values 
    where most requests fall, while still capturing long-tail outliers.

    Args:
        min_val (float): The starting value for the first bucket.
        max_val (float): The upper bound for the last bucket.
        step (float): The logarithmic step (base 10) between buckets.

    Returns:
        tuple[float]: A sequence of rounded bucket boundaries.

    Raises:
        ValueError: If min_val is non-positive, as log10 requires positive values.
    """
    if min_val <= 0:
        raise ValueError("min_val must be greater than 0 for logarithmic scale.")
    
    start_exp = math.log10(min_val)
    end_exp = math.log10(max_val)
    
    # +1e-9 to mitigate float precision issues during range calculation.
    num_steps = int((end_exp - start_exp) / step + 1.000000001) + 1
    return tuple(round(10 ** (start_exp + i * step), 4) for i in range(num_steps))

def x_get_buckets__mutmut_20(min_val: float = 1, max_val: float = 100, step: float = 0.1):
    """Generates logarithmic buckets for Prometheus histograms.

    Logarithmic spacing is superior for request durations and payload sizes 
    across several orders of magnitude, providing higher resolution at lower values 
    where most requests fall, while still capturing long-tail outliers.

    Args:
        min_val (float): The starting value for the first bucket.
        max_val (float): The upper bound for the last bucket.
        step (float): The logarithmic step (base 10) between buckets.

    Returns:
        tuple[float]: A sequence of rounded bucket boundaries.

    Raises:
        ValueError: If min_val is non-positive, as log10 requires positive values.
    """
    if min_val <= 0:
        raise ValueError("min_val must be greater than 0 for logarithmic scale.")
    
    start_exp = math.log10(min_val)
    end_exp = math.log10(max_val)
    
    # +1e-9 to mitigate float precision issues during range calculation.
    num_steps = int((end_exp - start_exp) / step + 1e-9) + 2
    return tuple(round(10 ** (start_exp + i * step), 4) for i in range(num_steps))

def x_get_buckets__mutmut_21(min_val: float = 1, max_val: float = 100, step: float = 0.1):
    """Generates logarithmic buckets for Prometheus histograms.

    Logarithmic spacing is superior for request durations and payload sizes 
    across several orders of magnitude, providing higher resolution at lower values 
    where most requests fall, while still capturing long-tail outliers.

    Args:
        min_val (float): The starting value for the first bucket.
        max_val (float): The upper bound for the last bucket.
        step (float): The logarithmic step (base 10) between buckets.

    Returns:
        tuple[float]: A sequence of rounded bucket boundaries.

    Raises:
        ValueError: If min_val is non-positive, as log10 requires positive values.
    """
    if min_val <= 0:
        raise ValueError("min_val must be greater than 0 for logarithmic scale.")
    
    start_exp = math.log10(min_val)
    end_exp = math.log10(max_val)
    
    # +1e-9 to mitigate float precision issues during range calculation.
    num_steps = int((end_exp - start_exp) / step + 1e-9) + 1
    return tuple(None)

def x_get_buckets__mutmut_22(min_val: float = 1, max_val: float = 100, step: float = 0.1):
    """Generates logarithmic buckets for Prometheus histograms.

    Logarithmic spacing is superior for request durations and payload sizes 
    across several orders of magnitude, providing higher resolution at lower values 
    where most requests fall, while still capturing long-tail outliers.

    Args:
        min_val (float): The starting value for the first bucket.
        max_val (float): The upper bound for the last bucket.
        step (float): The logarithmic step (base 10) between buckets.

    Returns:
        tuple[float]: A sequence of rounded bucket boundaries.

    Raises:
        ValueError: If min_val is non-positive, as log10 requires positive values.
    """
    if min_val <= 0:
        raise ValueError("min_val must be greater than 0 for logarithmic scale.")
    
    start_exp = math.log10(min_val)
    end_exp = math.log10(max_val)
    
    # +1e-9 to mitigate float precision issues during range calculation.
    num_steps = int((end_exp - start_exp) / step + 1e-9) + 1
    return tuple(round(None, 4) for i in range(num_steps))

def x_get_buckets__mutmut_23(min_val: float = 1, max_val: float = 100, step: float = 0.1):
    """Generates logarithmic buckets for Prometheus histograms.

    Logarithmic spacing is superior for request durations and payload sizes 
    across several orders of magnitude, providing higher resolution at lower values 
    where most requests fall, while still capturing long-tail outliers.

    Args:
        min_val (float): The starting value for the first bucket.
        max_val (float): The upper bound for the last bucket.
        step (float): The logarithmic step (base 10) between buckets.

    Returns:
        tuple[float]: A sequence of rounded bucket boundaries.

    Raises:
        ValueError: If min_val is non-positive, as log10 requires positive values.
    """
    if min_val <= 0:
        raise ValueError("min_val must be greater than 0 for logarithmic scale.")
    
    start_exp = math.log10(min_val)
    end_exp = math.log10(max_val)
    
    # +1e-9 to mitigate float precision issues during range calculation.
    num_steps = int((end_exp - start_exp) / step + 1e-9) + 1
    return tuple(round(10 ** (start_exp + i * step), None) for i in range(num_steps))

def x_get_buckets__mutmut_24(min_val: float = 1, max_val: float = 100, step: float = 0.1):
    """Generates logarithmic buckets for Prometheus histograms.

    Logarithmic spacing is superior for request durations and payload sizes 
    across several orders of magnitude, providing higher resolution at lower values 
    where most requests fall, while still capturing long-tail outliers.

    Args:
        min_val (float): The starting value for the first bucket.
        max_val (float): The upper bound for the last bucket.
        step (float): The logarithmic step (base 10) between buckets.

    Returns:
        tuple[float]: A sequence of rounded bucket boundaries.

    Raises:
        ValueError: If min_val is non-positive, as log10 requires positive values.
    """
    if min_val <= 0:
        raise ValueError("min_val must be greater than 0 for logarithmic scale.")
    
    start_exp = math.log10(min_val)
    end_exp = math.log10(max_val)
    
    # +1e-9 to mitigate float precision issues during range calculation.
    num_steps = int((end_exp - start_exp) / step + 1e-9) + 1
    return tuple(round(4) for i in range(num_steps))

def x_get_buckets__mutmut_25(min_val: float = 1, max_val: float = 100, step: float = 0.1):
    """Generates logarithmic buckets for Prometheus histograms.

    Logarithmic spacing is superior for request durations and payload sizes 
    across several orders of magnitude, providing higher resolution at lower values 
    where most requests fall, while still capturing long-tail outliers.

    Args:
        min_val (float): The starting value for the first bucket.
        max_val (float): The upper bound for the last bucket.
        step (float): The logarithmic step (base 10) between buckets.

    Returns:
        tuple[float]: A sequence of rounded bucket boundaries.

    Raises:
        ValueError: If min_val is non-positive, as log10 requires positive values.
    """
    if min_val <= 0:
        raise ValueError("min_val must be greater than 0 for logarithmic scale.")
    
    start_exp = math.log10(min_val)
    end_exp = math.log10(max_val)
    
    # +1e-9 to mitigate float precision issues during range calculation.
    num_steps = int((end_exp - start_exp) / step + 1e-9) + 1
    return tuple(round(10 ** (start_exp + i * step), ) for i in range(num_steps))

def x_get_buckets__mutmut_26(min_val: float = 1, max_val: float = 100, step: float = 0.1):
    """Generates logarithmic buckets for Prometheus histograms.

    Logarithmic spacing is superior for request durations and payload sizes 
    across several orders of magnitude, providing higher resolution at lower values 
    where most requests fall, while still capturing long-tail outliers.

    Args:
        min_val (float): The starting value for the first bucket.
        max_val (float): The upper bound for the last bucket.
        step (float): The logarithmic step (base 10) between buckets.

    Returns:
        tuple[float]: A sequence of rounded bucket boundaries.

    Raises:
        ValueError: If min_val is non-positive, as log10 requires positive values.
    """
    if min_val <= 0:
        raise ValueError("min_val must be greater than 0 for logarithmic scale.")
    
    start_exp = math.log10(min_val)
    end_exp = math.log10(max_val)
    
    # +1e-9 to mitigate float precision issues during range calculation.
    num_steps = int((end_exp - start_exp) / step + 1e-9) + 1
    return tuple(round(10 * (start_exp + i * step), 4) for i in range(num_steps))

def x_get_buckets__mutmut_27(min_val: float = 1, max_val: float = 100, step: float = 0.1):
    """Generates logarithmic buckets for Prometheus histograms.

    Logarithmic spacing is superior for request durations and payload sizes 
    across several orders of magnitude, providing higher resolution at lower values 
    where most requests fall, while still capturing long-tail outliers.

    Args:
        min_val (float): The starting value for the first bucket.
        max_val (float): The upper bound for the last bucket.
        step (float): The logarithmic step (base 10) between buckets.

    Returns:
        tuple[float]: A sequence of rounded bucket boundaries.

    Raises:
        ValueError: If min_val is non-positive, as log10 requires positive values.
    """
    if min_val <= 0:
        raise ValueError("min_val must be greater than 0 for logarithmic scale.")
    
    start_exp = math.log10(min_val)
    end_exp = math.log10(max_val)
    
    # +1e-9 to mitigate float precision issues during range calculation.
    num_steps = int((end_exp - start_exp) / step + 1e-9) + 1
    return tuple(round(11 ** (start_exp + i * step), 4) for i in range(num_steps))

def x_get_buckets__mutmut_28(min_val: float = 1, max_val: float = 100, step: float = 0.1):
    """Generates logarithmic buckets for Prometheus histograms.

    Logarithmic spacing is superior for request durations and payload sizes 
    across several orders of magnitude, providing higher resolution at lower values 
    where most requests fall, while still capturing long-tail outliers.

    Args:
        min_val (float): The starting value for the first bucket.
        max_val (float): The upper bound for the last bucket.
        step (float): The logarithmic step (base 10) between buckets.

    Returns:
        tuple[float]: A sequence of rounded bucket boundaries.

    Raises:
        ValueError: If min_val is non-positive, as log10 requires positive values.
    """
    if min_val <= 0:
        raise ValueError("min_val must be greater than 0 for logarithmic scale.")
    
    start_exp = math.log10(min_val)
    end_exp = math.log10(max_val)
    
    # +1e-9 to mitigate float precision issues during range calculation.
    num_steps = int((end_exp - start_exp) / step + 1e-9) + 1
    return tuple(round(10 ** (start_exp - i * step), 4) for i in range(num_steps))

def x_get_buckets__mutmut_29(min_val: float = 1, max_val: float = 100, step: float = 0.1):
    """Generates logarithmic buckets for Prometheus histograms.

    Logarithmic spacing is superior for request durations and payload sizes 
    across several orders of magnitude, providing higher resolution at lower values 
    where most requests fall, while still capturing long-tail outliers.

    Args:
        min_val (float): The starting value for the first bucket.
        max_val (float): The upper bound for the last bucket.
        step (float): The logarithmic step (base 10) between buckets.

    Returns:
        tuple[float]: A sequence of rounded bucket boundaries.

    Raises:
        ValueError: If min_val is non-positive, as log10 requires positive values.
    """
    if min_val <= 0:
        raise ValueError("min_val must be greater than 0 for logarithmic scale.")
    
    start_exp = math.log10(min_val)
    end_exp = math.log10(max_val)
    
    # +1e-9 to mitigate float precision issues during range calculation.
    num_steps = int((end_exp - start_exp) / step + 1e-9) + 1
    return tuple(round(10 ** (start_exp + i / step), 4) for i in range(num_steps))

def x_get_buckets__mutmut_30(min_val: float = 1, max_val: float = 100, step: float = 0.1):
    """Generates logarithmic buckets for Prometheus histograms.

    Logarithmic spacing is superior for request durations and payload sizes 
    across several orders of magnitude, providing higher resolution at lower values 
    where most requests fall, while still capturing long-tail outliers.

    Args:
        min_val (float): The starting value for the first bucket.
        max_val (float): The upper bound for the last bucket.
        step (float): The logarithmic step (base 10) between buckets.

    Returns:
        tuple[float]: A sequence of rounded bucket boundaries.

    Raises:
        ValueError: If min_val is non-positive, as log10 requires positive values.
    """
    if min_val <= 0:
        raise ValueError("min_val must be greater than 0 for logarithmic scale.")
    
    start_exp = math.log10(min_val)
    end_exp = math.log10(max_val)
    
    # +1e-9 to mitigate float precision issues during range calculation.
    num_steps = int((end_exp - start_exp) / step + 1e-9) + 1
    return tuple(round(10 ** (start_exp + i * step), 5) for i in range(num_steps))

def x_get_buckets__mutmut_31(min_val: float = 1, max_val: float = 100, step: float = 0.1):
    """Generates logarithmic buckets for Prometheus histograms.

    Logarithmic spacing is superior for request durations and payload sizes 
    across several orders of magnitude, providing higher resolution at lower values 
    where most requests fall, while still capturing long-tail outliers.

    Args:
        min_val (float): The starting value for the first bucket.
        max_val (float): The upper bound for the last bucket.
        step (float): The logarithmic step (base 10) between buckets.

    Returns:
        tuple[float]: A sequence of rounded bucket boundaries.

    Raises:
        ValueError: If min_val is non-positive, as log10 requires positive values.
    """
    if min_val <= 0:
        raise ValueError("min_val must be greater than 0 for logarithmic scale.")
    
    start_exp = math.log10(min_val)
    end_exp = math.log10(max_val)
    
    # +1e-9 to mitigate float precision issues during range calculation.
    num_steps = int((end_exp - start_exp) / step + 1e-9) + 1
    return tuple(round(10 ** (start_exp + i * step), 4) for i in range(None))

x_get_buckets__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_get_buckets__mutmut_1': x_get_buckets__mutmut_1, 
    'x_get_buckets__mutmut_2': x_get_buckets__mutmut_2, 
    'x_get_buckets__mutmut_3': x_get_buckets__mutmut_3, 
    'x_get_buckets__mutmut_4': x_get_buckets__mutmut_4, 
    'x_get_buckets__mutmut_5': x_get_buckets__mutmut_5, 
    'x_get_buckets__mutmut_6': x_get_buckets__mutmut_6, 
    'x_get_buckets__mutmut_7': x_get_buckets__mutmut_7, 
    'x_get_buckets__mutmut_8': x_get_buckets__mutmut_8, 
    'x_get_buckets__mutmut_9': x_get_buckets__mutmut_9, 
    'x_get_buckets__mutmut_10': x_get_buckets__mutmut_10, 
    'x_get_buckets__mutmut_11': x_get_buckets__mutmut_11, 
    'x_get_buckets__mutmut_12': x_get_buckets__mutmut_12, 
    'x_get_buckets__mutmut_13': x_get_buckets__mutmut_13, 
    'x_get_buckets__mutmut_14': x_get_buckets__mutmut_14, 
    'x_get_buckets__mutmut_15': x_get_buckets__mutmut_15, 
    'x_get_buckets__mutmut_16': x_get_buckets__mutmut_16, 
    'x_get_buckets__mutmut_17': x_get_buckets__mutmut_17, 
    'x_get_buckets__mutmut_18': x_get_buckets__mutmut_18, 
    'x_get_buckets__mutmut_19': x_get_buckets__mutmut_19, 
    'x_get_buckets__mutmut_20': x_get_buckets__mutmut_20, 
    'x_get_buckets__mutmut_21': x_get_buckets__mutmut_21, 
    'x_get_buckets__mutmut_22': x_get_buckets__mutmut_22, 
    'x_get_buckets__mutmut_23': x_get_buckets__mutmut_23, 
    'x_get_buckets__mutmut_24': x_get_buckets__mutmut_24, 
    'x_get_buckets__mutmut_25': x_get_buckets__mutmut_25, 
    'x_get_buckets__mutmut_26': x_get_buckets__mutmut_26, 
    'x_get_buckets__mutmut_27': x_get_buckets__mutmut_27, 
    'x_get_buckets__mutmut_28': x_get_buckets__mutmut_28, 
    'x_get_buckets__mutmut_29': x_get_buckets__mutmut_29, 
    'x_get_buckets__mutmut_30': x_get_buckets__mutmut_30, 
    'x_get_buckets__mutmut_31': x_get_buckets__mutmut_31
}
x_get_buckets__mutmut_orig.__name__ = 'x_get_buckets'

# ======================================================================
# 1. THE FOUR GOLDEN SIGNALS (System Health & SRE Compliance)
# ======================================================================

# LATENCY: Measures the time it takes to service a request.
# Tracking latency allows for the detection of performance regressions
# and the identification of slow path bottlenecks in the API layer.
HTTP_REQUEST_DURATION = Histogram(
    "http_request_duration_seconds",
    "API response time in seconds",
    ["method", "endpoint"],
    buckets=get_buckets(0.01, 20.0, step=0.1)
)

# TRAFFIC: Measures the demand placed on the system.
# Essential for capacity planning and understanding the impact of 
# external events or automated scrapers on the platform.
HTTP_REQUESTS_TOTAL = Counter(
    "http_requests_total",
    "Total count of received HTTP requests",
    ["method", "endpoint", "status"]
)

# ERRORS: Measures the rate of requests that fail.
# High error rates are the primary indicator of system instability
# or upstream data source failures.
HTTP_REQUESTS_FAILED_TOTAL = Counter(
    "http_requests_failed_total",
    "Total count of failed HTTP requests",
    ["method", "endpoint", "error_type"]
)

# CONCURRENCY (Saturation): Measures how "full" the service is.
# Monitoring in-flight requests helps prevent cascading failures 
# caused by resource exhaustion.
IN_FLIGHT_REQUESTS = Gauge(
    "http_requests_in_flight",
    "Current number of concurrent HTTP requests being processed",
    ["method", "endpoint"]
)

# PAYLOAD SIZES: Tracks data volume per interaction.
# Unexpected spikes in request size can indicate malicious behavior 
# or misalignment between the scraper and the API.
HTTP_REQUEST_SIZE = Histogram(
    "http_request_size_bytes",
    "Size of the HTTP request payload in bytes",
    ["method", "endpoint"],
    buckets=get_buckets(128, 1048576 * 10, step=0.6)
)

# SATURATION (Infra): Low-level resource utilization.
# Tracking DB connections prevents "maximum connections reached" errors 
# during high-concurrency sync cycles.
DB_CONNECTIONS_ACTIVE = Gauge(
    "db_connections_active",
    "Number of active connections in the database pool",
    ["database"]
)

# ======================================================================
# 2. DOMAIN METRICS (Ubiquitous Language & Business Outcomes)
# ======================================================================

# BUSINESS OUTCOME: Success of the B3 Synchronization event.
# This is the primary KPI for the platform's core value proposition.
COMPANIES_SYNCED_TOTAL = Counter(
    "companies_synced_total",
    "Total count of companies processed during synchronization",
    ["status"]
)

# Alias for legacy compatibility (should be deprecated when refactoring finishes).
ENTITIES_SYNCED_TOTAL = COMPANIES_SYNCED_TOTAL

ACTIVE_SYNC_TASKS = Gauge(
    "active_sync_tasks_count",
    "Number of background synchronization tasks currently running"
)

# SYNC DURATION: Measures the efficiency of the domain sync logic.
# Long sync times directly delay data availability for downstream analysis.
SYNC_DURATION_SECONDS = Histogram(
    "sync_duration_seconds",
    "Wall-clock time spent in the synchronization use case",
    ["context"],
    buckets=get_buckets(0.1, 1800.0, step=0.3)
)

# DATA QUALITY: Measures the integrity of the information retrieved from B3.
# Parsing failures signal changes in B3's internal data formats that 
# require adaptation in the Infrastructure layer (ACL).
DATE_PARSING_FAILURES = Counter(
    "domain_date_parsing_failures_total",
    "Total occurrences of date-string parsing failures (Data Integrity KPI)",
    ["field", "source"]
)

DATA_VALIDATION_ERRORS = Counter(
    "domain_data_validation_errors_total",
    "Total business rule violations (e.g., invalid CNPJ or Ticker format)",
    ["entity", "field", "reason"]
)

# DOMAIN RESILIENCE: Tracks how the domain handles errors.
GENERIC_SYNC_ERRORS = Counter(
    "domain_sync_errors_total",
    "Total unexpected failures during the orchestration of sync tasks",
    ["type"]
)

# EXTERNAL ADAPTER PERFORMANCE: Monitored via Rate Limit Detection.
# Frequent 429s from B3 indicate that the 'max_concurrency' setting 
# is too aggressive for current infrastructure limits.
B3_RATE_LIMIT_HITS = Counter(
    "domain_b3_rate_limit_hits_total",
    "Total count of HTTP 429 (Too Many Requests) received from B3"
)

# NETWORK EFFICIENCY
NETWORK_TRANSMIT_BYTES_TOTAL = Counter(
    "network_transmit_bytes_total",
    "Accumulated network traffic transmitted in bytes",
    ["direction", "context"]
)

HTTP_RESPONSE_SIZE = Histogram(
    "http_response_size_bytes",
    "Size of the HTTP responses returned to clients/workers",
    ["method", "endpoint"],
    buckets=get_buckets(128, 1048576 * 10, step=0.6)
)

# DOMAIN SNAPSHOTS: Real-time status of the Financial Universe.
COMPANIES_BY_SECTOR = Gauge(
    "domain_companies_by_sector_count",
    "Current distribution of issuers grouped by Economic Sector",
    ["sector"]
)

COMPANIES_BY_SEGMENT = Gauge(
    "domain_companies_by_segment_count",
    "Current distribution of issuers grouped by B3 Listing Segment",
    ["segment"]
)

NEW_ISSUERS_DISCOVERED = Counter(
    "domain_new_issuers_discovered_total",
    "Count of previously unknown issuers identified in the latest sync cycle"
)

# ======================================================================
# 3. APP INFO (Deployment & Version Tracking)
# ======================================================================

# APP METADATA: Static information exported as a Gauge with value 1.
# Allows for grouping metrics by version or environment in Grafana 
# to detect if a specific deployment version introduced a regression.
APP_INFO = Gauge(
    "app_info",
    "Static metadata about the running instance (version, environment)",
    ["version", "environment"]
)

# Initialize static values at startup.
# Using 'development' as a fallback prevents empty labels if the environment 
# variable is missing in non-orchestrated environments.
env = os.getenv("APP_ENV", "development")
APP_INFO.labels(
    version=getattr(settings.app, "version", "unknown"), 
    environment=env
).set(1)
