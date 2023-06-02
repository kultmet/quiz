from typing import AsyncGenerator

import redis
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import DeclarativeMeta, declarative_base, sessionmaker

from src.config import DB_HOST, DB_NAME, DB_PASSWORD, DB_PORT, DB_USERNAME

REDIS = redis.Redis(host='cache', port=6379, decode_responses=True)

DATABASE_URL = (f"postgresql+asyncpg://"
                f"{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")
Base: DeclarativeMeta = declarative_base()


engine = create_async_engine(DATABASE_URL)
async_session_maker = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session
