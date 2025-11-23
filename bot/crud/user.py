import datetime
from zoneinfo import ZoneInfo

from sqlalchemy import select, insert

from bot.database import User, get_db_session


async def create_user(userId):
    async with get_db_session() as session:
        try:
            stmt = insert(User).values(id=userId, created_at=datetime.datetime.now(tz=ZoneInfo('Europe/Moscow'))).prefix_with('IGNORE') # Работает только с MySQL
            await session.execute(stmt)
        except Exception:
            pass

async def get_users():
    async with get_db_session() as session:
        stmt = select(User.id)
        users = await session.execute(stmt)
        users = users.scalars().all()
        return users

