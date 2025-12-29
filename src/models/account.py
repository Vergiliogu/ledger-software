from sqlalchemy.orm import Mapped, mapped_column, relationship

from db import db
from models.transaction import TransactionModel


class AccountModel(db.Model):
    __tablename__ = "accounts"

    id: Mapped[int] = mapped_column(primary_key=True)

    transactions: Mapped[list["TransactionModel"]] = relationship(back_populates="account")
