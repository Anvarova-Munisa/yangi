from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

router = Router()

@router.message(Command("help"))
async def help_command(message: Message):
    await message.answer(
        text="Yordam bo'limi:\n\n"
             "Agarda bot ishlamay qolsa qaytadan /start buyrug'ini bosing.\n"
             "Avtosalondan mashina tanlash uchun /car buyrug'idan foydalaning.\n"
             "Muammo yuzaga kelsa admin bilan bog'laning."
    )