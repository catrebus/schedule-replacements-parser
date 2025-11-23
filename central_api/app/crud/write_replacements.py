import datetime

from sqlalchemy import select

from central_api.app.database import PdfDownloadUrl, Replacement, ReplacementType


async def write_replacements(session, pdfData):
    """Запись информации о заменах в бд"""
    # Создание записи записываемом файле
    pdfDownloadUrl = PdfDownloadUrl(url=pdfData.url, created_at=datetime.datetime.now())
    session.add(pdfDownloadUrl)
    await session.flush()

    # Создание записей о заменах из файла
    urlId = pdfDownloadUrl.id
    for replacement in pdfData.replacements:
        dbReplacement = Replacement(date=replacement.date,
                                  group=replacement.group,
                                  teacher_before=replacement.teacherBefore,
                                  pair_number_before=replacement.pairNumberBefore,
                                  discipline_before=replacement.disciplineBefore,
                                  class_before=replacement.classBefore,
                                  teacher_now=replacement.teacherNow,
                                  pair_number_now=replacement.pairNumberNow,
                                  discipline_now=replacement.disciplineNow,
                                  class_now=replacement.classNow,
                                  url_id=urlId)
        session.add(dbReplacement)
        await session.flush()

        # Создание записей и изменениях от этой замены
        for changeType in replacement.changeType:
            replacementType = ReplacementType(replacement_id=dbReplacement.id,
                                              type=changeType)
            session.add(replacementType)

async def is_url_exists(session, pdfData):
    url = pdfData.url

    stmt = select(PdfDownloadUrl).where(PdfDownloadUrl.url == url)
    result = await session.execute(stmt)
    result = result.scalar()

    return True if result else False


