from sqlalchemy import Column, Integer, String
from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    userName = Column(String, unique=True)
    points = Column(Integer)
    #timestamp = Column(String)
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