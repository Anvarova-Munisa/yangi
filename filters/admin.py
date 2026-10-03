from  aiogram import filters,types,Bot
from config.settings import ADMINS
from filters import user


class AdminFilters(filters.BaseFilter):
    async def __call__(self, msg: types.Message):
        return str(msg.from_user.id) in ADMINS

class GroupAdminFilter(filters.BaseFilter):
    async def __call__(self, msg: types.Message,bot:Bot):
        user = await bot.get_chat_member(msg.chat.id,msg.from_user.id)
        user = user.status
        return user in ["adminstrator","creator"]

