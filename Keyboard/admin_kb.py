from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

a1 = KeyboardButton('Список промоутеров')
a2 = KeyboardButton('Добавить в BD')
a3 = KeyboardButton('Выход')
start_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
start_kb.add(a1).add(a2).add(a3)

sand_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
sand_kb.add(KeyboardButton('Назад'))

b1 = KeyboardButton('Промоутер')
b2 = KeyboardButton('АДМИН')
b3 = KeyboardButton('Заказчик')
admin_panel_start = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
admin_panel_start.add(b1, b2, b3)