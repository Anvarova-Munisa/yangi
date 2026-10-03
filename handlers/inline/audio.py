from aiogram import Router, types,F

router = Router()
audiolar = [
"CQACAgQAAxkBAAOBasCkUD-yIsVlep38EdYnm9mhgAcAAu8fAAIhUJhR-g8CW8Nn0fI9BA",
"CQACAgQAAxkBAAOAasCkSgqvRhq3Kmr8kHWggaftqvgAAiIdAAJ_qNFRxNM0ahvDrHE9BA",
"CQACAgQAAxkBAAOBasCkUD-yIsVlep38EdYnm9mhgAcAAu8fAAIhUJhR-g8CW8Nn0fI9BA",
"CQACAgQAAxkBAAOJasCnsfng5iF8SWDQJcta6bNVDEkAArMeAAIChgFSVpKiaO1yOjc9BA",

]


@router.inline_query(F.query.in_(["audio", "mp3"]))
async def audio(query: types.InlineQuery):
    results = []
    i = 1
    for file_id in audiolar:
        results.append(
            types.InlineQueryResultCachedAudio(
                id=str(i),
                audio_file_id=file_id,
                caption=f"BU audio {i}"
            )
        )
        i = i + 1
    await query.answer(results=results, cache_time=1, is_personal=True)

