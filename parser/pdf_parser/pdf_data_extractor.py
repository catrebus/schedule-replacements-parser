import asyncio
import datetime
import re

from typing import List

from pypdf import PdfReader

from parser.pydantic_models import Replacement


def extract_text_sync(fileName: str) -> List[Replacement]:
    reader = PdfReader(fileName)
    changesLines = []
    for page in reader.pages:
        splittedText = page.extract_text().split('\n')
        for text in splittedText:
            if not text:
                continue
            changesLines.append(text)
    for i in range(4):
        changesLines.pop(0)

    changesList = []

    # Парсинг каждой строки замены
    for line in changesLines:

        # Получение даты
        date = line[:10]
        line = line[10:]

        # Получение группы
        groupMatch = re.search(r'301-ИС-23', line)
        if groupMatch:
            group = groupMatch.group()
        else:
            #print('Line parsing error', line)
            continue
        line = line[len(group):]

        # Получение типа замены
        changeTypeMatch = re.match(r'^(.*?)(?=[А-ЯЁ])', line)
        if changeTypeMatch:
            changeType = changeTypeMatch.group(1).strip()
        else:
            print('Line parsing error', line)
            continue
        line = line[len(changeType):]

        if changeType.strip().lower() == 'отмена занятия': # При отмене занятия
            teacherBefore = ''
            for char in line:
                if char.isdigit():
                    numberBefore = int(char)
                    break
                else:
                    teacherBefore = teacherBefore + char
            line = line[len(teacherBefore) + 1:]

            disciplineBefore = line[:15]
            line = line[15:]
            for char in line:
                if char.isdigit() or char == 'П' or char == 'К' or char == 'С':
                    break
                else:
                    disciplineBefore = disciplineBefore + char
                    line = line[1:]
            classBefore = line

            replacement = Replacement(date=datetime.datetime.strptime(date.strip(), "%d.%m.%Y").strftime("%Y-%m-%d"),
                                      group=group.strip(),
                                      changeType=[changeType],
                                      teacherBefore=teacherBefore.strip(),
                                      pairNumberBefore=numberBefore,
                                      disciplineBefore=disciplineBefore.strip(),
                                      classBefore=classBefore.strip(),
                                      teacherNow='',
                                      pairNumberNow=0,
                                      disciplineNow='',
                                      classNow='')
            changesList.append(replacement)
            continue

        elif changeType.strip().lower() == 'добавление занятия': # При добавлении занятия

            teacherNow = ''
            for char in line:
                if char.isdigit():
                    numberNow = int(char)
                    break
                else:
                    teacherNow = teacherNow + char
            line = line[len(teacherNow) + 1:]

            disciplineNow = line[:15]
            line = line[15:]
            for char in line:
                if char.isdigit() or char == 'П' or char == 'К' or char == 'С':
                    break
                else:
                    disciplineNow = disciplineNow + char
                    line = line[1:]
            classNow = line

            replacement = Replacement(date=datetime.datetime.strptime(date.strip(), "%d.%m.%Y").strftime("%Y-%m-%d"),
                                      group=group.strip(),
                                      changeType=[changeType],
                                      teacherBefore='',
                                      pairNumberBefore=0,
                                      disciplineBefore='',
                                      classBefore='',
                                      teacherNow=teacherNow.strip(),
                                      pairNumberNow=numberNow,
                                      disciplineNow=disciplineNow.strip(),
                                      classNow=classNow.strip())
            changesList.append(replacement)
            continue

        # Остальные случаи
        # Получение преподавателя до
        teacherBefore = ''
        for char in line:
            if char.isdigit():
                numberBefore = int(char)
                break
            else:
                teacherBefore = teacherBefore + char
        line = line[len(teacherBefore) + 1:]

        # Получение дисциплины до
        disciplineBefore = line[:15]
        line = line[15:]
        for char in line:
            if char.isdigit() or char == 'П' or char == 'К' or char == 'С':
                break
            else:
                disciplineBefore = disciplineBefore + char
                line = line[1:]

        # Получение кабинета до
        classBefore = line[:2]
        line = line[2:]
        for char in line:
            if not char.isdigit():
                break
            else:
                classBefore = classBefore + char
                line = line[1:]

        teacherNow = ''
        for char in line:
            if char.isdigit():
                numberNow = int(char)
                break
            else:
                teacherNow = teacherNow + char
        line = line[len(teacherNow) + 1:]

        disciplineNow = line[:15]
        line = line[15:]
        for char in line:
            if char.isdigit() or char == 'П' or char == 'К' or char == 'С':
                break
            else:
                disciplineNow = disciplineNow + char
                line = line[1:]
        classNow = line

        changeType = []
        if teacherBefore != teacherNow:
            changeType.append('замена преподавателя')
        if disciplineBefore != disciplineNow:
            changeType.append('замена дисциплины')
        if classBefore != classNow:
            changeType.append('замена кабинета')
        if numberBefore != numberNow:
            changeType.append('перенос занятия')

        replacement = Replacement(date=datetime.datetime.strptime(date.strip(), "%d.%m.%Y").strftime("%Y-%m-%d"),
                                  group=group.strip(),
                                  changeType=changeType,
                                  teacherBefore=teacherBefore.strip(),
                                  pairNumberBefore=numberBefore,
                                  disciplineBefore=disciplineBefore.strip(),
                                  classBefore=classBefore.strip(),
                                  teacherNow=teacherNow.strip(),
                                  pairNumberNow=numberNow,
                                  disciplineNow=disciplineNow.strip(),
                                  classNow=classNow.strip())
        changesList.append(replacement)

    return changesList


async def extract_text_async(fileName: str = 'last_changes.pdf') -> List[Replacement]:
    """Асинхронный парсинг пдф"""
    return await asyncio.to_thread(extract_text_sync, f'downloads/{fileName}')

