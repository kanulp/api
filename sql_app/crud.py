from sqlalchemy.orm import Session
from sqlalchemy.sql import func
from sqlalchemy import distinct
from . import models, schemas


def get_user_by_id(db: Session, id: int):
    return db.query(models.User).filter(models.User.id == id).first()


def get_user_from_email(db: Session, email: str,courseName:str):
    return db.query(models.User).filter(models.User.email == email).filter(models.User.courseName==courseName).order_by(models.User.timestamp.desc()).first()


def get_user_stats_general(db: Session, email: str,courseName:str):
    return db.query(models.User).filter(models.User.email == email).filter(models.User.courseName==courseName).filter(func.sum(models.User.correctCount).label('total_correct_count')).first()



def get_all_users(db: Session):
    return db.query(models.User).all()


def createUser(db: Session, user: schemas.UserSchema):
    db_user = models.User(email=user.email, points=user.points, courseName=user.courseName,userName=user.userName,incorrectCount=user.incorrectCount,correctCount=user.correctCount,setCount=user.setCount,userAverage=user.userAverage,totalTime=user.totalTime,answerCount=user.answerCount)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user_by_username(db: Session, username: str):
    return db.query(models.UserName).filter(models.UserName.userName == username).first()

def createUserName(db: Session, user: schemas.UserNameSchema):
    db_user = models.UserName(email=user.email,userName=user.userName)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def newCSV(db: Session, user: schemas.csvSchema):
    db_user = models.CSV(email=user.email,courseName=user.courseName)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def getCSVs(db: Session, email: str):
    return db.query(models.CSV).filter(models.CSV.email == email).all()

def get_users_by_csv(db: Session, courseName: str):
    return db.query(models.User.email).distinct().filter(models.User.courseName==courseName).all()
