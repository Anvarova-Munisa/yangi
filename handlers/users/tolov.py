from aiogram import Router, Bot, types, F
from aiogram.filters import Command
from aiogram.enums import ContentType

router = Router()

PAYMENT_TOKEN ="398062629:TEST:999999999_F91D8F69C042267444B74CC0B3C747757EB0E065"


@router.message(Command('buy'))
async def send(message: types.Message, bot: Bot):
    prices = [types.LabeledPrice(label='Premium Tarif', amount=5000000)]

    await bot.send_invoice(
        chat_id=message.chat.id,
        title="Bot Premium Tarifi",
        description="Botdagi barcha imkoniyatlarni ochish uchun to'lov qiling.",
        provider_token=PAYMENT_TOKEN,
        currency="UZS",
        prices=prices,
        start_parameter="premium-activation",
        payload="premium_user_payment"
    )


@router.pre_checkout_query()
async def process(pre_checkout_query: types.PreCheckoutQuery, bot: Bot):
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


@router.message(F.content_type == ContentType.SUCCESSFUL_PAYMENT)
async def payment(message: types.Message):
    payment_info = message.successful_payment

    await message.answer(
        f"To'lovingiz muvaffaqiyatli qabul qilindi!\n\n"
        f"To'langan summa: {payment_info.total_amount // 100} UZS\n\n"
        f"Sizning Premium maqomingiz faollashtirildi!"
    )


