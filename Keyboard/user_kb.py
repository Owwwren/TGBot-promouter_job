from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

a1 = KeyboardButton('🏆 В работе')
kstart = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kstart.add(a1)

b1 = KeyboardButton('◀️ Назад')
kjob = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kjob.add(b1)

e1 = KeyboardButton('◀️ Назад')
sand_map = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
sand_map.add(e1)

c1 = KeyboardButton('✅ Завершить подъезд')
c2 = KeyboardButton('✅ Нет подъезда')
pad = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
pad.add(c1).add(c2)

d1 = KeyboardButton('✅ Завершить работу')
pad_undo = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
pad_undo.add(d1)