from uuid import uuid4
from sqlalchemy.dialects.postgresql import UUID
from models.base import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import (
    Boolean,
    DateTime,
    String,
    func,
)
from datetime import datetime


class User(Base):
    __tablename__ = "users"

    id: Mapped[str] = mapped_column(UUID(
        as_uuid=True),
        primary_key=True,
        default=uuid4)

    email: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        nullable=False,
        index=True)

    username: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        nullable=False,
        index=True)
    password_hash: Mapped[str] = mapped_column(
        String(255),
        nullable=False)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True)
