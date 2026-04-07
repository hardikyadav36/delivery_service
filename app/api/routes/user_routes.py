from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.depends import get_db
from app.schemas.user_schema import UserCreate, UserResponse
from app.services import user_services
router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return user_services.create_user(db, user.name, user.email)

@router.get("/", response_model=list[UserResponse])
def get_users(db: Session = Depends(get_db)):
    return user_services.get_all_users(db)