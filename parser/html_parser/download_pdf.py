from pathlib import Path

import aiohttp

"""
Функция пишет информацию, полученную из запроса, в pdf файл
"""
async def download_pdf(url : str, filename : str = 'last_changes.pdf') -> None:
    """Скачивание файла по ссылке"""
    # Заголовки для корректного запроса
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Referer": "https://kmpo.eljur.ru/journal-board-action",
    }
    # Get запрос
    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get(url) as response:
            # Проверка статуса запроса
            if response.status != 200:
                raise Exception(f'Ошибка скачивания: {response.status}')

            # Создание папки загрузок, если не существует
            ROOT = Path(__file__).resolve().parents[1]
            DOWNLOAD_DIR = ROOT / "downloads"
            DOWNLOAD_DIR.mkdir(exist_ok=True)

            # Запись данных в файл
            with open(DOWNLOAD_DIR / filename, 'wb') as f:
                while True:
                    chunk = await response.content.read(1024)
                    if not chunk:
                        break
                    f.write(chunk)

    print(f'Файл сохранен: {filename}')