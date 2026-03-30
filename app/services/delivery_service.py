from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.repositories import delivery_repository

def create_delivery(db, delivery_data):
    
    user = delivery_repository.get_user_by_id(db, delivery_data["user_id"])

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return delivery_repository.create_delivery(db, delivery_data)

def get_all_deliveries(db: Session):
    return delivery_repository.get_all_deliveries(db)