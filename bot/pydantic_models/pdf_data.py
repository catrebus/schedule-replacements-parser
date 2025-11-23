from typing import List

from pydantic import BaseModel

from bot.pydantic_models import Replacement


class PdfData(BaseModel):
    url: str
    replacements: List[Replacement]