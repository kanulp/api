from sqlalchemy import Column, Integer, String
from .database import Base
from sqlalchemy.types import DateTime


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String(255), unique=True)
    teacher = Column(String(255))
    timestamp = Column(DateTime)
    courseName = Column(String(255))
    incorrectCount = Column(Integer)
    correctCount = Column(Integer)
    answerCount = Column(Integer)
    setCount = Column(Integer)
    userAverage = Column(Integer)
    totalTime = Column(Integer)
    eligible = Column(String(255))

class UserName(Base):
    __tablename__ = "username"

    id = Column(Integer, primary_key=True)
    email = Column(String(255), unique=True)
    userName = Column(String(255), unique=True)

class CSV(Base):
    __tablename__ = "csv_logs"

    id = Column(Integer, primary_key=True)
    email = Column(String(255), unique=True)
    timestamp = Column(DateTime)
    courseName = Column(String(255), unique=True)
    weekstoDraw = Column(String(255))
    minAns = Column(String(255))
    minCorrect = Column(String(255))
    minAverage = Column(String(255))
    minSets = Column(String(255))
    drawPrize = Column(String(255))
