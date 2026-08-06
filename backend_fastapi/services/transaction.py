from fastapi import HTTPException, status
from uuid import UUID

from sqlalchemy.orm import Session
from starlette import status

from enums.enums import RoomRole
from schemas.transaction import TransactionCreate
from services.utils import generate_invite_code
import crud.transaction as crud_transaction
import crud.room_member as crud_room_member

def create_transaction(transaction: TransactionCreate,
                    user_id: UUID,
                    db: Session):
    members = crud_room_member.get_all_member_room(transaction.room_id, db)
    member_ids = {user.id for user, _ in members}

    if user_id not in member_ids:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only room members can add transaction"
        )

    return crud_transaction.create_transaction(transaction, user_id, db)

def get_room_transaction(user_id: UUID,
                      room_id: UUID,
                      db: Session):
    members = crud_room_member.get_all_member_room(room_id, db)
    member_ids = {user.id for user, _ in members}

    if user_id not in member_ids:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only room members can read categories"
        )
    return crud_transaction.get_all_transaction(room_id, db)