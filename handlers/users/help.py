from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

router = Router()

@router.message(Command("help"))
async def help_command(msg: Message):
    text = (
        "Yordam bo'limi:\n\n"
        "Agarda bot ishlamay qolsa qaytadan /start buyrug'ini bosing.\n"
        "Avtosalondan mashina tanlash uchun /car buyrug'idan foydalaning.\n"
        "Botdan kengroq foydalanish uchun /buy buyrug'ini bering\n"
        "Muammo yuzaga kelsa admin bilan bog'laning."
    )
    await msg.answer(text=text)