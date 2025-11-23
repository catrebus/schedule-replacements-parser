import asyncio

from parser.services import send_replacements


async def main_loop():
    while True:
        try:
            await send_replacements()
        except Exception as e:
            print(f'Ошибка при отправке замен | {e}')

        await asyncio.sleep(60 * 60 * 2)


if __name__ == '__main__':
    asyncio.run(main_loop())