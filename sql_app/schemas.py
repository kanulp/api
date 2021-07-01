from typing import List,Optional
from pydantic import BaseModel
from datetime import datetime
class UserSchema(BaseModel):
    email : str
    points : int
    timestamp : Optional[datetime]
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