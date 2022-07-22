from aiogram import Dispatcher
from states import Goal
from .start import start
from .goal import enter_goal, enter_goal_count, create_goal, up_goal, clear_goal


def setup_handlers(dp: Dispatcher):
    dp.register_message_handler(start, commands=["start"])
    dp.register_message_handler(up_goal, text="Повысить цель", state="*")
    dp.register_message_handler(clear_goal, text="Очистить", state="*")
    dp.register_message_handler(enter_goal, text="Создать цель", state="*")
    dp.register_message_handler(enter_goal_count, state=Goal.goal)
    dp.register_message_handler(create_goal, state=Goal.goal_count)
