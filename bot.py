from aiogram.utils import executor
from aiogram import Bot, types
from create import dp
from handlers import client, admin, other

client.register_handlers_client(dp)
other.register_handlers_other(dp)


async def on_startup():
    print('Бот вышел в онлайн')


@dp.message_handler()
async def echo_send(message: types.Message):
    await message.answer(message.text)
    await message.reply(message.text)
  # await bot.send_message(message.from_user.id, message.text)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
