from typing import Optional
from fastapi import FastAPI
import uvicorn
from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import sys
sys.path.append(r"/Users/kanu/Desktop/api")
from typing import List

from sql_app import models
from sql_app import schemas
from sql_app import crud

from sql_app.database import SessionLocal, engine


models.Base.metadata.create_all(bind=engine)


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"Hello": "World"}

#get single user
@app.get("/users/{user_id}", response_model=schemas.UserSchema)
def read_user(id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_id(db, id=id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
    
#get user from email
@app.post("/users_by_email", response_model=schemas.UserSchema)
def read_user(email: str, db: Session = Depends(get_db)):
    db_user = crud.get_user_from_email(db, email=email)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
    
#get all users
@app.get("/users", response_model=List[schemas.UserSchema])
def get_all_users(db: Session = Depends(get_db)):
    db_user = crud.get_all_users(db)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

#insert user
@app.post("/users/", response_model=schemas.UserSchema)
def create_user(user: schemas.UserSchema, db: Session = Depends(get_db)):
    #db_user = crud.createUser(db, email=user.email,points=user.points,timestamp=user.timestamp,courseName=user.courseName)
    #if db_user:
    #    raise HTTPException(status_code=400, detail="Email already registered")
    return crud.createUser(db=db, user=user)
