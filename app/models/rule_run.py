# c evaluacion de la regla queda guardada
from sqlalchemy import Column, Integer, DateTime, Boolean, JSON
from datetime import datetime
from app.core.database import Base

class RuleRun(Base):
    __tablename__ = "rule_runs"

    id = Column(Integer, primary_key=True)
    input_data = Column(JSON, nullable=False)
    approved = Column(Boolean, nullable=False)
    reasons = Column(JSON, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
