# Disparar conciliación
from fastapi import APIRouter
from app.workers.tasks import reconcile_task

router = APIRouter()

@router.post("/run")
def run_reconciliation():
    task = reconcile_task.delay()
    return {"task_id": task.id, "status": "running"}
