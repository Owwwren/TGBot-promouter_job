from aiogram.utils import executor
from config import dp

async def on_startup(_):
    print('БОТ запущен!')

from Handlers import user, admin, register

register.register_handler_register(dp)
admin.register_handler_admin(dp)
user.register_handler_user(dp)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)