from typing import List
from pydantic import BaseModel
from datetime import datetime
class UserSchema(BaseModel):
    email : str
    points : int
    courseName : str
    incorrectCount : int
    correctCount : int
    answerCount : int
    setCount : int
    userAverage : int
    totalTime : int
    userName : str
    class Config:
        orm_mode = True

class UserNameSchema(BaseModel):
    email : str
    userName : str
    class Config:
        orm_mode = True