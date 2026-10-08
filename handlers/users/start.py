from aiogram import Router,filters,types,Bot,F
from aiogram.types import Message
from aiogram.filters import Command
from filters.user import UserFilters
from config.settings import ADMINS
from filters.admin import AdminFilters
from aiogram.exceptions import TelegramAPIError

router = Router()


@router.message(filters.Command("start"), UserFilters(), AdminFilters())
async def start_command(msg: types.Message, bot: Bot):
    KANAL= -1003546954926
    user = await bot.get_chat_member(chat_id=KANAL, user_id=msg.from_user.id)
    if user.status in ['left', 'kicked']:
        btn = [
            [types.InlineKeyboardButton(text="Kanalga a'zo bo'lish", url="https://t.me/+deSEUDcWOvthNmMy")],
            [types.InlineKeyboardButton(text="Tekshirish", callback_data="check")]
        ]
        knopka = types.InlineKeyboardMarkup(inline_keyboard=btn)
        await msg.answer("Botdan foydalanish uchun kanalga a'zo bo'ling!", reply_markup=knopka)
        return
    ism = msg.from_user.first_name
    id = msg.from_user.id

    n = "sizning botingizga yangi azo qoshildi"
    n += f"\nism: {ism}\nid: {id}"
    ba = "Assalomu alaykum\nyordam uchun"
    await msg.answer(ba)

    for admin in ADMINS:
        try:
            await bot.send_message(chat_id=admin, text=n)
        except TelegramAPIError:
            continue


@router.callback_query(F.data == "check")
async def check_sub(call: types.CallbackQuery, bot: Bot):
    KANAL = -1003546954926
    user = await bot.get_chat_member(chat_id=KANAL, user_id=call.from_user.id)

    if user.status not in ['left', 'kicked']:
        await call.message.delete()
        await call.message.answer("Rahmat! Obuna tasdiqlandi. Endi qayta /start bosing.")
    else:
        await call.answer("Siz hali kanalga a'zo bo'lmadingiz!", show_alert=True)