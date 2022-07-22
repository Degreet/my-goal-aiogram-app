from aiogram import types
from keyboards import create_goal_keyboard
from handlers.goal import send_goal_info
from db import database


async def start(message: types.Message):
    user_id = message.from_user.id
    user = database.get_user(user_id)

    if not user:
        user = database.reg_user(user_id)

    if not user[2]: # если нет цели
        return await message.answer("У тебя еще нет цели. Хочешь создать ее?", reply_markup=create_goal_keyboard)

    await send_goal_info(message)
