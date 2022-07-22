from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

goal_control_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
goal_control_keyboard.add(KeyboardButton("Повысить цель"))
goal_control_keyboard.add(KeyboardButton("Очистить"))