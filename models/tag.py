from sqlalchemy.orm import Mapped, mapped_column, relationship

from db import db

class TagModel(db.Model):
    __tablename__ = "tags"

    id:Mapped[int] = mapped_column(db.Integer, primary_key=True)
    name:Mapped[str] = mapped_column(db.String(80), unique=True, nullable=False)
    store_id:Mapped[str] = mapped_column(db.String(), db.ForeignKey("stores.id"), nullable=False)

    store:Mapped["StoreModel"] = relationship(back_populates="tags")
    items:Mapped[list["ItemModel"]] = relationship(back_populates="tags", secondary="items_tags")