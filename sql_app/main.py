from typing import Optional
from fastapi import FastAPI
import uvicorn
from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import sys

sys.path.append(r"/Users/user/PycharmProjects/api")
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


# get single user
@app.get("/users/{user_id}", response_model=schemas.UserSchema)
def read_user(id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_id(db, id=id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


# get user from email
@app.get("/users_by_email", response_model=schemas.UserSchema)
def read_user_by_email(email: str, courseName: str, teacher: str, db: Session = Depends(get_db)):
    db_user = crud.get_user_from_email(db, email=email, courseName=courseName, teacher=teacher)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


# get all users
@app.get("/users", response_model=List[schemas.UserSchema])
def get_all_users(db: Session = Depends(get_db)):
    db_user = crud.get_all_users(db)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


# insert user
@app.post("/users/", response_model=schemas.UserSchema)
def create_user(user: schemas.UserSchema, db: Session = Depends(get_db)):
    # db_user = crud.createUser(db, email=user.email,points=user.points,timestamp=user.timestamp,courseName=user.courseName)
    # if db_user:
    #    raise HTTPException(status_code=400, detail="Email already registered")
    return crud.createUser(db=db, user=user)


# insert userName
@app.post("/username", response_model=schemas.UserNameSchema)
def create_userName(user: schemas.UserNameSchema, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_username(db, username=user.userName)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    return crud.createUserName(db=db, user=user)


@app.post("/new_csv", response_model=schemas.csvSchema)
def create_CSV(csvSchema: schemas.csvSchema, db: Session = Depends(get_db)):
    return crud.newCSV(db=db, user=csvSchema)


@app.get("/get_csvs", response_model=List[schemas.csvSchema])
def get_csvs(email: str, db: Session = Depends(get_db)):
    db_user = crud.getCSVs(db, email=email)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Not found")
    return db_user


# check username
@app.post("/check_username")
def check_username(username: str, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_username(db, username=username)
    if db_user:
        return {"message": "username not available."}
    else:
        return {"message": "username available."}
    return db_user


@app.get("/get_user_stats_general")
def get_user_stats_general(email: str, courseName: str, teacher: str, db: Session = Depends(get_db)):
    db_user = crud.get_user_stats_general(db, email=email, courseName=courseName, teacher=teacher)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


# @app.get("/users_by_csv", response_model=List[schemas.UserSchema])
@app.get("/users_by_csv")
def read_users_by_csv(courseName: str, teacher: str, db: Session = Depends(get_db)):
    db_user = crud.get_users_by_csv(db, courseName=courseName, teacher=teacher)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.get("/activate_draw")
def activate_draw(courseName: str, teacher: str, db: Session = Depends(get_db)):
    db_user = crud.activateDraw(db, courseName=courseName, teacher=teacher)
    if db_user is None:
        raise HTTPException(status_code=404, detail="No users have qualified")
    return db_user


@app.post("/update_draw_data")
def update_draw_data(courseName: str, email: str, db: Session = Depends(get_db)):
    res = crud.update_drawData(db, courseName=courseName, email=email)
    return res


@app.post("/delete_records")
def delete_records(courseName: str, teacher: str, db: Session = Depends(get_db)):
    res = crud.delete_Records(db, courseName=courseName, teacher=teacher)
    return res

@app.post("/delete_csv")
def delete_CSV(courseName: str, email: str, db: Session = Depends(get_db)):
    res = crud.delete_CSV(db, courseName=courseName, email=email)
    return res
