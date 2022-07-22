from aiogram import types
from aiogram.dispatcher import FSMContext
from keyboards import goal_control_keyboard
from db import database
from states import Goal


async def send_goal_info(message: types.Message):
    user_id = message.from_user.id
    user = database.get_user(user_id)

    await message.answer(f"""
<b>Ваша цель: {user[2]}</b>
<i>{str(user[4])}/{str(user[3])}</i>
    """, parse_mode="HTML", reply_markup=goal_control_keyboard)


async def up_goal(message: types.Message):
    database.up_goal(message.from_user.id)
    await send_goal_info(message)


async def clear_goal(message: types.Message):
    database.clear_goal(message.from_user.id)
    await send_goal_info(message)


async def enter_goal(message: types.Message):
    await Goal.goal.set() # заходим в fsm
    await message.answer("Придумай цель")


async def enter_goal_count(message: types.Message, state: FSMContext):
    goal = message.text # получаем цель
    await state.update_data(goal=goal) # сохраняем в стейт

    await Goal.next() # идем дальше
    await message.answer("Введите кол-во выполнений на день")


async def create_goal(message: types.Message, state: FSMContext):
    goal_count = message.text # получаем кол-во выполнений на день

    # проверяем на число
    if not str(goal_count).isnumeric():
        return await message.answer("Введите число")
    
    result_state = await state.get_data() # получаем стейт
    result_state["goal_count"] = int(goal_count) # обновляем стейт
    
    user_id = message.from_user.id
    database.create_goal(user_id, result_state["goal"], result_state["goal_count"])

    await state.finish() # завершаем fsm
    await send_goal_info(message)
