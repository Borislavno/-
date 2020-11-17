from aiogram import types
from aiogram.dispatcher.filters import CommandStart

from filters import Allowed
from loader import dp, db


one= db.select_all_users()


@dp.message_handler( Allowed(),text='йо')
async def sadjasdja(message: types.Message):
    await message.answer('с фильтром')




@dp.message_handler(text='йо')
async def sadasdad(message: types.Message):
    await message.answer('без фильтра')
    await db.add_user(id=message.from_user.id,name=message.from_user.full_name,
                      balance=0,referal=1)




