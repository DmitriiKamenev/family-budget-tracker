from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas.user import UserCreate
from database.session import get_db

auth_routers = APIRouter(prefix="/auth", tags="")

