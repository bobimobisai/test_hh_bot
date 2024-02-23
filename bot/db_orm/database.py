from typing import Annotated
from sqlalchemy import String, create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from bot.db_orm.config_db import settings

sync_engine = create_engine(url=settings.DATABASE_URL_psycopg, echo=True)
async_engine = create_async_engine(url=settings.DATABASE_URL_asyncpg, echo=True)


async_session = async_sessionmaker(async_engine)
sync_session = sessionmaker(sync_engine)


# Custom type
str_264 = Annotated[str, 264]


class Base(DeclarativeBase):
    type_annotatid_map = {str_264: String(264)}
