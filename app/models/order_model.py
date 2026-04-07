from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.database.session import Base


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)  # we have named it id instead of order_id to maintain consistency with SQLAlchemy's default primary key naming convention. if we want to make it order_id we can do it by using the relationship i worker and other to orders.id to orders.order_id by renanming it

    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    worker_id = Column(Integer, ForeignKey("workers.id"), nullable=True)

    pickup_location = Column(String, nullable=False)
    delivery_location = Column(String, nullable=False)

    pickup_latitude = Column(Float, nullable=False)
    pickup_longitude = Column(Float, nullable=False)

    delivery_latitude = Column(Float, nullable=False)
    delivery_longitude = Column(Float, nullable=False)

    status = Column(String, default="PENDING", index=True)

    user = relationship("User", back_populates="orders")
    worker = relationship("Worker", back_populates="orders")

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    