# from aiogram import Router, F,Bot
# from aiogram.types import Message, CallbackQuery, InlineKeyboardButton
# from aiogram.filters import Command
# from aiogram.utils.keyboard import InlineKeyboardBuilder
# from config.settings import ADMINS
from aiogram import Router, F, Bot
from aiogram.types import Message, CallbackQuery, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder
from config.settings import BOT_TOKEN
from config.settings import ADMINS
# from handlers.inline.photo import photo

router = Router()
bot = Bot(token=BOT_TOKEN)


CAR_PHOTOS = {
    "gentra": "AgACAgIAAxkBAAOdasDIAwFsBeV44GHVuNCFytpTWBIAAs4baxvtHwlKoMh3LpPFYqoBAAMCAAN5AAM9BA",
    "cobalt": "AgACAgIAAxkBAAOfasDIzZNl33P2rtFVUMLy9pexqvUAAqgcaxtbjAlK87MG0que1K8BAAMCAAN5AAM9BA",
    "malibu": "AgACAgIAAxkBAAOhasDI1A1VmU668eL6siaD03K6IFoAAqkcaxtbjAlK8FQAAXfV9azyAQADAgADeQADPQQ",
    "byd": "AgACAgIAAxkBAAOjasDJLmeqV-7Z4gRKuxDA5q0Kkx4AAqocaxtbjAlKBgq4w3ZY4J4BAAMCAAN5AAM9BA",
    "tesla": "AgACAgIAAxkBAAOtasDJl850HRoAAZg1UR99g_zZwpmIAAKwHGsbW4wJSs01BMESOdryAQADAgADeAADPQQ",
    "kia": "AgACAgIAAxkBAAOpasDJRm5VYcxZdsUSZseHyKU_idsAAq0caxtbjAlKGHSq3FOrixsBAAMCAAN5AAM9BA",
    "hyundai": "AgACAgIAAxkBAAOlasDJNij8_ReS2BkDRQeUrNfS1g8AAqscaxtbjAlKKeUfKVKyCu0BAAMCAAN5AAM9BA"
}


@router.message(Command("car"))
async def car_start(message: Message):
    b = InlineKeyboardBuilder()
    b.add(
        InlineKeyboardButton(text="Oddiy mashinalar", callback_data="type_oddiy"),
        InlineKeyboardButton(text="Elektromobillar", callback_data="type_elektro"),
        InlineKeyboardButton(text="Inamarkalar", callback_data="type_inamarka")
    )
    b.adjust(1)

    await message.answer(
        text="Avto Salonga xush kelibsiz!\nKategoriyalardan birini tanlang:",
        reply_markup=b.as_markup()
    )


@router.callback_query(F.data.startswith("type_"))
async def car_type2(call: CallbackQuery):
    car_type = call.data.split("_")[1]
    b = InlineKeyboardBuilder()

    if car_type == "oddiy":
        b.add(
            InlineKeyboardButton(text="Gentra", callback_data="model_gentra"),
            InlineKeyboardButton(text="Cobalt", callback_data="model_cobalt"),
            InlineKeyboardButton(text="Malibu", callback_data="model_malibu")
        )
    elif car_type == "elektro":
        b.add(
            InlineKeyboardButton(text="BYD Song Plus", callback_data="model_byd"),
            InlineKeyboardButton(text="Tesla Model Y", callback_data="model_tesla")
        )
    elif car_type == "inamarka":
        b.add(
            InlineKeyboardButton(text="Kia K5", callback_data="model_kia"),
            InlineKeyboardButton(text="Hyundai Sonata", callback_data="model_hyundai")
        )

    b.adjust(2)
    b.row(InlineKeyboardButton(text="Orqaga", callback_data="back_to_types"))

    await call.message.edit_text(text="Quyidagi mashinalardan birini tanlang:", reply_markup=b.as_markup())
    await call.answer()


@router.callback_query(F.data.startswith("model_"))
async def car_model(call: CallbackQuery):
    model_name = call.data.split("_")[1]
    b = InlineKeyboardBuilder()

    b.add(
        InlineKeyboardButton(text="Oq", callback_data=f"color_{model_name}_oq"),
        InlineKeyboardButton(text="Qora", callback_data=f"color_{model_name}_qora"),
        InlineKeyboardButton(text="qizil", callback_data=f"color_{model_name}_qizil")
    )
    b.adjust(2)
    b.row(InlineKeyboardButton(text="Orqaga", callback_data="back_to_types"))

    await call.message.edit_text(text=f"{model_name.upper()} mashinasi uchun rang tanlang:", reply_markup=b.as_markup())
    await call.answer()


@router.callback_query(F.data.startswith("color_"))
async def car_color(call: CallbackQuery):
    data_parts = call.data.split("_")
    model_name = data_parts[1]
    color_name = data_parts[2]

    await call.message.delete()

    tel_tugma = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="📱 Telefon raqamni yuborish", request_contact=True)]
        ],
        resize_keyboard=True,
        one_time_keyboard=True
    )
    global moshina_saqla, rang_saqla
    moshina_saqla = model_name
    rang_saqla = color_name

    await call.message.answer(
        text="Buyurtmani rasmiylashtirish uchun pastdagi tugmani bosib, telefon raqamingizni yuboring:",
        reply_markup=tel_tugma
    )
    await call.answer()


@router.message(F.contact)
async def kontakt_qabul(message: Message):
    telefon_nomer = message.contact.phone_number
    kim = message.from_user.first_name
    username = message.from_user.username or "Mavjud emas"

    await message.answer(text="Raqamingiz qabul qilindi.", reply_markup=ReplyKeyboardRemove())

    photo_id = CAR_PHOTOS.get(moshina_saqla, "")

    await message.answer_photo(
        photo=photo_id,
        caption=f"Mashina: {moshina_saqla.upper()}\n"
                f"Rang: {rang_saqla.capitalize()}\n"
                f"Holati: Yangi (Salon)\n\n"
                f"Rahmat! Buyurtmangiz qabul qilindi. Tez orada aloqaga chiqamiz!"
    )

    admin_xabari = (
        "YANGI BUYURTMА!\n\n"
        f"Mijoz: {kim}\n"
        f"Tel: {telefon_nomer}\n"
        f"Telegram: @{username}\n\n"
        " Tanlangan mashina:\n"
        f"Moshina: {moshina_saqla.upper()}\n"
        f"Rang: {rang_saqla.capitalize()}"
    )

    try:
        await bot.send_message(chat_id=ADMINS, text=admin_xabari)
    except:
        print("Adminga xabar ketmadi")


@router.callback_query(F.data == "back_to_types")
async def types23(call: CallbackQuery):
    b = InlineKeyboardBuilder()
    b.add(
        InlineKeyboardButton(text="Oddiy mashinalar", callback_data="type_oddiy"),
        InlineKeyboardButton(text="Elektromobillar", callback_data="type_elektro"),
        InlineKeyboardButton(text="Inamarkalar", callback_data="type_inamarka")
    )
    b.adjust(1)

    await call.message.edit_text(text="Mashina turini tanlang:", reply_markup=b.as_markup())
    await call.answer()