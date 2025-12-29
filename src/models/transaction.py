from datetime import datetime
from enum import Enum

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db import db
from models.account import AccountModel


class TransactionDirection(Enum):
    CREDIT = "credit"
    DEBIT = "debit"


class TransactionModel(db.Model):
    __tablename__ = "transactions"

    id: Mapped[int] = mapped_column(primary_key=True)
    idempotency_key: Mapped[str] = mapped_column(unique=True)
    amount: Mapped[int] = mapped_column()
    direction: Mapped[TransactionDirection] = mapped_column()
    event_description: Mapped[str] = mapped_column()
    account_id: Mapped[int] = mapped_column(ForeignKey("accounts.id"))
    created_at: Mapped[datetime] = mapped_column(default=datetime.now())

    account: Mapped["AccountModel"] = relationship(back_populates="transactions")
