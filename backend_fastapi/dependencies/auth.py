from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from core.security import oauth2_scheme
from database.session import get_db
from crud.user import get_user_by_email

