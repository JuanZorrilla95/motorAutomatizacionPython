from fastapi import FastAPI
from app.core.database import Base, engine
import app.models

from app.api.routes.imports import router as imports_router
from app.api.routes.reconciliations import router as reconciliations_router
from app.api.routes.rules import router as rules_router
from app.api.routes import rules, invoices
app = FastAPI(title="Reconciliation Engine")

app.include_router(imports_router, prefix="/imports", tags=["Imports"])
app.include_router(reconciliations_router, prefix="/reconciliations", tags=["Reconciliations"])
app.include_router(rules_router, prefix="/rules")
app.include_router(invoices.router, prefix="/invoices", tags=["Invoices"])

# print(app.routes)

# crea tablas si no existen (dev only)
Base.metadata.create_all(bind=engine)

@app.get("/health")
def health():
    return {"status": "ok"}