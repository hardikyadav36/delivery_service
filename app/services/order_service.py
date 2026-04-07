from sqlalchemy.orm import Session
from app.repositories import order_repository


# ✅ Create Order
def create_order(db: Session, order_data):
    return order_repository.create_order(db, order_data.dict())


# ✅ Get All Orders
def get_orders(db: Session):
    return order_repository.get_all_orders(db)


# ✅ Get Single Order
def get_order_by_id(db: Session, order_id: int):
    return order_repository.get_order_by_id(db, order_id)