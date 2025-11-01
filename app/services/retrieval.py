# app/services/retrieval.py
from sqlalchemy import text
from app.db.engine import SessionLocal
from app.models.document import EMBED_DIM

async def knn_by_text_embedding(query_vec: list[float], k: int = 3):
    sql = text("""
        select id, text, aspect_hint, sentiment_label,
               1 - (embedding <-> :q) as similarity
        from documents
        order by embedding <-> :q
        limit :k
    """)
    async with SessionLocal() as s:
        rows = (await s.execute(sql, {"q": query_vec, "k": k})).mappings().all()
        return [dict(r) for r in rows]
