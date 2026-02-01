from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.rule import Rule
from app.models.invoice import Invoice
from app.services.rule_engine import apply_rule

router = APIRouter(prefix="/reconcile", tags=["Reconcile"])

@router.post("/")
def reconcile(db: Session = Depends(get_db)):
    invoices = db.query(Invoice).filter(Invoice.status == "pending").all()
    rules = db.query(Rule).filter(Rule.active == True).all()

    results = []

    for invoice in invoices:
        for rule in rules:
            action = apply_rule(invoice, rule)
            if action:
                invoice.status = action
                results.append({
                    "invoice_id": invoice.id,
                    "rule": rule.name,
                    "action": action
                })

    db.commit()
    return results
