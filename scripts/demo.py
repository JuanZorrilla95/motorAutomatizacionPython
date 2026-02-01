from app.core.database import SessionLocal
from app.models.rule import Rule

db = SessionLocal()

rule = Rule(
    name="Amount match",
    version=1,
    priority=1,
    config={"type": "amount_match", "tolerance": 0.01},
    active=True
)

db.add(rule)
db.commit()

print("Regla creada")
