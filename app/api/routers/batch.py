from fastapi import APIRouter
from pydantic import BaseModel
from typing import List
from app.pipelines.analyzer import analyze_review

router = APIRouter(prefix="/api/v1")

class BatchIn(BaseModel):
    reviews: List[str]
    include_baseline: bool = True

@router.post("/batch-analyze")
async def batch_analyze(body: BatchIn):
    results = []
    for r in body.reviews:
        results.append(await analyze_review(r, body.include_baseline))
    return {"results": results}
