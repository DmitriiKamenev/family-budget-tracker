from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from starlette import status

from core.security import verify_password, create_access_token
from schemas.user import UserCreate, UserResponse
from database.session import get_db

from models.user import User as UserModel
import crud.user as crud_user

auth_router = APIRouter(prefix="/auth", tags="")

# Регистрация
@auth_router.post("/register",
    status_code=status.HTTP_201_CREATED
    )
def register(user: UserCreate, db: Session = Depends(get_db)):
    db_user = crud_user.create_user(user, db)
    return UserResponse(
        id=db_user.id,
        email=db_user.email,
        username=db_user.username,
        created_at=db_user.created_at,
        updated_at=db_user.updated_at,
        is_active=db_user.is_active
    )
# Аутентификация пользователя
@auth_router.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    db_user = crud_user.get_user_by_email(form_data.username, db)

    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    if not verify_password(form_data.password, db_user.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    token = create_access_token({"sub": db_user.email})

    return {
        "access_token": token,
        "token_type": "bearer"
    }