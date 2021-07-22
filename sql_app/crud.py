from sqlalchemy.orm import Session
from sqlalchemy.sql import func
from sqlalchemy import distinct
from sqlalchemy.sql import text
from . import models, schemas


def get_user_by_id(db: Session, id: int):
    return db.query(models.User).filter(models.User.id == id).first()


def get_user_from_email(db: Session, email: str,courseName:str):
    return db.query(models.User).filter(models.User.email == email).filter(models.User.courseName==courseName).order_by(models.User.timestamp.desc()).first()


def get_user_stats_general(db: Session, email: str,courseName:str):
    query = text("SELECT email, courseName, SUM(incorrectCount) total_incorrect, SUM(correctCount) total_correct_count, SUM(points) total_points, SUM(answerCount) total_answerCount, SUM(totalTime) total_upTime, SUM(setCount) total_Sets, ROUND(AVG(userAverage)) total_average  FROM users where courseName=:courseName and email=:email")
    data = { 'courseName' : courseName ,'email':email}
    return db.execute(query,data).fetchall()
    #return db.query(models.User).filter(models.User.email == email).filter(models.User.courseName==courseName).filter(func.sum(models.User.correctCount).label('total_correct_count')).first()



def get_all_users(db: Session):
    return db.query(models.User).all()


def createUser(db: Session, user: schemas.UserSchema):
    db_user = models.User(email=user.email, points=user.points, courseName=user.courseName,incorrectCount=user.incorrectCount,correctCount=user.correctCount,setCount=user.setCount,userAverage=user.userAverage,totalTime=user.totalTime,answerCount=user.answerCount, eligible=user.eligible)
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
    db_user = models.CSV(email=user.email,courseName=user.courseName, timestamp = user.timestamp, weekstoDraw=user.weekstoDraw, minAns=user.minAns, minCorrect=user.minCorrect, minAverage=user.minAverage, minSets=user.minSets, drawPrize=user.drawPrize)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def getCSVs(db: Session, email: str):
    return db.query(models.CSV).filter(models.CSV.email == email).all()

def get_users_by_csv(db: Session, courseName: str):
    
    query = text("Select DISTINCT email from users where courseName = :course")
    data = { 'course' : courseName }
    return db.execute(query,data).fetchall()
    #return db.query(models.User.email).distinct().filter(models.User.courseName==courseName).all()

# def update_drawData(db: Session, courseName: str):
#     db.query(models.CSV).filter(courseName == user.courseName).update({'weekstoDraw': 'Complete'})
#     db.commit()
#
# def delete_Records(db: Session, courseName: str):
#     query = text("DELETE * from users where courseName = :course")
#     data = {'course': courseName}
#     db.execute(query,data)
#
# def delete_CSV(db: Session, courseName: str):
#     query = text("DELETE * from csv_logs where courseName = :course")
#     data = {'course': courseName}
#     db.execute(query,data)
