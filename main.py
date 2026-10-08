from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from config.settings import BOT_TOKEN
import asyncio

from handlers.users.start import router as start_router
from handlers.users.help import router as help_router
from handlers.users.tolov import router as tolov_router
from handlers.users.tugma import router as tugma
from handlers.inline.photo import router as photo
from handlers.inline.audio import router as audio
from handlers.inline.voice import router as voice
from handlers.inline.article import router as article
from handlers.inline.gif import router as gif_router
from handlers.users.car import router as car_router
from handlers.groups.startGroup import router as startGroup

dp = Dispatcher()


async def main():
    bot = Bot(token=BOT_TOKEN,
              default=DefaultBotProperties(parse_mode=ParseMode.HTML))


    dp.include_router(start_router)
    dp.include_router(help_router)
    dp.include_router(tolov_router)
    dp.include_router(car_router)
    dp.include_router(tugma)
    dp.include_router(photo)
    dp.include_router(gif_router)
    dp.include_router(audio)
    dp.include_router(voice)
    dp.include_router(article)
    dp.include_router(startGroup)


    print("Bot ishga tushdi")
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())