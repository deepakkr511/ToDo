#from auth.oauth2 import get_current_user
from fastapi import APIRouter, Depends, status
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session
from routers.schemas import TodoBase, TodoDisplay, UserBase
from db.database import get_db
from db import db_user
from typing import List


router = APIRouter(
  prefix='/user',
  tags=['user']
)

@router.post('')
def create_user(request: UserBase, db: Session = Depends(get_db)):
  if not request.username:
    raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, 
              detail="Username can't be empty")
  if not request.email:
    raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, 
              detail="Email is neccessary for contact info")
  return db_user.create(db, request)