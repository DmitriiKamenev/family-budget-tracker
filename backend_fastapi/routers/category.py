from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from core.security import get_current_user
from database.session import get_db

from schemas.category import CategoryCreate, CategoryResponse
from models.user import User as UserModel
from uuid import UUID

import services.category as category_services

category_router = APIRouter(prefix='/category')

@category_router.post(path='/')
def add_category(category: CategoryCreate,
                 user: UserModel = Depends(get_current_user),
                 db: Session = Depends(get_db)):
    return category_services.create_category(category, user.id, db)

@category_router.get(path='/{room_id}/', response_model=List[CategoryResponse])
def get_category(room_id: UUID,
                 user: UserModel = Depends(get_current_user),
                 db: Session = Depends(get_db)):
    return category_services.get_room_category(user.id, room_id, db)

@category_router.delete(path='/{room_id}/{category_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_category(room_id:UUID,
                    category_id: UUID,
                    user: UserModel = Depends(get_current_user),
                    db: Session = Depends(get_db)
                    ):
    category_services.delete_category_in_room(user_id=user.id,
                                              room_id=room_id,
                                              category_id=category_id,
                                              db=db)