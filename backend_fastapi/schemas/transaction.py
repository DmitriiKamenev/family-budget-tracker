from uuid import UUID
from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, ConfigDict

from .enums import TransactionType


class TransactionBase(BaseModel):
    category_id: UUID
    amount: Decimal
    type: TransactionType
    description: str | None = None
    transaction_date: datetime


class TransactionCreate(TransactionBase):
    room_id: UUID


class TransactionUpdate(BaseModel):
    category_id: UUID | None = None
    amount: Decimal | None = None
    type: TransactionType | None = None
    description: str | None = None
    transaction_date: datetime | None = None


class TransactionResponse(TransactionBase):
    id: UUID
    room_id: UUID
    user_id: UUID
    created_at: datetime
    updated_at: datetime
    is_deleted: bool

    model_config = ConfigDict(from_attributes=True)