from contextlib import asynccontextmanager

from sqlalchemy import exc
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncAttrs
from sqlalchemy.orm import DeclarativeBase

from central_api.app.config import DATABASE_URL

"""Точка доступа к бд"""

engine = create_async_engine(DATABASE_URL, echo=False)
SessionLocal = async_sessionmaker(bind=engine, expire_on_commit=False)

class Base(AsyncAttrs, DeclarativeBase):
    pass

@asynccontextmanager
async def get_db_session():
    """Контекстный менеджер для безопасной работы с БД"""
    session = SessionLocal()
    try:
        yield session
        await session.commit()
    except exc.SQLAlchemyError as e:
        await session.rollback()
        print(f"Ошибка при работе с БД: {e}")
        raise
    finally:
        await session.close()

async def get_db_session_dep():
    session = SessionLocal()
    try:
        yield session
        await session.commit()
    except:
        await session.rollback()
        raise
    finally:
        await session.close()