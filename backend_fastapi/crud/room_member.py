from typing import List
from uuid import UUID

from sqlalchemy.orm import Session

from enums.enums import RoomRole
from models.roommember import RoomMember
from models.room import Room as RoomModel
from models.user import User as UserModel


def add_member(db: Session, room_id: UUID, user_id: UUID, role: RoomRole):
    member = RoomMember(
        room_id=room_id,
        user_id=user_id,
        role=role,
    )

    db.add(member)
    return member


def get_member(room_id: UUID, user_id: UUID, db: Session):
    return (db.query(RoomMember)
            .filter(RoomMember.room_id == room_id,
                    RoomMember.user_id == user_id,
                    )
            .first()
            )

def get_all_member_room(room_id: UUID, db: Session):
    return (
        db.query(UserModel, RoomMember.role)
        .join(RoomMember, UserModel.id == RoomMember.user_id)
        .filter(RoomMember.room_id == room_id)
        .all()
    )

def get_admin_member_room(room_id: UUID, db: Session) -> list[UserModel]:
    return (
        db.query(UserModel)
        .join(RoomMember, UserModel.id == RoomMember.user_id)
        .filter(RoomMember.room_id == room_id,
                RoomMember.role == RoomRole.ADMIN)
        .all()
    )
