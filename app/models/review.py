# app/models/review.py
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Text, String, Integer, ForeignKey, Float, JSON
from app.db.base import Base

class Review(Base):
    __tablename__ = "reviews"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    text: Mapped[str] = mapped_column(Text, nullable=False)
    product_category: Mapped[str | None] = mapped_column(String(64))
    rating: Mapped[int | None] = mapped_column(Integer)
