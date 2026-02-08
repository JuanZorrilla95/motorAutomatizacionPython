from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from app.models.rule_run import RuleRun
from app.models.rule import Rule
from app.models.invoice import Invoice
from app.schemas.rule import RuleCreate, RuleOut
from app.core.database import SessionLocal
router = APIRouter()

# --- dependencia DB ---
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/ping")
def ping():
    return {"ok": True}

# -------------------------
# Crear regla
# -------------------------
@router.post("/config", response_model=RuleOut)
def create_rule(rule: RuleCreate, db: Session = Depends(get_db)):
    r = Rule(**rule.model_dump())
    db.add(r)
    db.commit()
    db.refresh(r)
    return r


# -------------------------
# Ejecutar reglas (todas las invoices)
# -------------------------
@router.post("/run")
def run_all_rules(db: Session = Depends(get_db)):
    rules = db.query(Rule).filter(Rule.active == True).all()
    invoices = db.query(Invoice).all()

    results = []

    for rule in rules:
        matched_invoices = []

        for inv in invoices:
            if rule.field == "amount":
                value = float(rule.value)

                if rule.operator == ">" and inv.amount > value:
                    matched_invoices.append(inv.id)
                elif rule.operator == "<" and inv.amount < value:
                    matched_invoices.append(inv.id)
                elif rule.operator == "==" and inv.amount == value:
                    matched_invoices.append(inv.id)

        results.append({
            "rule_id": rule.id,
            "rule_name": rule.name,
            "action": rule.action,
            "matched_invoices": matched_invoices
        })

    return results


# -------------------------
# Ejecutar reglas para una invoice
# -------------------------
@router.post("/run/{invoice_id}") #rules.action define que hacer, rule_runs.action define que se ejecutó
def run_rules_for_invoice(
    invoice_id: int,
    db: Session = Depends(get_db)
):
    invoice = db.query(Invoice).filter(Invoice.id == invoice_id).first()
    if not invoice:
        return {"error": "Factura no encontrada"}

    rules = db.query(Rule).filter(Rule.active == True).all()
    applied_actions = []
    # results = []

    for rule in rules:
        matched = False

        if rule.field == "amount":
            # invoice_value = invoice.amount
            # rule_value = float(rule.value)

            if rule.operator == ">" and invoice.amount > float(rule.value):
                matched = True
            # if rule.operator == "<" and invoice.amount < float(rule.value):
            #     matched = True
            # if rule.operator == "==" and invoice.amount == float(rule.value):
            #     matched = True
        if matched:
            #  aplica acción
            if rule.action == "flag":
                invoice.status = "flagged"
            elif rule.action == "approve":
                invoice.status = "approved"
            elif rule.action == "reject":
                invoice.status = "rejected"

            run = RuleRun(
                invoice_id=invoice.id,
                rule_id=rule.id,
                action=rule.action, #if matched else None,
                matched=True
            )

            db.add(run)

            applied_actions.append(rule.action)
        # if matched:
        #     results.append({
        #         "rule": rule.name,
        #         "action": rule.action
        #     })

    db.commit()

    return {
        "invoice_id": invoice.id,
        "final_status": invoice.status,
        "actions_applied": applied_actions
        # "matched_rules": results
    }

