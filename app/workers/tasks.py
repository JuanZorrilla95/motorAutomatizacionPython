from app.core.celery_app import celery_app
from app.services.reconciliation_engine import run_reconciliation

@celery_app.task(bind=True, autoretry_for=(Exception,), retry_backoff=10)
def reconcile_task(self):
    run_reconciliation()
