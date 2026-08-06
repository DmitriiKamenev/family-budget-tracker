from enum import Enum
class RoomRole(str, Enum):
    ADMIN = "admin"
    MEMBER = "member"


class TransactionType(str, Enum):
    INCOME = "income"
    EXPENSE = "expense"