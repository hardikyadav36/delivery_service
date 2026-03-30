from sqlalchemy.orm import Session
from app.models.delivery_model import Delivery

def create_delivery(db: Session, data: dict):
    delivery = Delivery(**data)
    db.add(delivery)
    db.commit()
    db.refresh(delivery)
    return delivery

def get_all_deliveries(db: Session):
    return db.query(Delivery).all()
def get_user_by_id(db: Session, user_id: int):
    return db.query(Delivery).filter(Delivery.user_id == user_id).first()