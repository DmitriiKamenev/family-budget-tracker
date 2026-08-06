from fastapi import HTTPException, status
from uuid import UUID

from sqlalchemy.orm import Session
from starlette import status

from enums.enums import RoomRole
from schemas.category import CategoryCreate
from services.utils import generate_invite_code
import crud.category as crud_category
import crud.room_member as crud_room_member

def create_category(category: CategoryCreate,
                    user_id: UUID,
                    db: Session):
    members = crud_room_member.get_all_member_room(category.room_id, db)
    member_ids = {user.id for user, _ in members}

    if user_id not in member_ids:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only room members can add categories"
        )

    return crud_category.create_category(category, db)

def get_room_category(user_id: UUID,
                      room_id: UUID,
                      db: Session):
    members = crud_room_member.get_all_member_room(room_id, db)
    member_ids = {user.id for user, _ in members}

    if user_id not in member_ids:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only room members can read categories"
        )
    return crud_category.get_category(room_id, db)

def delete_category_in_room(user_id:UUID,
                            category_id: UUID,
                            room_id: UUID,
                            db: Session):

    members = crud_room_member.get_all_member_room(room_id, db)
    member_ids = {user.id for user, _ in members}

    if user_id not in member_ids:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only room members can delete categories"
        )
    return crud_category.delete_category(category_id,
                                         room_id,
                                         db)