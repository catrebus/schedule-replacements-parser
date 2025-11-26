from fastapi import APIRouter

healthRouter = APIRouter()
@healthRouter.get("/health")
async def health():
    return {"status": "OK"}