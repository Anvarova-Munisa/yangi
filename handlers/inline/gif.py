from aiogram import Router,types,F
router = Router()
giflar = [
"CgACAgQAAxkBAAOVasCpvf302XU7dOsCtGl_VuvRns8AAugNAALd00lQRxL8YxeQrCc9BA",
"CgACAgIAAxkBAAOZasCrgCrBYsbwVJGMl0hlZs5vgYUAAjafAAIShShIW8auxWQdn9Q9BA",
"CgACAgIAAxkBAAOaasCrgkVCk52ZthYYCBNqoPOjAhUAAnaiAAJlHjhLtxaCWVvah-w9BA",
"CgACAgIAAxkBAAObasCronyX9LHsbKLwlQ5gBXuXRCIAAsQRAAK8YkBI-Illk0nJHJg9BA",

]


@router.inline_query(F.query.in_(["gif", "giff"]))
async def gif(query: types.InlineQuery):
    results = []
    i = 1


    for file_id in giflar:
        results.append(
            types.InlineQueryResultCachedGif(
                id=str(i),
                gif_file_id=file_id,
                title=f"Ajoyib gif {i}",
                caption="bola"
            )
        )
        i = i + 1

    await query.answer(results=results, cache_time=1, is_personal=True)

