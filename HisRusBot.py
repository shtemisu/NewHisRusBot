import asyncio
from aiogram import Dispatcher, Bot
from aiogram.fsm.storage.memory import MemoryStorage
import logging
from app.handlers import router1


async def main():
    bot = Bot("6949421058:AAFG_aLGPaXVUu2fHccjun0LbAwwmDY-LjQ", parse_mode="HTML")
    dp = Dispatcher(storage=MemoryStorage())
    dp.include_router(router1)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
