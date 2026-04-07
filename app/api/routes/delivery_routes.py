from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.depends import get_db
from app.schemas.delivery_schema import DeliveryCreate, DeliveryResponse
from app.services import delivery_service

router = APIRouter(prefix="/delivery", tags=["Delivery"])

@router.post("/deliveries", response_model=DeliveryResponse)
def create_delivery(delivery: DeliveryCreate, db: Session = Depends(get_db)):
    return delivery_service.create_delivery(db, delivery.dict())

@router.get("/deliveries", response_model=list[DeliveryResponse])
def get_deliveries(db: Session = Depends(get_db)):
    return delivery_service.get_all_deliveries(db)