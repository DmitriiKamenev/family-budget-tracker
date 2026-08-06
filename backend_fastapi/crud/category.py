from uuid import UUID

from sqlalchemy.orm import Session
from models.room import Room as RoomModel
from models.category import Category as CategoryModel

def create_category(category: CategoryModel,
                    db: Session):
    db_category = CategoryModel(
        name=category.name,
        icon=category.icon,
        color=category.color,
        room_id=category.room_id

    )
    db.add(db_category)
    db.commit()
    db.refresh(db_category)

    return db_category

def get_category(room_id: UUID, db: Session):
    room_category = db.query(CategoryModel).filter(CategoryModel.room_id == room_id)
    return room_category

def delete_category(category_id: UUID,
                    room_id: UUID,
                    db: Session):
    db.query(CategoryModel).filter(CategoryModel.id==category_id,
                                   CategoryModel.room_id==room_id).delete()
    db.commit()