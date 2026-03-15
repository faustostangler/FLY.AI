from typing import Optional
from shared.domain.ports.telemetry_port import TelemetryPort
from shared.infrastructure.monitoring.metrics import (
    ACTIVE_SYNC_TASKS,
    COMPANIES_SYNCED_TOTAL,
    COMPANIES_BY_SECTOR,
    COMPANIES_BY_SEGMENT,
    SYNC_DURATION_SECONDS,
    DATE_PARSING_FAILURES,
    B3_RATE_LIMIT_HITS,
    NETWORK_TRANSMIT_BYTES_TOTAL,
    DATA_VALIDATION_ERRORS,
    GENERIC_SYNC_ERRORS,
)
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

class PrometheusTelemetryAdapter(TelemetryPort):
    def increment_active_sync_tasks(self) -> None:
        ACTIVE_SYNC_TASKS.inc()

    def decrement_active_sync_tasks(self) -> None:
        ACTIVE_SYNC_TASKS.dec()

    def increment_companies_synced(self, count: int, status: str) -> None:
        args = [count, status]# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁPrometheusTelemetryAdapterǁincrement_companies_synced__mutmut_orig'), object.__getattribute__(self, 'xǁPrometheusTelemetryAdapterǁincrement_companies_synced__mutmut_mutants'), args, kwargs, self)

    def xǁPrometheusTelemetryAdapterǁincrement_companies_synced__mutmut_orig(self, count: int, status: str) -> None:
        COMPANIES_SYNCED_TOTAL.labels(status=status).inc(count)

    def xǁPrometheusTelemetryAdapterǁincrement_companies_synced__mutmut_1(self, count: int, status: str) -> None:
        COMPANIES_SYNCED_TOTAL.labels(status=status).inc(None)

    def xǁPrometheusTelemetryAdapterǁincrement_companies_synced__mutmut_2(self, count: int, status: str) -> None:
        COMPANIES_SYNCED_TOTAL.labels(status=None).inc(count)
    
    xǁPrometheusTelemetryAdapterǁincrement_companies_synced__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁPrometheusTelemetryAdapterǁincrement_companies_synced__mutmut_1': xǁPrometheusTelemetryAdapterǁincrement_companies_synced__mutmut_1, 
        'xǁPrometheusTelemetryAdapterǁincrement_companies_synced__mutmut_2': xǁPrometheusTelemetryAdapterǁincrement_companies_synced__mutmut_2
    }
    xǁPrometheusTelemetryAdapterǁincrement_companies_synced__mutmut_orig.__name__ = 'xǁPrometheusTelemetryAdapterǁincrement_companies_synced'

    def set_companies_by_sector(self, sector: str, count: int) -> None:
        args = [sector, count]# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁPrometheusTelemetryAdapterǁset_companies_by_sector__mutmut_orig'), object.__getattribute__(self, 'xǁPrometheusTelemetryAdapterǁset_companies_by_sector__mutmut_mutants'), args, kwargs, self)

    def xǁPrometheusTelemetryAdapterǁset_companies_by_sector__mutmut_orig(self, sector: str, count: int) -> None:
        COMPANIES_BY_SECTOR.labels(sector=sector).set(count)

    def xǁPrometheusTelemetryAdapterǁset_companies_by_sector__mutmut_1(self, sector: str, count: int) -> None:
        COMPANIES_BY_SECTOR.labels(sector=sector).set(None)

    def xǁPrometheusTelemetryAdapterǁset_companies_by_sector__mutmut_2(self, sector: str, count: int) -> None:
        COMPANIES_BY_SECTOR.labels(sector=None).set(count)
    
    xǁPrometheusTelemetryAdapterǁset_companies_by_sector__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁPrometheusTelemetryAdapterǁset_companies_by_sector__mutmut_1': xǁPrometheusTelemetryAdapterǁset_companies_by_sector__mutmut_1, 
        'xǁPrometheusTelemetryAdapterǁset_companies_by_sector__mutmut_2': xǁPrometheusTelemetryAdapterǁset_companies_by_sector__mutmut_2
    }
    xǁPrometheusTelemetryAdapterǁset_companies_by_sector__mutmut_orig.__name__ = 'xǁPrometheusTelemetryAdapterǁset_companies_by_sector'

    def set_companies_by_segment(self, segment: str, count: int) -> None:
        args = [segment, count]# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁPrometheusTelemetryAdapterǁset_companies_by_segment__mutmut_orig'), object.__getattribute__(self, 'xǁPrometheusTelemetryAdapterǁset_companies_by_segment__mutmut_mutants'), args, kwargs, self)

    def xǁPrometheusTelemetryAdapterǁset_companies_by_segment__mutmut_orig(self, segment: str, count: int) -> None:
        COMPANIES_BY_SEGMENT.labels(segment=segment).set(count)

    def xǁPrometheusTelemetryAdapterǁset_companies_by_segment__mutmut_1(self, segment: str, count: int) -> None:
        COMPANIES_BY_SEGMENT.labels(segment=segment).set(None)

    def xǁPrometheusTelemetryAdapterǁset_companies_by_segment__mutmut_2(self, segment: str, count: int) -> None:
        COMPANIES_BY_SEGMENT.labels(segment=None).set(count)
    
    xǁPrometheusTelemetryAdapterǁset_companies_by_segment__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁPrometheusTelemetryAdapterǁset_companies_by_segment__mutmut_1': xǁPrometheusTelemetryAdapterǁset_companies_by_segment__mutmut_1, 
        'xǁPrometheusTelemetryAdapterǁset_companies_by_segment__mutmut_2': xǁPrometheusTelemetryAdapterǁset_companies_by_segment__mutmut_2
    }
    xǁPrometheusTelemetryAdapterǁset_companies_by_segment__mutmut_orig.__name__ = 'xǁPrometheusTelemetryAdapterǁset_companies_by_segment'

    def observe_sync_duration(self, context: str, duration: float) -> None:
        args = [context, duration]# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁPrometheusTelemetryAdapterǁobserve_sync_duration__mutmut_orig'), object.__getattribute__(self, 'xǁPrometheusTelemetryAdapterǁobserve_sync_duration__mutmut_mutants'), args, kwargs, self)

    def xǁPrometheusTelemetryAdapterǁobserve_sync_duration__mutmut_orig(self, context: str, duration: float) -> None:
        SYNC_DURATION_SECONDS.labels(context=context).observe(duration)

    def xǁPrometheusTelemetryAdapterǁobserve_sync_duration__mutmut_1(self, context: str, duration: float) -> None:
        SYNC_DURATION_SECONDS.labels(context=context).observe(None)

    def xǁPrometheusTelemetryAdapterǁobserve_sync_duration__mutmut_2(self, context: str, duration: float) -> None:
        SYNC_DURATION_SECONDS.labels(context=None).observe(duration)
    
    xǁPrometheusTelemetryAdapterǁobserve_sync_duration__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁPrometheusTelemetryAdapterǁobserve_sync_duration__mutmut_1': xǁPrometheusTelemetryAdapterǁobserve_sync_duration__mutmut_1, 
        'xǁPrometheusTelemetryAdapterǁobserve_sync_duration__mutmut_2': xǁPrometheusTelemetryAdapterǁobserve_sync_duration__mutmut_2
    }
    xǁPrometheusTelemetryAdapterǁobserve_sync_duration__mutmut_orig.__name__ = 'xǁPrometheusTelemetryAdapterǁobserve_sync_duration'

    def increment_date_parsing_failures(self, field: str, source: str) -> None:
        args = [field, source]# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁPrometheusTelemetryAdapterǁincrement_date_parsing_failures__mutmut_orig'), object.__getattribute__(self, 'xǁPrometheusTelemetryAdapterǁincrement_date_parsing_failures__mutmut_mutants'), args, kwargs, self)

    def xǁPrometheusTelemetryAdapterǁincrement_date_parsing_failures__mutmut_orig(self, field: str, source: str) -> None:
        DATE_PARSING_FAILURES.labels(field=field, source=source).inc()

    def xǁPrometheusTelemetryAdapterǁincrement_date_parsing_failures__mutmut_1(self, field: str, source: str) -> None:
        DATE_PARSING_FAILURES.labels(field=None, source=source).inc()

    def xǁPrometheusTelemetryAdapterǁincrement_date_parsing_failures__mutmut_2(self, field: str, source: str) -> None:
        DATE_PARSING_FAILURES.labels(field=field, source=None).inc()

    def xǁPrometheusTelemetryAdapterǁincrement_date_parsing_failures__mutmut_3(self, field: str, source: str) -> None:
        DATE_PARSING_FAILURES.labels(source=source).inc()

    def xǁPrometheusTelemetryAdapterǁincrement_date_parsing_failures__mutmut_4(self, field: str, source: str) -> None:
        DATE_PARSING_FAILURES.labels(field=field, ).inc()
    
    xǁPrometheusTelemetryAdapterǁincrement_date_parsing_failures__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁPrometheusTelemetryAdapterǁincrement_date_parsing_failures__mutmut_1': xǁPrometheusTelemetryAdapterǁincrement_date_parsing_failures__mutmut_1, 
        'xǁPrometheusTelemetryAdapterǁincrement_date_parsing_failures__mutmut_2': xǁPrometheusTelemetryAdapterǁincrement_date_parsing_failures__mutmut_2, 
        'xǁPrometheusTelemetryAdapterǁincrement_date_parsing_failures__mutmut_3': xǁPrometheusTelemetryAdapterǁincrement_date_parsing_failures__mutmut_3, 
        'xǁPrometheusTelemetryAdapterǁincrement_date_parsing_failures__mutmut_4': xǁPrometheusTelemetryAdapterǁincrement_date_parsing_failures__mutmut_4
    }
    xǁPrometheusTelemetryAdapterǁincrement_date_parsing_failures__mutmut_orig.__name__ = 'xǁPrometheusTelemetryAdapterǁincrement_date_parsing_failures'

    def increment_b3_rate_limit_hits(self) -> None:
        B3_RATE_LIMIT_HITS.inc()

    def increment_network_transmit_bytes(self, direction: str, context: str, payload_size: int) -> None:
        args = [direction, context, payload_size]# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁPrometheusTelemetryAdapterǁincrement_network_transmit_bytes__mutmut_orig'), object.__getattribute__(self, 'xǁPrometheusTelemetryAdapterǁincrement_network_transmit_bytes__mutmut_mutants'), args, kwargs, self)

    def xǁPrometheusTelemetryAdapterǁincrement_network_transmit_bytes__mutmut_orig(self, direction: str, context: str, payload_size: int) -> None:
        NETWORK_TRANSMIT_BYTES_TOTAL.labels(direction=direction, context=context).inc(payload_size)

    def xǁPrometheusTelemetryAdapterǁincrement_network_transmit_bytes__mutmut_1(self, direction: str, context: str, payload_size: int) -> None:
        NETWORK_TRANSMIT_BYTES_TOTAL.labels(direction=direction, context=context).inc(None)

    def xǁPrometheusTelemetryAdapterǁincrement_network_transmit_bytes__mutmut_2(self, direction: str, context: str, payload_size: int) -> None:
        NETWORK_TRANSMIT_BYTES_TOTAL.labels(direction=None, context=context).inc(payload_size)

    def xǁPrometheusTelemetryAdapterǁincrement_network_transmit_bytes__mutmut_3(self, direction: str, context: str, payload_size: int) -> None:
        NETWORK_TRANSMIT_BYTES_TOTAL.labels(direction=direction, context=None).inc(payload_size)

    def xǁPrometheusTelemetryAdapterǁincrement_network_transmit_bytes__mutmut_4(self, direction: str, context: str, payload_size: int) -> None:
        NETWORK_TRANSMIT_BYTES_TOTAL.labels(context=context).inc(payload_size)

    def xǁPrometheusTelemetryAdapterǁincrement_network_transmit_bytes__mutmut_5(self, direction: str, context: str, payload_size: int) -> None:
        NETWORK_TRANSMIT_BYTES_TOTAL.labels(direction=direction, ).inc(payload_size)
    
    xǁPrometheusTelemetryAdapterǁincrement_network_transmit_bytes__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁPrometheusTelemetryAdapterǁincrement_network_transmit_bytes__mutmut_1': xǁPrometheusTelemetryAdapterǁincrement_network_transmit_bytes__mutmut_1, 
        'xǁPrometheusTelemetryAdapterǁincrement_network_transmit_bytes__mutmut_2': xǁPrometheusTelemetryAdapterǁincrement_network_transmit_bytes__mutmut_2, 
        'xǁPrometheusTelemetryAdapterǁincrement_network_transmit_bytes__mutmut_3': xǁPrometheusTelemetryAdapterǁincrement_network_transmit_bytes__mutmut_3, 
        'xǁPrometheusTelemetryAdapterǁincrement_network_transmit_bytes__mutmut_4': xǁPrometheusTelemetryAdapterǁincrement_network_transmit_bytes__mutmut_4, 
        'xǁPrometheusTelemetryAdapterǁincrement_network_transmit_bytes__mutmut_5': xǁPrometheusTelemetryAdapterǁincrement_network_transmit_bytes__mutmut_5
    }
    xǁPrometheusTelemetryAdapterǁincrement_network_transmit_bytes__mutmut_orig.__name__ = 'xǁPrometheusTelemetryAdapterǁincrement_network_transmit_bytes'

    def increment_data_validation_error(self, entity: str, field: str, reason: str) -> None:
        args = [entity, field, reason]# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁPrometheusTelemetryAdapterǁincrement_data_validation_error__mutmut_orig'), object.__getattribute__(self, 'xǁPrometheusTelemetryAdapterǁincrement_data_validation_error__mutmut_mutants'), args, kwargs, self)

    def xǁPrometheusTelemetryAdapterǁincrement_data_validation_error__mutmut_orig(self, entity: str, field: str, reason: str) -> None:
        DATA_VALIDATION_ERRORS.labels(entity=entity, field=field, reason=reason).inc()

    def xǁPrometheusTelemetryAdapterǁincrement_data_validation_error__mutmut_1(self, entity: str, field: str, reason: str) -> None:
        DATA_VALIDATION_ERRORS.labels(entity=None, field=field, reason=reason).inc()

    def xǁPrometheusTelemetryAdapterǁincrement_data_validation_error__mutmut_2(self, entity: str, field: str, reason: str) -> None:
        DATA_VALIDATION_ERRORS.labels(entity=entity, field=None, reason=reason).inc()

    def xǁPrometheusTelemetryAdapterǁincrement_data_validation_error__mutmut_3(self, entity: str, field: str, reason: str) -> None:
        DATA_VALIDATION_ERRORS.labels(entity=entity, field=field, reason=None).inc()

    def xǁPrometheusTelemetryAdapterǁincrement_data_validation_error__mutmut_4(self, entity: str, field: str, reason: str) -> None:
        DATA_VALIDATION_ERRORS.labels(field=field, reason=reason).inc()

    def xǁPrometheusTelemetryAdapterǁincrement_data_validation_error__mutmut_5(self, entity: str, field: str, reason: str) -> None:
        DATA_VALIDATION_ERRORS.labels(entity=entity, reason=reason).inc()

    def xǁPrometheusTelemetryAdapterǁincrement_data_validation_error__mutmut_6(self, entity: str, field: str, reason: str) -> None:
        DATA_VALIDATION_ERRORS.labels(entity=entity, field=field, ).inc()
    
    xǁPrometheusTelemetryAdapterǁincrement_data_validation_error__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁPrometheusTelemetryAdapterǁincrement_data_validation_error__mutmut_1': xǁPrometheusTelemetryAdapterǁincrement_data_validation_error__mutmut_1, 
        'xǁPrometheusTelemetryAdapterǁincrement_data_validation_error__mutmut_2': xǁPrometheusTelemetryAdapterǁincrement_data_validation_error__mutmut_2, 
        'xǁPrometheusTelemetryAdapterǁincrement_data_validation_error__mutmut_3': xǁPrometheusTelemetryAdapterǁincrement_data_validation_error__mutmut_3, 
        'xǁPrometheusTelemetryAdapterǁincrement_data_validation_error__mutmut_4': xǁPrometheusTelemetryAdapterǁincrement_data_validation_error__mutmut_4, 
        'xǁPrometheusTelemetryAdapterǁincrement_data_validation_error__mutmut_5': xǁPrometheusTelemetryAdapterǁincrement_data_validation_error__mutmut_5, 
        'xǁPrometheusTelemetryAdapterǁincrement_data_validation_error__mutmut_6': xǁPrometheusTelemetryAdapterǁincrement_data_validation_error__mutmut_6
    }
    xǁPrometheusTelemetryAdapterǁincrement_data_validation_error__mutmut_orig.__name__ = 'xǁPrometheusTelemetryAdapterǁincrement_data_validation_error'

    def increment_generic_sync_error(self, type: str) -> None:
        args = [type]# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁPrometheusTelemetryAdapterǁincrement_generic_sync_error__mutmut_orig'), object.__getattribute__(self, 'xǁPrometheusTelemetryAdapterǁincrement_generic_sync_error__mutmut_mutants'), args, kwargs, self)

    def xǁPrometheusTelemetryAdapterǁincrement_generic_sync_error__mutmut_orig(self, type: str) -> None:
        GENERIC_SYNC_ERRORS.labels(type=type).inc()

    def xǁPrometheusTelemetryAdapterǁincrement_generic_sync_error__mutmut_1(self, type: str) -> None:
        GENERIC_SYNC_ERRORS.labels(type=None).inc()
    
    xǁPrometheusTelemetryAdapterǁincrement_generic_sync_error__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁPrometheusTelemetryAdapterǁincrement_generic_sync_error__mutmut_1': xǁPrometheusTelemetryAdapterǁincrement_generic_sync_error__mutmut_1
    }
    xǁPrometheusTelemetryAdapterǁincrement_generic_sync_error__mutmut_orig.__name__ = 'xǁPrometheusTelemetryAdapterǁincrement_generic_sync_error'
