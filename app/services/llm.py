import anyio
from openai import OpenAI
from app.core.config import settings

_client = OpenAI(api_key=settings.OPENAI_API_KEY)

def _chat_sync(msg: str) -> dict:
    resp = _client.chat.completions.create(
        model=settings.OPENAI_CHAT_MODEL,
        messages=[{"role": "system", "content": "Return strict JSON."},
                  {"role": "user", "content": msg}],
        temperature=0
    )
    return resp.choices[0].message.content

async def chat_json(msg: str) -> dict:
    # run sync OpenAI in a worker thread to avoid blocking event loop
    content = await anyio.to_thread.run_sync(_chat_sync, msg)
    import json
    return json.loads(content)
