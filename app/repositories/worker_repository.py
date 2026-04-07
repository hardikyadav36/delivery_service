from sqlalchemy.orm import Session
from app.models.worker_model import Worker

def create_worker(db: Session, data: dict):
    worker = Worker(**data)
    db.add(worker)
    db.commit()
    db.refresh(worker)
    return worker

def get_all_workers(db: Session):
    return db.query(Worker).all()

def get_available_worker(db: Session):
    return db.query(Worker).filter(Worker.is_available == True).all()