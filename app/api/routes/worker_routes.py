from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.depends import get_db
from app.schemas.worker_schema import WorkerCreate, WorkerResponse
from app.services import worker_service

router = APIRouter()

@router.post("/workers", response_model=WorkerResponse)
def create_worker(worker: WorkerCreate, db: Session = Depends(get_db)):
    return worker_service.create_worker(db, worker.dict())

@router.get("/workers", response_model=list[WorkerResponse])
def get_workers(db: Session = Depends(get_db)):
    return worker_service.get_all_workers(db)