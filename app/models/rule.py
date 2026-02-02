from sqlalchemy import Column, Integer, String, Boolean
from app.core.database import Base

class Rule(Base):
    __tablename__ = "rules"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    condition = Column(String, nullable=True)
    action = Column(String, nullable=True)
    # rule_id = Column(String, unique=True, index=True, nullable=False)
    active = Column(Boolean, default=True)
    field = Column(String, nullable=False)
    operator = Column(String, nullable=False)
    value = Column(String, nullable=False)
