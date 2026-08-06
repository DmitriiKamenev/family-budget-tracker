from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import create_engine
from models.base import Base

engine = create_engine('sqlite:///db.sqlite', echo=True)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)
def del_db():
    Base.metadata.drop_all(engine)

def init_db():
    Base.metadata.create_all(engine)

def get_db():
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()
