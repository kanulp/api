from typing import List
from pydantic import BaseModel

class UserInfo(BaseModel):
    id: int
    email : str
    points = int
    timestamp = str
    courseName = str

    class Config:
        orm_mode = True