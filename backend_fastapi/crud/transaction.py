from uuid import UUID

from sqlalchemy.orm import Session
from models.transaction import Transaction as TransactionModel
from models.roommember import RoomMember
from schemas.room import RoomCreate

def create_transaction( transaction: TransactionModel,
                        room_id: UUID,
                        user_id: UUID,
                        db: Session):
    db_transaction = TransactionModel(
        room_id=room_id,
        category_id=transaction.category_id,
        amount=transaction.amount,
        type=transaction.type,
        description=transaction.description,
        transaction_date=transaction.transaction_date,
        user_id=user_id
    )
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    return db_transaction
def get_all_transaction(room_id: UUID, db: Session):
    room_transaction = db.query(TransactionModel).filter(TransactionModel.room_id == room_id)
    return room_transaction

def get_by_id_transaction(tran_id: UUID, db: Session):
    return db.query(TransactionModel).filter(TransactionModel.id == tran_id).first()

def delete_transaction(transaction_id: UUID,
                    db: Session):
    db.query(TransactionModel).filter(TransactionModel.id==transaction_id).delete()
    db.commit()

