from sqlalchemy import Column, DateTime, func

class AuditMixin:
    """
    Injeta metadados de observabilidade e ciclo de vida em qualquer tabela.
    Garante consistência absoluta para telemetria SRE.
    """
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), server_onupdate=func.now(), nullable=False)
    ingested_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
