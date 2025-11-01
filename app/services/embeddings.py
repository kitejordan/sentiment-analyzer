# app/services/embeddings.py
from openai import OpenAI
from app.core.config import settings

_client = OpenAI(api_key=settings.OPENAI_API_KEY)

async def embed_text(text: str) -> list[float]:
    resp = _client.embeddings.create(model="text-embedding-3-small", input=text)
    return resp.data[0].embedding
