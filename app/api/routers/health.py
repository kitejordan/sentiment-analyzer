from fastapi import APIRouter
from app.db.engine import engine
from sqlalchemy import text
from openai import OpenAI
from app.core.config import settings

router = APIRouter(prefix="/api/v1")

@router.get("/health")
async def health():
    # DB check
    try:
        async with engine.begin() as conn:
            await conn.execute(text("select 1"))
        db = "ok"
    except Exception as e:
        db = f"error: {e}"

    # OpenAI check (lightweight, no model list to save latency)
    try:
        _ = bool(settings.OPENAI_API_KEY)
        client = OpenAI(api_key=settings.OPENAI_API_KEY)
        # a tiny embed on a fixed string (fast & cheap)
        em = client.embeddings.create(model=settings.OPENAI_EMBED_MODEL, input="hi")
        ai = "ok" if em.data else "empty"
    except Exception as e:
        ai = f"error: {e}"

    return {"status": "ok" if db=="ok" and ai=="ok" else "degraded", "db": db, "openai": ai}
