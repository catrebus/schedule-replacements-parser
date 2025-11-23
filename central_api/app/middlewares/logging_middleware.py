import time

from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response

from central_api.app.config import API_KEY


class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start_time = time.time()

        # Логируем запрос
        print(f"[REQUEST] {request.method} {request.url}")

        # Проверка токена
        token = request.headers.get("API-KEY")
        if token != API_KEY:
            return Response("Unauthorized", status_code=401)

        # Передаем управление дальше
        response = await call_next(request)

        # Логируем время обработки
        process_time = time.time() - start_time
        print(f"[RESPONSE] Status: {response.status_code} | Time: {process_time:.3f}s")

        return response