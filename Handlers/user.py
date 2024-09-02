from config import bot
from aiogram import types, Dispatcher
from db_config.Sq_user_config import SQLighter
from Keyboard import kstart, pad, pad_undo, kjob
from aiogram.dispatcher import FSMContext
from config import status


"""class status(StatesGroup):
    job = State()
    adres = State()
    photo = State()
    check = State()
    map = State()"""

cl = 0
db = SQLighter('db.db')
number = 0

#@dp.messagae_handler(state=status.map)
async  def map(message: types.Message, state:FSMContext):
    global map
    map = message.text
    if db.admin_exists_map(map=map):
        if db.exists_map(map=map):
            await message.answer('Карта уже пройдена, выберити другую')
        else:
            await message.answer(f'Вы начали карту {map}')
            await status.adres.set()
            await bot.send_message(message.from_user.id, 'Введите адрес', reply_markup=kjob)
    elif message.text == '◀️ Назад':
        await message.answer(f"Для начала работы нажмите\n ⟪В работе⟫", reply_markup=kstart)
        await status.job.set()
    else:
        print(db.admin_exists_map(map=map))
        await  message.answer(f'Карты {map} нет.\nПроверьте номер карты или обратитесь к администратору.')

#@dp.message_handler(state=status.adres)
async def adres(message: types.Message, state:FSMContext):
    global q
    global cl
    global number
    global map
    if message.text == '◀️ Назад':
        await message.answer(f"Для начала работы нажмите\n ⟪В работе⟫", reply_markup=kstart)
        await status.job.set()
    elif message.text == '✅ Завершить работу':
        await bot.send_message(message.from_user.id, "Спасибо за работу!")
        await message.answer(f'Вы прошли подъездов: {number}')
        await message.answer("Для начала работы нажмите <<В работе>>", reply_markup=kstart)
        db.add_pad_map(pad=number, map=map)
        db.delete_all(message.from_user.id, photo=0)
        db.connection.commit()
        await status.job.set()
    else:
        if len(message.text) < 3:
            await message.answer('Это не адрес')
        elif db.exists_adres(message.from_user.id, message.text):
            await message.answer("Вы уже прошли этот дом, выберити другой!")
        else:
            await message.answer("Адрес добавлен")
            q = message.text
            cl = 0
            await status.check.set()
            db.add_user_id(message.from_user.id, message.from_user.first_name, pad=0, map=map)
            db.connection.commit()
            db.add_adres(message.from_user.id, message.text, adres_null=0, map=map)
            if db.exists_pad(message.from_user.id, pad=0, adres=q):
                await bot.send_message(message.from_user.id, "Подъезд 1", reply_markup=pad)
                await bot.send_message(message.from_user.id, "Отправьте 1 фото подъезда.")
                db.update_id_pad(message.from_user.id, pad=1, photo=0)
                db.connection.commit()
            else:
                await message.answer('Проблемы с добавлением адреса.')

#@dp.message_handler(state=status.check, content_types=["text","photo"])
async def check(message: types.Message, state:FSMContext):
    global cl
    global map
    if message.text == '✅ Завершить подъезд':
        await bot.send_message(message.from_user.id, 'Фото отсутствует. Пришлите фото.')
    elif message.text == '✅ Нет подъезда':
        if cl == 0:
            await bot.send_message(message.from_user.id, 'Фото отсутствует. Пришлите фото.')
        else:
            await bot.send_message(message.from_user.id, 'Дом принят')
            await bot.send_message(message.from_user.id, 'Введите адрес или завершите работу', reply_markup=pad_undo)
            await status.adres.set()
    elif message.content_type == 'photo':
        msg = await message.answer('Фото принято')
        db.add_photo(message.from_user.id, message.photo[0].file_id, photo_null=0, adres=q, data=message.date, map=map)
        db.connection.commit()
        global q_photo
        q_photo = message.photo[0].file_id
        await message.answer('Сделайте новое фото или нажмите кнопку <<Завершить подъезд>>')
        await status.photo.set()
        await msg.delete()
        cl = 0
    else:
        await message.answer('Это не фото')

#@dp.message_handler(state=status.photo, content_types=["text", "photo"])
async def photo(message: types.Message, state:FSMContext):
    global cl
    global number


def register_handler_user(dp : Dispatcher):
    dp.register_message_handler(map, state=status.map)
    dp.register_message_handler(adres, state=status.adres)
    dp.register_message_handler(check, state=status.check, content_types=["text", "photo"])
    dp.register_message_handler(photo, state=status.photo, content_types=["text", "photo"])