from sqlalchemy import Column, Integer, String, Boolean, Float, Index
from app.database.session import Base

class Worker(Base):
    __tablename__ = "workers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    current_location = Column(String, nullable=False)
    is_available = Column(Boolean, default=True, index=True)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)

    __table_args__ = (
        Index("idx_worker_location", "latitude", "longitude"),
    )