from app.services.llm import chat_json

BASELINE_TMPL = """Review: {review}
Aspect: {aspect}
Classify sentiment towards the aspect as one of: positive, negative, neutral.
Return strict JSON: {{"sentiment":"...", "confidence":0.0, "reasoning":"..."}}"""

async def classify_baseline(review: str, aspect: str) -> dict:
    return await chat_json(BASELINE_TMPL.format(review=review, aspect=aspect))
