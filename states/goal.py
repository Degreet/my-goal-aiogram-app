from aiogram.dispatcher.filters.state import State, StatesGroup


class Goal(StatesGroup):
    goal = State()
    goal_count = State()
