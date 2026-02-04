from pydantic import BaseModel

class InvoiceCreate(BaseModel):
    amount: int
    description: str | None = None
