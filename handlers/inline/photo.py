from aiogram import Router,types,F
router = Router()


animals = [
    "AgACAgIAAxkBAAOPasCozfIy-QABSknxst1rFAXOw_muAALj0jEb8SyoSeaHtkJBhPVYAQADAgADeQADPQQ",
"AgACAgIAAxkBAAOOasCoryRFflvuWFyhsVtO0KDpo1cAAgEcaxtbjAlKWCMS_00ujj8BAAMCAAN5AAM9BA",
"AgACAgIAAxkBAAOSasCpMvJCT_Ac37YheysrhWbuU58AAgMcaxtbjAlKs-naP9MiUxABAAMCAAN5AAM9BA",
"AgACAgIAAxkBAAOTasCpPwYF1KbkRTCVyBcsCBRPCnIAAgQcaxtbjAlKojmCi9PvQo0BAAMCAAN5AAM9BA",


 ]

@router.inline_query(F.query.in_(["rasm", "photo"]))
async def photo(query: types.InlineQuery):
    results = []
    i = 1
    for url in animals:
        results.append(
            types.InlineQueryResultCachedPhoto(
                id=str(i),
                photo_file_id=url
            )
        )
        i = i + 1
    await query.answer(results=results, cache_time=1, is_personal=True)




