from uuid import UUID

from fastapi import HTTPException
from sqlalchemy.orm import Session
import crud.user as  crud_user
def get_user_by_id(user_id: UUID,
                   db: Session):
    user = crud_user.get_user_by_id(user_id, db)
    if user is None:
        raise HTTPException(404, "User not found")
    return user