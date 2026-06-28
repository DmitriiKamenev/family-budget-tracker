from sqlalchemy.orm import Session
from models.user import User as UserModel
from schemas.user import UserCreate
from core.security import hash_password
from datetime import datetime


def get_all_users(db: Session):
    return db.query(UserModel).all()


def get_user_by_email(email: str, db: Session):
    return (
        db.query(UserModel)
        .filter(UserModel.email == email)
        .first()
    )


def create_user(user: UserCreate, db: Session):

    db_user = UserModel(
        email=user.email,
        username=user.username,
        password_hash=hash_password(user.password)
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user