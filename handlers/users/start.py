from aiogram import Router,filters,types,Bot,F
from aiogram.types import Message
from aiogram.filters import Command
from filters.user import UserFilters
from config.settings import ADMINS
from filters.admin import AdminFilters
from aiogram.exceptions import TelegramAPIError

router = Router()

@router.message(filters.Command("start"), UserFilters(),AdminFilters())
async def start_command(msg: types.Message, bot:Bot):
    ism = msg.from_user.first_name
    id = msg.from_user.id
    n = "sizning botingzga yangi azo qoshildi"
    n += f"ism: {ism}\nid: {id}"
    bs = "Assalomi alaykum"
    bs += "yordam uchun"
    await msg.answer(bs)
    for admin in ADMINS:
        try:
            await bot.send_message(chat_id=admin,text=n)
        except TelegramAPIError:
            continue


