from sqlalchemy.orm import Mapped, mapped_column, relationship

from db import db

class StoreModel:
    __tablename__ = "stores"
    id:Mapped[int] = mapped_column(db.Integer, primary_key=True)
    name: Mapped[str] = mapped_column(db.String(80), nullable=False)
    items: Mapped["db.ItemModel"] = relationship(back_populates="stores", lazy="dynamic")