import json, asyncio
from sqlalchemy import text
from app.db.engine import SessionLocal
from app.services.embeddings import embed_text

SEED_PATH = "data/seed_examples.json"

async def main():
    with open(SEED_PATH, "r", encoding="utf-8") as f:
        items = json.load(f)  # list of {text, aspect_hint?, sentiment_label?}
    async with SessionLocal() as s:
        for it in items:
            vec = await embed_text((it.get("aspect_hint") or "") + " " + it["text"])
            await s.execute(text("""
                insert into documents (text, aspect_hint, sentiment_label, category, flags, embedding)
                values (:t, :a, :sl, :c, :fl, :e)
            """), {
                "t": it["text"],
                "a": it.get("aspect_hint"),
                "sl": it.get("sentiment_label"),
                "c": it.get("category"),
                "fl": json.dumps(it.get("flags", {})),
                "e": vec
            })
        await s.commit()
    print(f"Inserted {len(items)} documents.")

if __name__ == "__main__":
    asyncio.run(main())
