#Motor de conciliación (core)
from app.core.database import SessionLocal
from app.models.invoice import Invoice
from app.models.bank_movement import BankMovement
from app.models.rule import Rule
from app.services.rules.engine import RulesEngine

def run_reconciliation():
    db = SessionLocal()

    invoices = db.query(Invoice).filter(Invoice.status == "pending").all()
    movements = db.query(BankMovement).filter(BankMovement.processed == False).all()
    rules = db.query(Rule).all().filter(Rule.active == True).all()

    engine = RulesEngine(rules)

    for move in movements:
        for inv in invoices:
            result = engine.evaluate(inv, move)

            if result["matched"]:
                inv.status = "paid"
                move.processed = True
                break

    db.commit()
    db.close()
