from fastapi import HTTPException, status
from uuid import UUID

from sqlalchemy.orm import Session
from starlette import status

from enums.enums import RoomRole
from schemas.room import RoomCreate
from services.utils import generate_invite_code
import crud.room as crud_room
import crud.room_member as crud_room_member


def create_room(room: RoomCreate, user_id:   UUID, db: Session):
    invite_code = generate_invite_code(db)

    db_room = crud_room.create_room(
        db=db,
        room=room,
        user_id=user_id,
        invite_code=invite_code,
    )

    crud_room_member.add_member(
        db=db,
        room_id=db_room.id,
        user_id=user_id,
        role=RoomRole.ADMIN,
    )

    db.commit()
    db.refresh(db_room)

    return db_room


def get_user_rooms(user_id: UUID, db: Session):
    return crud_room.get_user_rooms(user_id, db)


def invite_member_in_room(invite_code: str, user_id: UUID, db: Session):
    room = crud_room.get_room_by_invite_code(invite_code, db)
    if room is None:
        raise HTTPException(404, "Room not found")

    member = crud_room_member.get_member(room.id, user_id, db)
    if member is not None:
        raise HTTPException(404, "Member duplicate")

    crud_room_member.add_member(db, room.id, user_id, RoomRole.MEMBER)
    db.commit()
    return room

def get_all_members_in_room(room_id :UUID, user_id: UUID, db: Session):
    rooms = get_user_rooms(user_id, db)
    if room_id not in [room.id for room in rooms]:
        raise HTTPException(404, "Room not found")

    members = crud_room_member.get_all_member_room(room_id, db)
    if members is None:
        raise HTTPException(404, "Room not found")

    return [
        {
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "role": role,
        }
        for user, role in members
    ]

def delete_room(room_id :UUID, user_id:  UUID, db: Session):
    admins = crud_room_member.get_admin_member_room(room_id, db)
    if user_id not in [admin.id for admin in admins]:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only room admin can delete the room"
        )
    crud_room.delete_room(room_id, db)

