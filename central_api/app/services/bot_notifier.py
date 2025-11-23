import aiohttp

from central_api.app.config import BOT_API_KEY, BOT_URL


async def notify_bot(pdfData):
    headers = {
        "API-KEY": BOT_API_KEY,
    }

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.post(f"{BOT_URL}/upload_replacements", json=pdfData.model_dump()) as response:
            if response.status == 200:
                print('Data successfully sent to bot')
                return
            print(f'Failed to send data to bot: {response.status}')
            print(await response.text())