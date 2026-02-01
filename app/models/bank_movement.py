from sqlalchemy import Column, Integer
from app.core.database import Base

class BankMovement(Base):
    __tablename__ = "bank_movements"

    id = Column(Integer, primary_key=True)
