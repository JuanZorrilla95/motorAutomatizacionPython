from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.models.invoice import Invoice
# from app.schemas.invoice import InvoiceCreate
from app.models.rule import Rule
from app.models.rule_run import RuleRun


router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db # yield  permite que otros codigos usen la sesión
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
#endpot para factura especifica
@router.post("/run/{invoice_id}")
def run_rules_for_invoice(
    invoice_id: int,
    db: Session = Depends(get_db)
):
    invoice = db.query(Invoice).filter(Invoice.id == invoice_id).first()

    if not invoice:
        return {"error": "factura no encontrada"}

    rules = db.query(Rule).filter(Rule.active == True).all()

    results = []

    for rule in rules:
        passed = False

        if rule.field == "amount":
            invoice_value = invoice.amount
            rule_value = float(rule.value)

            if rule.operator == ">":
                passed = invoice_value > rule_value
            elif rule.operator == "<":
                passed = invoice_value < rule_value
            elif rule.operator == "==":
                passed = invoice_value == rule_value

        # guardar ejecución
        run = RuleRun(
            rule_id=rule.id,
            matched_count=1 if passed else 0,
            approved=passed
        )
        db.add(run)

        # aplicar acción
        if passed and rule.action == "flag":
            invoice.status = "flagged"

        results.append({
            "rule": rule.name,
            "passed": passed
        })

    db.commit()

    return {
        "invoice_id": invoice.id,
        "status": invoice.status,
        "rules": results
    }
