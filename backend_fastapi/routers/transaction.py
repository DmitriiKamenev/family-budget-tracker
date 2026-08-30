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

transaction_router = APIRouter(prefix="/rooms/{room_id}/transactions",
                               tags=["Transactions"])


@transaction_router.post(path='/',
                         response_model=TransactionResponse,
                         status_code=status.HTTP_201_CREATED)
def add_transaction(transaction: TransactionCreate,
                    room_id: UUID,
                    user: UserModel = Depends(get_current_user),
                    db: Session = Depends(get_db)):
    return transaction_services.create_transaction(transaction, room_id, user.id, db)


@transaction_router.get(path='/',
                        response_model=List[TransactionResponse])
def get_transactions(room_id: UUID,
                     user: UserModel = Depends(get_current_user),
                     db: Session = Depends(get_db)):
    return transaction_services.get_room_transaction(user.id, room_id, db)


@transaction_router.get(path='/{transaction_id}',
                        response_model=TransactionResponse)
def get_by_id_transaction(room_id: UUID,
                          transaction_id: UUID,
                          user: UserModel = Depends(get_current_user),
                          db: Session = Depends(get_db)):
    return transaction_services.get_by_id_transaction(transaction_id, user.id, room_id, db)

@transaction_router.delete(path='/{transaction_id}')
def delete_transaction(room_id: UUID,
                          transaction_id: UUID,
                          user: UserModel = Depends(get_current_user),
                          db: Session = Depends(get_db)):
    return transaction_services.delete_transaction(transaction_id, user.id, room_id, db)