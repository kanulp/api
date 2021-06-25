from sqlalchemy.orm import Session

from . import models, schemas


def get_user_by_id(db: Session, id: int):
    return db.query(models.User).filter(models.User.id == id).first()


def get_user_from_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def get_all_users(db: Session):
    return db.query(models.User).all()


def createUser(db: Session, user: schemas.UserSchema):
    db_user = models.User(email=user.email, points=user.points, courseName=user.courseName,userName=user.userName,incorrectCount=user.incorrectCount,correctCount=user.correctCount,setCount=user.setCount,userAverage=user.userAverage,totalTime=user.totalTime,answerCount=user.answerCount)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user