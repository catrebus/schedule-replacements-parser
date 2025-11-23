import aiohttp

from parser.config import ELJUR_LOGIN, ELJUR_PASSWORD, CENTRAL_API_KEY, CENTRAL_API_URL
from parser.html_parser import get_board_html, get_url_list, download_pdf
from parser.pdf_parser import extract_text_async
from parser.pydantic_models import PdfData


async def send_replacements():
    html = await get_board_html(ELJUR_LOGIN, ELJUR_PASSWORD)

    urls = await get_url_list(html)
    if not urls:
        print('Url list is empty')
        return

    headers = {
        'API-KEY': CENTRAL_API_KEY
    }

    async with aiohttp.ClientSession(headers=headers) as session:
        for url in urls:

            # Скачивание pdf
            try:
                await download_pdf(url)
            except Exception as e:
                print(f'Failed to download {url} | {e}')
                continue

            # Парсинг pdf
            try:
                replacements = await extract_text_async()
            except Exception as e:
                print(f'Failed to extract {url} | {e}')
                continue

            # Проверка на наличие замен в файле
            if len(replacements) == 0:
                print('No replacements found')
                continue

            # Формирование объекта для отправки
            pdfData = PdfData(url=url, replacements=[replacement.model_dump() for replacement in replacements])

            # Пост запрос к центральному апи
            try:
                async with session.post(f'{CENTRAL_API_URL}/upload_pdf', json=pdfData.model_dump(), timeout=10) as response:

                    if response.status == 200:
                        print('Data successfully sent to central api')
                        continue

                    print('Failed to send data to central api')
                    print(await response.text())
            except aiohttp.ClientError as e:
                print(f'Failed to send data to central api: {e}')