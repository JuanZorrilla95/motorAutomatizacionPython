from fastapi import APIRouter, UploadFile, Depends
from sqlalchemy.orm import Session
from app.api.dependencies import get_db
from app.services.import_service import import_invoices

router = APIRouter()

@router.post("/invoices")
def upload_invoices(file: UploadFile, db: Session = Depends(get_db)):
    imported = import_invoices(file, db)
    return {"imported": imported}
