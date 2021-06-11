from typing import List
from pydantic import BaseModel
from datetime import datetime
class UserInfo(BaseModel):
    id: int
    email : str
    points : int
    timestamp : datetime
    courseName : str

    class Config:
        orm_mode = True