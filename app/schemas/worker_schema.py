from pydantic import BaseModel

class WorkerBase(BaseModel):
    name: str
    current_location: str
    latitude: float
    longitude: float

class WorkerCreate(WorkerBase):
    pass

class WorkerResponse(WorkerBase):
    id: int
    is_available: bool

    class Config:
        from_attributes = True