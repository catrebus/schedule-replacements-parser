from fastapi import APIRouter, Depends

from central_api.app.crud import is_url_exists
from central_api.app.crud import write_replacements
from central_api.app.database import get_db_session_dep
from central_api.app.pydantic_models import PdfData
from central_api.app.services import notify_bot

parserRouter = APIRouter()

@parserRouter.post('/upload_pdf')
async def upload_pdf(pdfData: PdfData, session=Depends(get_db_session_dep)):
    """Получение новых замен от парсера"""
    if await is_url_exists(session, pdfData):
        return
    await write_replacements(session, pdfData)
    await notify_bot(pdfData)