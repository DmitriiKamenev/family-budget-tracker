from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette import status

from core.security import get_current_user
from database.session import get_db

from schemas.user import UserResponse
from models.user import User as UserModel
import crud.user as  crud_user

import services.user as user_services

user_router = APIRouter(prefix='/user')

@user_router.get('/', response_model=UserResponse, description="Получить данные пользователя")
def get_user_by_id(user: UserModel = Depends(get_current_user),
                   db: Session = Depends(get_db)):
    return user_services.get_user_by_id(user.id, db)