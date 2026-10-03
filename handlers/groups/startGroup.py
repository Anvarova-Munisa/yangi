from aiogram import Router,types,filters
from filters.group import GroupFilters
from filters.admin import GroupAdminFilter
router = Router()
@router.message(GroupFilters())
async def start(msg: types.Message):
    await msg.answer("qondayee")