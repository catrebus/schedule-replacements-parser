from fastapi import FastAPI

from central_api.app.middlewares import LoggingMiddleware
from central_api.app.routers import BotRouter, parserRouter, healthRouter

# Основное приложение
app = FastAPI(title="Central API", version="1.0.0", description="API for tracking schedule replacements")

# Подключение routers
app.include_router(BotRouter, prefix="/bot", tags=["Bot"])
app.include_router(parserRouter, prefix="/parser", tags=["Parser"])
app.include_router(healthRouter, tags=["Health"])

# Подключение middleware
app.add_middleware(LoggingMiddleware)


