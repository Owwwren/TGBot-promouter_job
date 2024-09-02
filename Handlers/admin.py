from config import bot, status, dp
from aiogram import types, Dispatcher
from db_config.Sq_admin_config import SQLighter
from Keyboard import start_kb, sand_kb, admin_panel_start
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher.filters import Text

db = SQLighter('db.db')
"""class status(StatesGroup):
    admin_start = State()"""

##############InlineKeyboardMarkup####################
ia1 =InlineKeyboardButton(text='Промоутер', callback_data='Промоутер')
ia2 = InlineKeyboardButton(text='Заказчик', callback_data='Заказчик')
ia3 = InlineKeyboardButton(text='Карта', callback_data='Карта')
ia4 = InlineKeyboardButton(text='Назад', callback_data='Назад')
panel_db_ikb = InlineKeyboardMarkup(row_width=1)
panel_db_ikb.add(ia1, ia2, ia3, ia4)
######################################################
##################ADMIN PASSWORD######################
######################################################
##45g67788794357887567b6bbbBnm786NN998Mm89m786m79976##
######################################################


def gen_markup():
    markup = InlineKeyboardMarkup(row_width=1)
    read = db.liset_USER_admin()
    for ret in read:
        markup.insert(InlineKeyboardButton(f'{ret[0]} ⟫ {ret[1]}', callback_data=f'id {ret[0]}'))
    return markup
def ik_cust_markup():
    markup = InlineKeyboardMarkup(row_width=1)
    read = db.liset_CUST_admin()
    for ret in read:
        markup.insert(InlineKeyboardButton(f'{ret[0]} ⟫ {ret[1]}', callback_data=f'cust {ret[0]}'))
    return markup
def gen_markup_adres():
    global MAP
    global ID_ADRES
    global Mm
    markup_adres = InlineKeyboardMarkup(row_width=1)
    read_adres = set(db.selekt_adres_id_admin(id=ID_ADRES, map=MAP))
    for ret_adres in read_adres:
        a1 = InlineKeyboardButton(f'{ret_adres[0]}', callback_data=f'adres {ret_adres[0]}')
        markup_adres.add(a1)
    markup_adres.add(InlineKeyboardButton('Все фото', callback_data='all'))
    markup_adres.add(InlineKeyboardButton('Назад', callback_data='undo_user4'))
    Mm = 0
    return markup_adres
def gen_markup_map():
    global ID_ADRES
    markup_map = InlineKeyboardMarkup(row_width=1)
    read = set(db.liset_MAP_admin(ID_ADRES))
    for ret in read:
        markup_map.insert(InlineKeyboardButton(f'{ret[0]} ⟫ {ret[1]}', callback_data=f'map {ret[0]}'))
    markup_map.add(InlineKeyboardButton('Назад', callback_data='undo_user'))
    return markup_map

@dp.callback_query_handler(Text(startswith='cust '), state=status.prom_info)
async def adres_panel(callback : types.CallbackQuery):
    global mes1
    global CUST
    global WTF
    global MAP
    print(WTF)
    CUST = (callback.data.replace('cust ', ''))
    await mes4.delete()
    if WTF == 'all':
        markup_adres = gen_markup_adres()
        mes1 = await bot.send_message(callback.from_user.id, f'Адреса промоутера\nВсего подъездов: {db.selekt_map_pad_admin(map=MAP)}', reply_markup=markup_adres)
        FILE = db.selekt_all_admin(id=ID_ADRES, map=MAP)
        DEL = await bot.send_message(callback.from_user.id, 'Пользователь заблокировал бота.')
        for photo in FILE:
            await bot.send_photo(CUST, photo[0], f'{photo[1]} Подъезд{photo[2]}')
        await bot.send_message(CUST, f'Всего подъездов: {db.selekt_map_pad_admin(map=MAP)}')
        await DEL.delete()
        await bot.send_message(callback.from_user.id, 'Отчет отправлен')
    elif WTF == 'adres':
        markup_adres = gen_markup_adres()
        mes1 = await bot.send_message(callback.from_user.id, f'Адреса промоутера\nВсего подъездов: {db.selekt_map_pad_admin(map=MAP)}', reply_markup=markup_adres)
        FILE = db.selekt_all_admin(id=ID_ADRES, map=MAP)
        DEL = await bot.send_message(callback.from_user.id, 'Пользователь заблокировал бота.')
        for photo in FILE:
            await bot.send_message(CUST,f'{photo[1]}')
        await bot.send_message(CUST, f'Всего подъездов: {db.selekt_map_pad_admin(map=MAP)}')
        await DEL.delete()
        await bot.send_message(callback.from_user.id, 'Отчет отправлен')


