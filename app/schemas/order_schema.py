from pydantic import BaseModel


class OrderCreate(BaseModel):
    user_id: int
    pickup_location: str
    delivery_location: str
    pickup_latitude: float
    pickup_longitude: float
    delivery_latitude: float
    delivery_longitude: float


class OrderResponse(BaseModel):
    id: int
    user_id: int
    worker_id: int | None
    status: str

    pickup_location: str
    delivery_location: str

    class Config:
        from_attributes = True