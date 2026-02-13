#motor de reglas
def apply_rule(invoice, rule):
    if rule.condition.startswith("amount >"):
        limit = int(rule.condition.split(">")[1].strip())
        if invoice.amount > limit:
            return rule.action
    return None
