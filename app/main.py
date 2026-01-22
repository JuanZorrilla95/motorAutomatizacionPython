from fastapi import FastAPI
from app.api.routes import imports, reconciliations, reports, rules

app = FastAPI(title="Reconciliation Engine")

app.include_router(imports.router, prefix="/imports", tags=["Imports"])
app.include_router(reconciliations.router, prefix="/reconciliations", tags=["Reconciliations"])
app.include_router(reports.router, prefix="/reports", tags=["Reports"])
app.include_router(rules.router, prefix="/rules", tags=["Rules"])
