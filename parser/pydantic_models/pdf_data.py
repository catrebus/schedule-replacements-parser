from typing import List

from pydantic import BaseModel

from parser.pydantic_models import Replacement


class PdfData(BaseModel):
    url: str
    replacements: List[Replacement]