@dp.callback_query_handler(Text(startswith='id '), state=status.prom_info)
async def adres_panel(callback : types.CallbackQuery):
    global ID_ADRES
    global msg4
    ID_ADRES = (callback.data.replace('id ', ''))
    map_panel = gen_markup_map()
    msg4 = await bot.send_message(callback.from_user.id, 'Выберити карту', reply_markup=map_panel)
    await MES.delete()
    await mes.delete()

@dp.callback_query_handler(text='all', state=status.prom_info)
async def all(callback : types.CallbackQuery):
    global mes2
    await mes1.delete()
    ikb_all = InlineKeyboardMarkup(row_width=2).add(InlineKeyboardButton('Себе', callback_data='report_i'), (InlineKeyboardButton('Заказчику', callback_data='report_customer')), (InlineKeyboardButton('Назад', callback_data='undo_user2')))
    mes2 = await bot.send_message(callback.from_user.id, 'Кому отправить отчет', reply_markup=ikb_all)

@dp.callback_query_handler(Text(startswith='report_'), state=status.prom_info)
async def undo_panel(callback : types.CallbackQuery):
    global mes3
    global all_state
    await mes2.delete()
    WHT = (callback.data.replace('report_', ''))
    ikb_all_wtf = InlineKeyboardMarkup(row_width=2).add(InlineKeyboardButton('Адреса', callback_data='send_adres'), (InlineKeyboardButton('Все', callback_data='send_all')), (InlineKeyboardButton('Назад', callback_data='undo_user3')))
    mes3 = await bot.send_message(callback.from_user.id, 'Что отпровить', reply_markup=ikb_all_wtf)
    if WHT == 'i':
        all_state = 1
    elif WHT == 'customer':
        all_state = 2

@dp.callback_query_handler(Text(startswith='send_'), state=status.prom_info)
async def undo_panel(callback : types.CallbackQuery):
    global all_state
    global ID_ADRES
    global mes1
    global mes4
    global WTF
    await mes3.delete()
    print(all_state)
    print((callback.data.replace('send_', '')))
    WTF = (callback.data.replace('send_', ''))
    if WTF == 'all':
        if all_state == 1:
            FILE = db.selekt_all_admin(id=ID_ADRES, map=MAP)
            for photo in FILE:
                await bot.send_photo(callback.from_user.id, photo[0], f'{photo[1]} Подъезд{photo[2]}')
            markup_adres = gen_markup_adres()
            mes1 = await bot.send_message(callback.from_user.id, f'Адреса промоутера\nВсего подъездов: {db.selekt_map_pad_admin(map=MAP)}', reply_markup=markup_adres)
        elif all_state == 2:
            ik_cust = ik_cust_markup()
            mes4 = await bot.send_message(callback.from_user.id, 'Выберити заказчика', reply_markup=ik_cust)
    elif WTF == 'adres':
        if all_state == 1:
            FILE = db.selekt_all_admin(id=ID_ADRES, map=MAP)
            for photo in FILE:
                await bot.send_message(callback.from_user.id,f'{photo[1]}')
            markup_adres = gen_markup_adres()
            mes1 = await bot.send_message(callback.from_user.id, f'Адреса промоутера\nВсего подъездов: {db.selekt_map_pad_admin(map=MAP)}', reply_markup=markup_adres)
        elif all_state == 2:
            ik_cust = ik_cust_markup()
            mes4 = await bot.send_message(callback.from_user.id, 'Выберити заказчика', reply_markup=ik_cust)

@dp.callback_query_handler(text='undo_user4', state=status.prom_info)
async def undo_panel(callback : types.CallbackQuery):
    global msg4
    await mes1.delete()
    map_panel = gen_markup_map()
    msg4 = await bot.send_message(callback.from_user.id, 'Выберити карту', reply_markup=map_panel)
    await status.prom_info.set()

@dp.callback_query_handler(text='undo_user3', state=status.prom_info)
async def undo_panel(callback : types.CallbackQuery):
    global mes2
    await mes3.delete()
    ikb_all = InlineKeyboardMarkup(row_width=2).add(InlineKeyboardButton('Себе', callback_data='report_i'), (InlineKeyboardButton('Заказчику', callback_data='report_customer')), (InlineKeyboardButton('Назад', callback_data='undo_user2')))
    mes2 = await bot.send_message(callback.from_user.id, 'Кому отправить отчет', reply_markup=ikb_all)

