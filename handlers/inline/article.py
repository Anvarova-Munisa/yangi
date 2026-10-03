# from aiogram import Router,types,F
# router = Router()
#
# @router.inline_query(F.query.startswith("article"))
# async def article(query: types.InlineQuery):
#     text = query.query
#     results = [
#         types.InlineQueryResultArticle(
#             id="1",
#             title="matinning har bir sozining birinchisi kata harf bilina yoziladi",
#             input_message_content=types.InputTextMessageContent(
#                 message_text=text.title(),
#             )
#
#         )
#     ]
#     await query.answer(results=results, cache_time=1,is_personal=True)
from aiogram import Router, types, F

router = Router()


@router.inline_query(F.query.startswith("article"))
async def article(query: types.InlineQuery):
    text = query.query.replace("article", "").strip()

    if not text:
        text = "matn kiriting"

    results = [
        types.InlineQueryResultArticle(
            id="1",
            title="matinning har bir sozining birinchisi kata harf bilina",
            input_message_content=types.InputTextMessageContent(
                message_text=text.title()
            )
        )
    ]
    await query.answer(results=results, cache_time=1, is_personal=True)
