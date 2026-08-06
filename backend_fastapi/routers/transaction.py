from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from core.security import get_current_user
from database.session import get_db

from schemas.transaction import TransactionCreate, TransactionResponse
from models.user import User as UserModel
from uuid import UUID

import services.transaction as transaction_services

transaction_router = APIRouter(prefix='/transaction')

@transaction_router.post(path='/')
def add_transaction(transaction: TransactionCreate,
                 user: UserModel = Depends(get_current_user),
                 db: Session = Depends(get_db)):
    return transaction_services.create_transaction(transaction, user.id, db)

@transaction_router.get(path='/{room_id}/', response_model=List[TransactionResponse])
def get_category(room_id: UUID,
                 user: UserModel = Depends(get_current_user),
                 db: Session = Depends(get_db)):
    return transaction_services.get_room_transaction(user.id, room_id, db)