@dp.callback_query_handler(text='undo_user2', state=status.prom_info)
async def undo_panel(callback : types.CallbackQuery):
    global mes1
    await mes2.delete()
    markup_adres = gen_markup_adres()
    mes1 = await bot.send_message(callback.from_user.id, f'Адреса промоутера\nВсего подъездов: {db.selekt_map_pad_admin(map=MAP)}', reply_markup=markup_adres)
    await status.prom_info.set()

@dp.callback_query_handler(text='undo_user', state=status.prom_info)
async def undo_panel(callback : types.CallbackQuery):
    markup = gen_markup()
    global MES
    global mes
    await msg4.delete()
    MES = await bot.send_message(callback.from_user.id, '>>>>>>>>>>>>>>>>>>>', reply_markup=sand_kb)
    mes = await bot.send_message(callback.from_user.id, 'Список промоутеров', reply_markup=markup)
    await status.prom_info.set()

@dp.callback_query_handler(Text(startswith='map '), state=status.prom_info)
async def map(callback : types.CallbackQuery):
    global msg4
    global mes1
    global MAP
    MAP = (callback.data.replace('map ', ''))
    await msg4.delete()
    markup_adres = gen_markup_adres()
    mes1 = await bot.send_message(callback.from_user.id, f'Адреса промоутера\nВсего подъездов: {db.selekt_map_pad_admin(map=MAP)}', reply_markup=markup_adres)

@dp.callback_query_handler(Text(startswith='adres '), state=status.prom_info)
async def adres_(callback : types.CallbackQuery):
    global ADRES
    global mes1
    global msg4
    global Mm
    await mes1.delete()
    ADRES = (callback.data.replace('adres ', ''))
    FILE = db.selekt_photo_admin(adres=ADRES)
    for photo in FILE:
        await bot.send_photo(callback.from_user.id, photo[0], f'{ADRES}, Подъезд {photo[1]}')
    markup_adres = gen_markup_adres()
    Mm = 1
    mes1 = await bot.send_message(callback.from_user.id, f'Адреса промоутера\nВсего подъездов: {db.selekt_map_pad_admin(map=MAP)}', reply_markup=markup_adres)
    if Mm == 0:
        await msg4.delete()

#@dp.message_handlers(state=status.admin_start)
async def kb_config(message: types.Message):
    global mes
    global MES
    global bd_msg
    if message.text == 'Список промоутеров':
        await status.prom_info.set()
        markup = gen_markup()
        MES = await bot.send_message(message.from_user.id, '>>>>>>>>>>>>>>>>>>>', reply_markup=sand_kb)
        mes = await bot.send_message(message.from_user.id, 'Список промоутеров', reply_markup=markup)
    elif message.text == 'Добавить в BD':
        bd_msg = await bot.send_message(message.from_user.id, 'Выберити что вы хотите добавить в БД', reply_markup=panel_db_ikb)
        await status.db_panel.set()
    elif message.text == 'Выход':
        await message.answer("Выберити необходимую панель", reply_markup=admin_panel_start)
        await message.delete()
        await status.start_admin_panel.set()
        db.delete_all(message.from_user.id, photo=0)
    else:
        await bot.send_message(message.from_user.id, 'Таких комманд нет')

#@dp.callback_query_handler(text='Назад')
async def send_panel(callback : types.CallbackQuery):
    global bd_msg
    await status.admin_start.set()
    await bd_msg.delete()
    await bot.send_message(callback.from_user.id, 'Вы вернулиь в основное меню.', reply_markup=start_kb)

#@dp.message_handlers(text='Назад', state=status.prom_info))
async def send_panel_kb(message : types.Message):
    if message.text == 'Назад':
        await status.admin_start.set()
        await bot.send_message(message.from_user.id, 'Вы вернулиь в основное меню.', reply_markup=start_kb)
    else:
        xz = await bot.send_message(message.from_user.id, 'Неизвесная команда')
        await message.delete()

#@dp.callback_query_handler(text='Промоутер')
async def db_id_ikb(callback : types.CallbackQuery):
    await bot.send_message(callback.from_user.id, 'Введите ID пользователя', reply_markup=sand_kb)
    await status.db_id.set()

#@dp.callback_query_handler(text='Заказчик')
async def db_customer_ikb(callback: types.CallbackQuery):
    await bot.send_message(callback.from_user.id, 'Введите ID пользователя', reply_markup=sand_kb)
    await status.db_customer_id.set()

