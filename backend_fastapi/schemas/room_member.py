from uuid import UUID
from datetime import datetime

from pydantic import BaseModel, ConfigDict

from .enums import RoomRole


class RoomMemberCreate(BaseModel):
    room_id: UUID
    user_id: UUID
    role: RoomRole = RoomRole.member


class RoomMemberResponse(BaseModel):
    id: UUID
    room_id: UUID
    user_id: UUID
    role: RoomRole
    joined_at: datetime
    is_active: bool

    model_config = ConfigDict(from_attributes=True)