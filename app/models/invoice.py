from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime
from app.core.database import Base
#cargado de invoices/facturas
class Invoice(Base):
    __tablename__ = "invoices"

    id = Column(Integer, primary_key=True)
    external_id = Column(String, index=True)
    customer_name = Column(String)
    amount = Column(Float)
    description = Column(String)
    currency = Column(String)
    status = Column(String, default="pendiente")
    created_at = Column(DateTime, default=datetime.utcnow)
