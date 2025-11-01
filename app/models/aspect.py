# app/models/aspect.py
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer, ForeignKey, Float, Text
from app.db.base import Base

class Aspect(Base):
    __tablename__ = "aspects"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    review_id: Mapped[int] = mapped_column(ForeignKey("reviews.id", ondelete="CASCADE"), index=True)
    aspect_term: Mapped[str] = mapped_column(String(128), index=True)
    sentiment: Mapped[str] = mapped_column(String(16))
    confidence: Mapped[float | None] = mapped_column(Float)
    method: Mapped[str] = mapped_column(String(16))  # 'baseline'|'rag'

class RetrievedEvidence(Base):
    __tablename__ = "retrieved_evidence"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    aspect_id: Mapped[int] = mapped_column(ForeignKey("aspects.id", ondelete="CASCADE"), index=True)
    evidence_text: Mapped[str] = mapped_column(Text)
    similarity_score: Mapped[float] = mapped_column(Float)
    source_document_id: Mapped[int | None] = mapped_column(Integer)  # documents.id
