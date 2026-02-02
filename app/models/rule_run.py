# c evaluacion de la regla queda guardada
from sqlalchemy import Column, Integer, DateTime, Boolean, JSON, ForeignKey
from datetime import datetime
from app.core.database import Base
# la BD tiene que reflejar el modelo SIEMPRE
class RuleRun(Base):
    __tablename__ = "rule_runs"

    id = Column(Integer, primary_key=True)
    rule_id = Column(Integer, ForeignKey("rules.id"), nullable=False)
    matched_count = Column(Integer, nullable=False)
    # input_data = Column(JSON, nullable=False)
    # approved = Column(Boolean, nullable=False)
    # reasons = Column(JSON, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
