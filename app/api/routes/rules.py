# endpoints para reglas
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.api.dependencies import get_db
from app.models.rule import Rule

router = APIRouter()

@router.get("/")
def list_rules(db: Session = Depends(get_db)):
    return db.query(Rule).all()

@router.post("/")
def create_rule(rule: dict, db: Session = Depends(get_db)):
    new_rule = Rule(**rule)
    db.add(new_rule)
    db.commit()
    return new_rule
