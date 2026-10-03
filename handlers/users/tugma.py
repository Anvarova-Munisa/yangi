# from aiogram import Router,types,F
# from aiogram.types import Message
#
# router = Router()
# @router.message(F.photo)
# async def get(msg:Message):
#     await msg.answer(f"{msg.photo[-1].file_id}")




from aiogram import Router, F
from aiogram.types import Message

router = Router()

@router.message(F.text)
async def tugma2r(msg: Message):
    await msg.answer(
        text=f"Bot dan foydanala olishiz uchun.\n"
             f"Siz yozgan xabar: {msg.text}\n\n"
             f"Avtosalon loyihasini boshlash uchun /car komandasini bosing."
    )