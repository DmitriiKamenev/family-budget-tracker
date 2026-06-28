from uuid import uuid4
from sqlalchemy.dialects.postgresql import UUID

from enums.enums import RoomRole
from models.base import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import (
    Boolean,
    DateTime,
    Enum as SQLEnum,
    ForeignKey,
    UniqueConstraint,
    func,
)
from datetime import datetime

class RoomMember(Base):
    __tablename__ = "room_members"

    __table_args__ = (
        UniqueConstraint("room_id", "user_id"),
    )

    id: Mapped[str] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid4)

    room_id: Mapped[str] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("rooms.id", ondelete="CASCADE"),
    )

    user_id: Mapped[str] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="CASCADE"),
    )

    role: Mapped[RoomRole] = mapped_column(
        SQLEnum(RoomRole),
        default=RoomRole.MEMBER,
    )

    joined_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
    )

    is_active: Mapped[bool] = mapped_column(Boolean, default=True)