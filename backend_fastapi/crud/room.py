from uuid import UUID

from sqlalchemy.orm import Session
from models.room import Room as RoomModel
from models.roommember import RoomMember
from schemas.room import RoomCreate


def create_room(room: RoomCreate,
                user_id: UUID,
                invite_code: str,
                db: Session):
    db_room = RoomModel(
        name=room.name,
        created_by=user_id,
        invite_code=invite_code,
    )

    db.add(db_room)
    db.commit()
    db.refresh(db_room)

    return db_room


def get_user_rooms(user_id: UUID, db: Session):
    return (
        db.query(RoomModel)
        .join(RoomMember, RoomModel.id == RoomMember.room_id)
        .filter(
            RoomMember.user_id == user_id
        )
        .all()
    )



def get_room_by_invite_code(invite_code: str, db: Session):
    room = (db.query(RoomModel)
            .filter(RoomModel.invite_code == invite_code and
                    RoomModel.is_active == 1)
            .first())
    return room


