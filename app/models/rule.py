# reglas
from sqlalchemy import Column, Integer, String, Boolean, DateTime, JSON
from datetime import datetime
from app.core.database import Base

class Rule(Base):
    __tablename__ = "rules"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    version = Column(Integer, nullable=False)
    priority = Column(Integer, default=100)
    config = Column(JSON, nullable=False)
    active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
