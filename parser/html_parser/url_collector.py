import pickle
from typing import List

import aiohttp
from bs4 import BeautifulSoup

LOGIN_URL = 'https://kmpo.eljur.ru/ajaxauthorize'
BOARD_URL = 'https://kmpo.eljur.ru/journal-board-action'
COOKIES_FILE = 'cookies.pkl'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/142.0.7444.163 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "Referer": "https://kmpo.eljur.ru/",
    "Connection": "keep-alive"
}

"""
Функция проходит авторизацию под учетной записью студента, сохраняет кукис для входа и стягивает html со страницы объявлений
"""
async def get_board_html(login, password) -> str:
    """Получение HTML со страницы объявлений"""
    async with aiohttp.ClientSession(headers=headers) as session:
        # Загрузка cookies
        try:
            with open(COOKIES_FILE, 'rb') as f:
                cookies = pickle.load(f)
                session.cookie_jar.update_cookies(cookies)
                print('Cookies loaded')
        except FileNotFoundError:
            print('Cookies file not found. Creating new one')

        # Попытка получить страницу с загруженными cookies
        async with session.get(BOARD_URL) as response:
            html = await response.text()
            if '<title>Объявления&nbsp;&mdash; Электронный журнал&nbsp;&mdash; Колледж многоуровневого  профессионального образования&nbsp;&mdash; Москва</title>' in html:
                print('Data collected')
                return html

        # При неудаче попытка авторизации и обновление cookies
        async with session.post(LOGIN_URL, data={'username': login, 'password': password, 'return_uri': '/'}) as response:
            if response.status != 200:
                raise Exception('Login failed')

            # Сохранение новых cookies
            cookies_to_save = {c.key: c.value for c in session.cookie_jar}
            with open(COOKIES_FILE, 'wb') as f:
                pickle.dump(cookies_to_save, f, protocol=pickle.HIGHEST_PROTOCOL)
                print('Cookies saved')

        async with session.get(BOARD_URL) as response:
            html = await response.text()

        return html

"""
Функция вытаскивает из чистого html ссылки на скачивание файлов с заменами в виде списка
"""
async def get_url_list(html) -> List[str]:
    """Получение списка ссылок с сайта"""

    bs = BeautifulSoup(html, 'html.parser')
    links = bs.select('a[title*="Замен"]')
    links = [link.get('href') for link in links if link.get('href')]
    return links

