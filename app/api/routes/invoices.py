from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.models.invoice import Invoice
from app.schemas.invoice import InvoiceCreate

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def create_invoice(data: dict, db: Session = Depends(get_db)):
    invoice = Invoice(**data)
    db.add(invoice)
    db.commit()
    db.refresh(invoice)
    return invoice

@router.get("/")
def list_invoices(db: Session = Depends(get_db)):
    invoices = db.query(Invoice).all()
    return invoices
    