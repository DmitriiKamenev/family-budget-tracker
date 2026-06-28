from uuid import UUID
from datetime import datetime

from pydantic import BaseModel, ConfigDict


class RoomBase(BaseModel):
    name: str


class RoomCreate(RoomBase):
    pass


class RoomUpdate(BaseModel):
    name: str | None = None


class RoomResponse(RoomBase):
    id: UUID
    created_by: UUID
    invite_code: str
    created_at: datetime
    is_active: bool

    model_config = ConfigDict(from_attributes=True)