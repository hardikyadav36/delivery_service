from pydantic import BaseModel
from app.models.delivery_enum import DeliveryStatus

class DeliveryCreate(BaseModel):
    user_id: int
    pickup_location: str
    drop_location: str

class DeliveryResponse(BaseModel):
    id: int
    user_id: int
    pickup_location: str
    drop_location: str
    status: DeliveryStatus

    class Config:
        from_attributes = True