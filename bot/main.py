from aiogram import Bot, Dispatcher
from aiogram.client.session.aiohttp import AiohttpSession
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage


import asyncio
from config import settings
import logging
from bot.src.commands import router


async def main():
    try:
        session = AiohttpSession()
        bot = Bot(token=settings.BOT_TOKEN_G, session=session)
        dp = Dispatcher(storage=MemoryStorage())
        dp.include_router(router=router)
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
