from app.services.rules.engine import RulesEngine
from app.services.rules.amount_match import AmountMatchRule
from app.models.rule import Rule

class FakeInvoice:
    def __init__(self, amount):
        self.amount = amount

class FakeMovement:
    def __init__(self, amount):
        self.amount = amount

def test_amount_match_rule_exact():
    rule = Rule(
        name="amount match",
        version=1,
        priority=1,
        config={"type": "amount_match", "tolerance": 0.01},
        active=True
    )

    engine = RulesEngine([rule])

    invoice = FakeInvoice(amount=100.00)
    movement = FakeMovement(amount=100.00)

    result = engine.evaluate(invoice, movement)

    assert result["matched"] is True
    assert result["match_type"] == "amount"

# test negativo
def test_amount_match_rule_fail():
    rule = Rule(
        name="amount match",
        version=1,
        priority=1,
        config={"type": "amount_match", "tolerance": 0.01},
        active=True
    )

    engine = RulesEngine([rule])

    invoice = FakeInvoice(amount=100.00)
    movement = FakeMovement(amount=110.00)

    result = engine.evaluate(invoice, movement)

    assert result["matched"] is False

