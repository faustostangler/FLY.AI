from abc import ABC, abstractmethod

class TelemetryPort(ABC):
    @abstractmethod
    def increment_active_sync_tasks(self) -> None:
        pass

    @abstractmethod
    def decrement_active_sync_tasks(self) -> None:
        pass

    @abstractmethod
    def increment_companies_synced(self, count: int, status: str) -> None:
        pass

    @abstractmethod
    def set_companies_by_sector(self, sector: str, count: int) -> None:
        pass

    @abstractmethod
    def set_companies_by_segment(self, segment: str, count: int) -> None:
        pass

    @abstractmethod
    def observe_sync_duration(self, context: str, duration: float) -> None:
        pass

    @abstractmethod
    def increment_date_parsing_failures(self, field: str, source: str) -> None:
        pass

    @abstractmethod
    def increment_b3_rate_limit_hits(self) -> None:
        pass

    @abstractmethod
    def increment_network_transmit_bytes(self, direction: str, context: str, payload_size: int) -> None:
        pass

    @abstractmethod
    def increment_data_validation_error(self, entity: str, field: str, reason: str) -> None:
        pass

    @abstractmethod
    def increment_generic_sync_error(self, type: str) -> None:
        pass
