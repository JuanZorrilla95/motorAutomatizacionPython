# regla para coincidir montos
from app.services.rules.base import RuleHandler

class AmountMatchRule(RuleHandler):

    def apply(self, invoice, movement, config):
        tolerance = config.get("tolerance", 0.0)
        diff = abs(invoice.amount - movement.amount)

        if diff <= tolerance:
            return {
                "matched": True,
                "match_type": "amount",
                "difference": diff
            }

        return {"matched": False}
