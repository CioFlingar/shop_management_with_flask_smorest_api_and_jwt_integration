from sqlalchemy.orm import Mapped, mapped_column, relationship

from db import db

class ItemModel(db.Model):
    __tablename__ = "items"
    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    name: Mapped[str] = mapped_column(db.String(80), nullable=False)
    price: Mapped[float] = mapped_column(db.Float(precision=2), nullable=False)
    store_id: Mapped[int] = mapped_column(db.Integer, db.ForeignKey("stores.id"), nullable=False)

    store: Mapped["StoreModel"] = relationship(back_populates="items")
    tags:Mapped[list["TagModel"]] = relationship(back_populates="items", secondary="items_tags")


