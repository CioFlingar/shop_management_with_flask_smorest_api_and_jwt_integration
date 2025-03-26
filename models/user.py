from sqlalchemy.orm import Mapped, mapped_column

from db import db

class UserModel(db.Model):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    username: Mapped[str] = mapped_column(db.String(80), nullable=False)
    password: Mapped[str] = mapped_column(db.String(), nullable=False)