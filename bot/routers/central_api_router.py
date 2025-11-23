from fastapi import APIRouter

from bot.pydantic_models import PdfData
from bot.services import announce_new_replacements

centralApiRouter = APIRouter()

@centralApiRouter.post("/upload_replacements")
async def upload_replacements(pdfData: PdfData):
    await announce_new_replacements(pdfData)