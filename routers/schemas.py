from pydantic import BaseModel
from datetime import date
from typing import List


class UserBase(BaseModel):
  username: str
  email: str
  password: str

class UserDisplay(BaseModel):
  username: str
  email: str
  class Config():
    orm_mode = True

class TodoBase(BaseModel):
  text: str
  assigned_to: str
  due_date: str
  is_completed: bool

class TodoDisplay(BaseModel):
  id: int
  text: str
  assigned_to: str
  due_date: str
  is_completed: bool
  class Config():
    orm_mode = True

class UserAuth(BaseModel):
    id:int
    username:str
    email:str
