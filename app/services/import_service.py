# Importación de CSV
import csv
from io import StringIO
from app.models.invoice import Invoice

def import_invoices(file, db):
    content = file.file.read().decode("utf-8")
    reader = csv.DictReader(StringIO(content))

    count = 0
    for row in reader:
        invoice = Invoice(
            external_id=row["external_id"],
            customer_name=row["customer"],
            amount=float(row["amount"]),
            currency=row["currency"]
        )
        db.add(invoice)
        count += 1

    db.commit()
    return count
