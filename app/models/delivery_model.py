from sqlalchemy import Column, Integer, String, ForeignKey, Enum as SqlEnum
from app.database.session import Base
from app.models.delivery_enum import DeliveryStatus

class Delivery(Base):
    __tablename__ = "deliveries"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    pickup_location = Column(String, nullable=False)
    drop_location = Column(String, nullable=False)
    status = Column(SqlEnum(DeliveryStatus), default=DeliveryStatus.PENDING)