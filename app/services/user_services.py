from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.repositories import user_repo
"""This layer contains business logic and talks to repo layer"""
def create_user(db: Session, name: str, email: str):
    existing_user = user_repo.get_user_by_email(db, email)

    if existing_user:
        raise HTTPException(status_code=400, detail="Email already exists")

    return user_repo.create_user(db, name, email)



def get_all_users(db: Session):
    return user_repo.get_all_users(db)