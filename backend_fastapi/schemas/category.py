from uuid import UUID
from datetime import datetime

from pydantic import BaseModel, ConfigDict


class CategoryBase(BaseModel):
    name: str
    icon: str
    color: str


class CategoryCreate(CategoryBase):
    room_id: UUID


class CategoryUpdate(BaseModel):
    name: str | None = None
    icon: str | None = None
    color: str | None = None


class CategoryResponse(CategoryBase):
    id: UUID
    room_id: UUID
    is_default: bool
    is_active: bool
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)