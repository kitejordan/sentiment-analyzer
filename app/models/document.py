# app/models/document.py
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer, JSON, Text
from pgvector.sqlalchemy import Vector
from app.db.base import Base

EMBED_DIM = 1536

class Document(Base):
    __tablename__ = "documents"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    text: Mapped[str] = mapped_column(Text, nullable=False)
    aspect_hint: Mapped[str | None] = mapped_column(String(128))
    sentiment_label: Mapped[str | None] = mapped_column(String(16))
    category: Mapped[str | None] = mapped_column(String(64))
    flags: Mapped[dict | None] = mapped_column(JSON)
    embedding: Mapped[list[float]] = mapped_column(Vector(EMBED_DIM), nullable=False)
