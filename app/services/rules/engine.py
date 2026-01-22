# motor de reglas
from app.services.rules.registry import RULE_REGISTRY

class RulesEngine:

    def __init__(self, rules):
        self.rules = sorted(rules, key=lambda r: r.priority)

    def evaluate(self, invoice, movement):
        for rule in self.rules:
            handler = RULE_REGISTRY.get(rule.config["type"])
            if not handler:
                continue

            result = handler.apply(invoice, movement, rule.config)

            if result.get("matched"):
                return result

        return {"matched": False}
