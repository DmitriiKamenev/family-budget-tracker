import secrets
import string

from sqlalchemy.orm import Session
from models.room import Room as RoomModel

ALPHABET = string.ascii_uppercase + string.digits

def generate_invite_code(db: Session) -> str:
    while True:
        code = "".join(secrets.choice(ALPHABET) for _ in range(8))

        exists = db.query(RoomModel).filter(RoomModel.invite_code == code).first()

        if not exists:
            return code