from sqlalchemy import Column, DateTime, func

class AuditMixin:
    """
    Injeta metadados de observabilidade e ciclo de vida em qualquer tabela.
    Garante consistência absoluta para telemetria SRE.
    """
    timestamp = func.now()
    created_at = Column(DateTime(timezone=True), default=timestamp, nullable=False)
    updated_at = Column(DateTime(timezone=True), default=timestamp, onupdate=timestamp, nullable=False)
    ingested_at = Column(DateTime(timezone=True), default=timestamp, nullable=False)
