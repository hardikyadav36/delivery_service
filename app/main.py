from fastapi import FastAPI,Depends
from app.api.routes import user_routes,delivery_routes
from app.database.session import Base, SessionLocal, engine
from app.database.depends import get_db
from sqlalchemy.orm import Session
from sqlalchemy import text 
Base.metadata.create_all(bind=engine)
app = FastAPI()
app.include_router(user_routes.router)
app.include_router(delivery_routes.router)
# logistic_env\scripts\activate

@app.get("/")
def root():
    return {"message": "Backend is running 🚀"}

@app.get("/db-test")
def db_test(db: Session = Depends(get_db)):
    result = db.execute(text("SELECT 1"))
    return {"db_test": result.scalar()}




