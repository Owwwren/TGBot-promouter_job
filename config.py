from aiogram import Bot, Dispatcher
import TOKEN
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State

class status(StatesGroup):
    start_admin_panel = State()
    db_id = State()
    db_user = State()
    login = State()
    job = State()
    adres = State()
    photo = State()
    check = State()
    admin_start = State()
    prom_info = State()
    map = State()
    db_panel = State()
    db_map = State()
    db_customer_ikb = State()
    db_customer_id = State()
    db_customer = State()

bot = Bot(TOKEN.TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())