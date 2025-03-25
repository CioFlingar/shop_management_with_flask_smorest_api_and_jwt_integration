from db import db
from sqlalchemy.orm import Mapped, mapped_column


class ItemTags(db.Model):
    __tablename__ = "items_tags"

    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)

    store_id: Mapped[int] = mapped_column(db.Integer, db.ForeignKey("stores.id"))
    tag_id: Mapped[int] = mapped_column(db.Integer, db.ForeignKey("tags.id"))