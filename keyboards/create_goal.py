from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

create_goal_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
create_goal_keyboard.add(KeyboardButton("Создать цель"))
