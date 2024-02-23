from sqlalchemy import Integer, and_, func, insert, select, text, update, bindparam
from bot.db_orm.database import async_engine, sync_engine
from bot.db_orm.models.base_models import DataEoraOrm, Base


class AsyncCore:

    @staticmethod
    async def insert_data(data: dict):
        async with async_engine.connect() as conn:
            stmt_1 = insert(DataEoraOrm).values(data)
            await conn.execute(stmt_1)
            await conn.commit()

    @staticmethod
    async def select_data(id: int):
        async with async_engine.connect() as conn:
            query = select(DataEoraOrm).where(DataEoraOrm.id == id)
            result = await conn.execute(query)
            data = result.fetchall()
            return data

    @staticmethod
    async def update_data(id: int, new_data: dict):
        async with async_engine.connect() as conn:
            stmt = update(DataEoraOrm).values(data=new_data).where(DataEoraOrm.id == id)
            await conn.execute(stmt)
            await conn.commit()


class SyncCore:
    @staticmethod
    def create_tables():
        Base.metadata.drop_all(sync_engine)
        Base.metadata.create_all(sync_engine)
