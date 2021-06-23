from typing import List
from pydantic import BaseModel
from datetime import datetime
class UserSchema(BaseModel):
    id: int
    email : str
    points : int
    timestamp : datetime
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