import asyncio
import logging
from aiogram import Bot, Dispatcher
from handler import start, allhandlers, admin

logging.basicConfig(level=logging.INFO)




async def main():
    bot = Bot(token="7650674022:AAG7aNieJIBj2cLEn8hW3LXsE3mKiolzMlE")
    dp = Dispatcher()
    dp.include_router(start.router)
    dp.include_router(allhandlers.router)
    dp.include_router(admin.router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())