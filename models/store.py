from sqlalchemy.orm import Mapped, mapped_column, relationship

from db import db

class StoreModel(db.Model):
    __tablename__ = "stores"
    id:Mapped[int] = mapped_column(db.Integer, primary_key=True)
    name: Mapped[str] = mapped_column(db.String(80), unique=True, nullable=False)
    items: Mapped[db.ItemModel] = relationship(back_populates="store", lazy="dynamic", cascade="all, delete")
    tags: Mapped[db.TagModel] = relationship(back_populates="store", lazy="dynamic")
