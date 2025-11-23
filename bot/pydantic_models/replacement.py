from typing import List, Optional

from pydantic import BaseModel


class Replacement(BaseModel):
    date: str
    group : str
    changeType: List[str]
    teacherBefore: Optional[str] = None
    pairNumberBefore: int
    disciplineBefore: Optional[str] = None
    classBefore: Optional[str] = None
    teacherNow: Optional[str] = None
    pairNumberNow: int
    disciplineNow: Optional[str] = None
    classNow: Optional[str] = None