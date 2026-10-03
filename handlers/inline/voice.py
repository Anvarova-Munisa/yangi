from aiogram import Router,types, F
router = Router()
ovozlar = [
  "AwACAgQAAxkBAAOKasCoNnZwCp24DzWFlqWaEU0YDsYAAsAgAAJ4snFRtR_4RedblE49BA",
"AwACAgQAAxkBAAOLasCoPqYthyZv6RfTjLWzgBpRH0YAApgdAAJHlgABUutyovRhqaOiPQQ",
"AwACAgQAAxkBAAOMasCoSequH0ayj629CjptHkDPvwAD-yUAAhjCQVFc7PcPStNPXT0E",
"AwACAgQAAxkBAAONasCoUUr7uioiptvZxsB7R9X7dnwAArggAAKJHbFR_bgf_lLTs9U9BA",
]


@router.inline_query(F.query.in_(["voice", "ovoz"]))
async def voice(query: types.InlineQuery):
    results = []
    i = 1
    for file_id in ovozlar:
        results.append(
            types.InlineQueryResultCachedVoice(
                id=str(i),
                voice_file_id=file_id,
                title=f"Ovoz {i}"
            )
        )
        i = i + 1
    await query.answer(results=results, cache_time=1, is_personal=True)





