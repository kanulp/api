from sqlalchemy import Column, Integer, String
from .database import Base
from sqlalchemy.types import DateTime


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    points = Column(Integer)
    timestamp = Column(DateTime)
    courseName = Column(String)
    incorrectCount = Column(Integer)
    correctCount = Column(Integer)
    answerCount = Column(Integer)
    setCount = Column(Integer)
    userAverage = Column(Integer)
    totalTime = Column(Integer)

class UserName(Base):
    __tablename__ = "username"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    userName = Column(String, unique=True)

class CSV(Base):
    __tablename__ = "csv_logs"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    courseName = Column(String, unique=True)
