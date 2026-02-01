from app.models.rule import Rule
from app.models.rule_run import RuleRun

class RulesEngine:
    def __init__(self, db):
        self.db = db

    def _evaluate_rule(self, rule: Rule, data: dict) -> bool:
        field_value = data.get(rule.field)

        if field_value is None:
            return False

        if rule.operator == ">":
            return float(field_value) > float(rule.value)

        if rule.operator == "<":
            return float(field_value) < float(rule.value)

        if rule.operator == "==":
            return str(field_value) == rule.value

        if rule.operator == "in":
            return str(field_value) in rule.value.split(",")

        return False

    def evaluate(self, invoice: dict):
        rules = self.db.query(Rule).filter(Rule.active == True).all()
        failed = []

        for rule in rules:
            if not self._evaluate_rule(rule, invoice):
                failed.append(f"{rule.field} {rule.operator} {rule.value}")

        approved = len(failed) == 0

        run = RuleRun(
            input_data=invoice,
            approved=approved,
            reasons=failed
        )

        self.db.add(run)
        self.db.commit()

        return {
            "approved": approved,
            "reasons": failed
        }
