from sqlalchemy import Column, Integer, String
from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    userName = Column(String, unique=True)
    points = Column(Integer)
    timestamp = Column(String)
    courseName = Column(String)
    incorrectCount = Column(Integer)
    correctCount = Column(Integer)
    answerCount = Column(Integer)
    setCount = Column(Integer)
    userAverage = Column(Integer)
    totalTime = Column(Integer)

# {
#   "id": 8,
#   "email": "string",
#   "points": 0,
#   "timestamp": "2021-06-23T01:04:35.213Z",
#   "courseName": "string",
#   "incorrectCount" : 2,
#    "correctCount" : 2,
#     "answerCount" : 2,
#     "setCount" : 2,
#     "userAverage" : 2,
#     "totalTime" : 2,
# "userName" : "username123"
# }