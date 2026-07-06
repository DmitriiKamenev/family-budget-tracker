from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from core.security import get_current_user
from database.session import get_db
from schemas.room import RoomCreate
from models.user import User as UserModel
from uuid import UUID
import crud.room as crud_room
from services.utils import generate_invite_code
import services.room as room_servise


room_router = APIRouter(prefix='/rooms')
@room_router.post('/', status_code=status.HTTP_201_CREATED)
def createRooms(room: RoomCreate,
                user: UserModel = Depends(get_current_user),
                db: Session = Depends(get_db)
                ):
    return room_servise.create_room(room=room,
                                    user_id=user.id,
                                    db=db)

@room_router.get('/')
def get_rooms_user(user: UserModel = Depends(get_current_user),
                   db: Session = Depends(get_db)):
    return room_servise.get_user_rooms(user_id=user.id, db=db)

@room_router.post('/join/{invite_code}')
def join_room_by_invite_code(invite_code: str,
                             user: UserModel = Depends(get_current_user),
                             db : Session = Depends(get_db)):
    return room_servise.invite_member_in_room(invite_code=invite_code,
                                              user_id=user.id, db=db)

@room_router.get("/{room_id}/members")
def get_all_member_in_room(room_id: UUID,
                           db: Session = Depends(get_db),
                           user: UserModel = Depends(get_current_user)):
    return room_servise.get_all_members_in_room(room_id, db)