#@dp.callback_query_handler(text='Карта')
async def db_map_ikb(callback: types.CallbackQuery):
    await bot.send_message(callback.from_user.id, 'Введите номер карты', reply_markup=sand_kb)
    await status.db_map.set()

async def db_map(message: types.Message):
    global maps
    maps = message.text
    if message.text == 'Назад':
        await status.admin_start.set()
        await bot.send_message(message.from_user.id, 'Вы вернулиь в основное меню.', reply_markup=start_kb)
    elif db.selekt_map_admin(maps):
        await message.answer('Такая карта уже есть.')
    else:
        db.add_map_admin(map=maps)
        db.connection.commit()
        await message.answer("Карта добавлена в БД")
        await status.admin_start.set()
        await bot.send_message(message.from_user.id, 'Вы вернулиь в основное меню.', reply_markup=start_kb)

async def db_panel(message: types.message):
    if message.text == 'Промоутер':
        await bot.send_message(message.from_user.id, 'Введите ID пользователя', reply_markup=sand_kb)
        await status.db_id.set()
    elif message.text == 'Заказчик':
        await bot.send_message(message.from_user.id, 'Введите ID пользователя', reply_markup=sand_kb)
    elif message.text == 'Карта':
        await bot.send_message(message.from_user.id, 'Введите номер карты', reply_markup=sand_kb)
        await status.db_map.set()
    elif message.text == 'Назад':
        await status.admin_start.set()
        await bot.send_message(message.from_user.id, 'Вы вернулиь в основное меню.', reply_markup=start_kb)
    else:
        await message.answer("Выберити кнопку")

#@dp.register_message_handler(db_customer_id, state=status.db_customer_id)
async def db_customer_id(message: types.Message):
    global ID
    ID = message.text
    if message.text == 'Назад':
        await status.admin_start.set()
        await bot.send_message(message.from_user.id, 'Вы вернулиь в основное меню.', reply_markup=start_kb)
    elif db.selekt_id_admin(ID):
        await message.answer("Пользователь с таким ID уже существует!")
        await status.admin_start.set()
    else:
        await message.answer("ID добавлен.\n"
                             "Введите имя")
        await status.db_user.set()
        db.add_status_admin(ID)
        db.connection.cursor()

#@dp.register_message_handler(db_customer, state=status.db_customer)
async def db_customer(message: types.Message):
    USER = message.text
    await message.answer("Пользватель добавлен")
    db.add_user_admin(USER, ID)
    db.connection.cursor()
    await status.admin_start.set()
    await bot.send_message(message.from_user.id, 'Вы вернулиь в основное меню.', reply_markup=start_kb)

#@dp.register_message_handler(db_id, state=status.db_id)
async def db_id(message: types.Message):
    global ID
    ID = message.text
    if message.text == 'Назад':
        await status.admin_start.set()
        await bot.send_message(message.from_user.id, 'Вы вернулиь в основное меню.', reply_markup=start_kb)
    elif db.selekt_id_admin(ID):
        await message.answer("Пользователь с таким ID уже существует!")
        await status.admin_start.set()
    else:
        await message.answer("ID добавлен.\n"
                             "Введите имя")
        await status.db_user.set()
        db.add_id_admin(ID)
        db.connection.cursor()

#@dp.register_message_handler(db_user, state=status.db_user)
async def db_user(message: types.Message):
    USER = message.text
    await message.answer("Пользватель добавлен")
    db.add_user_admin(USER, ID)
    db.connection.cursor()
    await status.admin_start.set()
    await bot.send_message(message.from_user.id, 'Вы вернулиь в основное меню.', reply_markup=start_kb)



def register_handler_admin(dp: Dispatcher):
    dp.register_callback_query_handler(db_customer_ikb, text='Заказчик', state=status.db_panel)
    dp.register_callback_query_handler(send_panel, text='Назад', state=status.db_panel)
    dp.register_callback_query_handler(db_map_ikb, text='Карта', state=status.db_panel)
    dp.register_callback_query_handler(db_id_ikb, text='Промоутер', state=status.db_panel)
    dp.register_message_handler(send_panel_kb, state=status.prom_info)
    dp.register_message_handler(db_map, state=status.db_map)
    dp.register_message_handler(db_panel, state=status.db_panel)
    dp.register_message_handler(db_user, state=status.db_user)
    dp.register_message_handler(db_id, state=status.db_id)
    dp.register_message_handler(db_customer_id, state=status.db_customer_id)
    dp.register_message_handler(db_customer, state=status.db_customer)
    dp.register_message_handler(kb_config, state=status.admin_start)