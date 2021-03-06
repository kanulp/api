from sqlalchemy.orm import Session
from sqlalchemy.sql import func
from sqlalchemy import distinct
from sqlalchemy.sql import text
from . import models, schemas


def get_user_by_id(db: Session, id: int):
    return db.query(models.User).filter(models.User.id == id).first()


def get_user_from_email(db: Session, email: str, courseName: str, teacher: str):
    return db.query(models.User).filter(models.User.email == email).filter(
        models.User.courseName == courseName).filter(models.User.teacher == teacher).order_by(models.User.timestamp.desc()).first()


def get_user_stats_general(db: Session, email: str, courseName: str, teacher: str):
    query = text(
        "SELECT email, teacher, courseName, SUM(incorrectCount) total_incorrect, SUM(correctCount) total_correct_count, SUM(answerCount) total_answerCount, SUM(totalTime) total_upTime, SUM(setCount) total_Sets, ROUND(AVG(userAverage)) total_average, eligible  FROM users WHERE courseName=:courseName and email=:email AND teacher=:teacher GROUP BY email, teacher, courseName, eligible")
    data = {'courseName': courseName, 'email': email, 'teacher': teacher}
    return db.execute(query, data).fetchall()
    # return db.query(models.User).filter(models.User.email == email).filter(models.User.courseName==courseName).filter(func.sum(models.User.correctCount).label('total_correct_count')).first()


def get_all_users(db: Session):
    return db.query(models.User).all()


def createUser(db: Session, user: schemas.UserSchema):
    db_user = models.User(email=user.email, teacher=user.teacher, timestamp=user.timestamp, courseName=user.courseName,incorrectCount=user.incorrectCount, correctCount=user.correctCount, setCount=user.setCount,userAverage=user.userAverage, totalTime=user.totalTime, answerCount=user.answerCount,eligible=user.eligible)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user_by_username(db: Session, username: str):
    return db.query(models.UserName).filter(models.UserName.userName == username).first()


def createUserName(db: Session, user: schemas.UserNameSchema):
    db_user = models.UserName(email=user.email, userName=user.userName)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def newCSV(db: Session, user: schemas.csvSchema):
    db_user = models.CSV(email=user.email, courseName=user.courseName, timestamp=user.timestamp,
                         weekstoDraw=user.weekstoDraw, minAns=user.minAns, minCorrect=user.minCorrect,
                         minAverage=user.minAverage, minSets=user.minSets, drawPrize=user.drawPrize)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def getCSVs(db: Session, email: str):
    return db.query(models.CSV).filter(models.CSV.email == email).all()


def get_users_by_csv(db: Session, courseName: str, teacher: str):
    query = text("Select DISTINCT email, eligible from users WHERE courseName=:courseName AND teacher=:teacher")
    data = {'courseName': courseName, 'teacher': teacher}
    return db.execute(query, data).fetchall()
    # return db.query(models.User.email).distinct().filter(models.User.courseName==courseName).all()


def activateDraw(db: Session, courseName: str, teacher: str):
    query = text(
        "SELECT email, courseName, eligible FROM users WHERE courseName=:courseName AND teacher=:teacher AND eligible='true' ORDER BY RAND() LIMIT 1")
    data = {'courseName': courseName, 'teacher': teacher}
    return db.execute(query, data).fetchall()


def update_drawData(db: Session, courseName: str, email: str):
    query = text("UPDATE csv_logs SET weekstoDraw='complete' WHERE courseName=:courseName and email=:email")
    data = {'courseName': courseName, 'email': email}
    d = db.execute(query, data)
    db.commit()
    return {"message": "updated successfully."}


def delete_Records(db: Session, courseName: str, teacher: str):
    query = text("DELETE FROM users WHERE courseName=:courseName and teacher=:teacher")
    data = {'courseName': courseName, 'teacher':teacher}
    db.execute(query, data)
    db.commit()
    return {"message": "deleted successfully from users."}


def delete_CSV(db: Session, courseName: str, email: str):
    query = text("DELETE FROM csv_logs WHERE courseName=:courseName and email=:email")
    data = {'courseName': courseName, 'email':email}
    db.execute(query, data)
    db.commit()
    return {"message": "deleted successfully from csv."}
