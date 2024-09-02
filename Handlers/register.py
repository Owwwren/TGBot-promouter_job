from aiogram import types, Dispatcher
from config import bot, status
from Keyboard import kstart, admin_panel_start, start_kb, sand_map
from db_config.Sq_admin_config import SQLighter


ID = 0
USER = 0
db = SQLighter('db.db')

async def start(message: types.Message):
    global ID
    global mes
    ID = message.from_user.id
    if message.text == "/start":
        if db.selekt_id_admin(message.from_user.id) :
            if db.selekt_status_admin('ADMIN', id=ID):
                mes = await message.answer("Выберити необходимую панель", reply_markup=admin_panel_start)
                await message.delete()
                await status.start_admin_panel.set()
                db.delete_all(message.from_user.id, photo=0)
            elif db.selekt_status_admin('CUST', id=ID):
                await message.answer("HELLO!", reply_markup=kstart)
                await message.delete()
                await status.job.set()
                db.delete_all(message.from_user.id, photo=0)
            else:
                await message.answer(f"Для начала работы нажмите\n ⟪В работе⟫", reply_markup=kstart)
                await message.delete()
                await status.job.set()
                db.delete_all(message.from_user.id, photo=0)
        else:
            await message.answer("Вас нет в базе, обратитесь к админестратору")
    elif message.text == "id":
        global USER
        USER = message.from_user.id, message.from_user.first_name
        await bot.send_message(1853593910, USER)
    elif message.text == '45g67788794357887567b6bbbBnm786NN998Mm89m786m79976':
        await bot.send_message(message.from_user.id, 'Добро пожаловать в меню админа!'
                                                    '\n Выберети что хотите сделать', reply_markup=start_kb)
        await status.admin_start.set()
    else:
        await message.answer('Напишите команду /start')

#@dp.message_handler(state=status.start_admin_panel)
async def start_admin_panel(message: types.Message):
    if message.text == 'АДМИН':
        await bot.send_message(message.from_user.id, 'Добро пожаловать в меню админа!'
                                                     '\n Выберети что хотите сделать', reply_markup=start_kb)
        await status.admin_start.set()
        db.delete_all(message.from_user.id, photo=0)
        db.connection.commit()
        await mes.delete()
    elif message.text == 'Промоутер':
        await message.answer(f"Для начала работы нажмите\n ⟪В работе⟫", reply_markup=kstart)
        await message.delete()
        await status.job.set()
        db.delete_all(message.from_user.id, photo=0)
        db.connection.commit()
        await mes.delete()
    elif message.text == 'Заказчик':
        await message.answer("HELLO!", reply_markup=kstart)
        await message.delete()
        await status.job.set()
        db.delete_all(message.from_user.id, photo=0)
        db.connection.commit()
        await mes.delete()
    else:
        await message.answer('Выберити кнопку в панели.')

#@dp.message_handler(state=status.job)
async def job(message: types.Message):
    global number
    global mes
    if message.text == "🏆 В работе":
        await message.delete()
        await status.map.set()
        await bot.send_message(message.from_user.id, 'Введите номер карты.', reply_markup=sand_map)
        number = 0
    elif message.text == '45g67788794357887567b6bbbBnm786NN998Mm89m786m79976':
        await bot.send_message(message.from_user.id, 'Добро пожаловать в меню админа!'
                                                    '\n Выберети что хотите сделать.', reply_markup=start_kb)
        await status.admin_start.set()
    elif message.text == '/start':
        if db.selekt_status_admin('ADMIN', id=ID):
            mes = await message.answer("Выберити необходимую панель.", reply_markup=admin_panel_start)
            await message.delete()
            await status.start_admin_panel.set()
            db.delete_all(message.from_user.id, photo=0)
        else:
            await message.answer('Нажмите ⟪В работе⟫.')
            await message.delete()
    else:
        await message.answer('Нажмите ⟪В работе⟫.')
        await message.delete()


def register_handler_register(dp: Dispatcher):
    dp.register_message_handler(start_admin_panel, state=status.start_admin_panel)
    dp.register_message_handler(start, content_types=['text'], state=None)
    dp.register_message_handler(job, state=status.job)