from fastapi import APIRouter
from fastapi import Depends
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

@router.post("/runs")
def run_rules(db: Session = Depends(get_db)):
    rules = db.query(Rule).filter(Rule.active == True).all()

    results = []

    for rule in rules:
        # ejemplo simple: amount > value
        if rule.operator == ">":
            matched = db.query(Invoice).filter(
                Invoice.amount > float(rule.value)
            ).count()
        else:
            matched = 0

        run = RuleRun(
            rule_id=rule.id,
            matched_count=matched
        )
        db.add(run)
        results.append({
            "rule_id": rule.id,
            "matched": matched
        })

    db.commit()
    return results


# endpoints para gestionar las reglas
@router.post("/config", response_model=RuleOut)
def create_rule(rule: RuleCreate, db: Session = Depends(get_db)):
    r = Rule(**rule.model_dump())
    db.add(r)
    db.commit()
    db.refresh(r)
    return r
