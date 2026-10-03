from  aiogram import filters,types

class  GroupFilters(filters.BaseFilter):
    async def __call__(self, msg: types.Message):
        return msg.chat.type in ['group', 'supergroup']