# c evaluacion de la regla queda guardada
from sqlalchemy import Column, Integer, DateTime, Boolean, JSON, ForeignKey, String
from datetime import datetime
from app.core.database import Base
# la BD tiene que reflejar el modelo SIEMPRE
class RuleRun(Base):
    __tablename__ = "rule_runs"

    id = Column(Integer, primary_key=True)
    invoice_id = Column(JSON, nullable=False)
    rule_id = Column(Integer, ForeignKey("rules.id"), nullable=False)
    action = Column(String, nullable=False)
    matched = Column(Boolean, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    # matched_count = Column(Integer, nullable=False)

