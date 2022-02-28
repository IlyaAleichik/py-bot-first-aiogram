from aiogram import types, Dispatcher
from create import dp, bot

# @dp.message_handler(commands =['start', 'help'])


async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Приветствуем вас!')
        await message.delete()
    except:
        await message.reply('Общение с ботом через ЛС, напишите ему:\nhttps://t.me/BingAvito_bot')

# @dp.message_handler(commands =['Рассмотр_заявок'])


async def avito_open_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'ВС-Чт с 9:00 до 20:00, Пт-сб с 10:00 до 23:00')

# @dp.message_handler(commands =['Страна_компании'])


async def avito_place_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'Российская Федерация')

    # @dp.message_handler(commands=['Услуги'])
    # async def avito_services_command(message : types.Message):
    #     for ret in cur.execute('SELECT * FROM services').Fetchall():
    #         await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nОписание: {ret[2]}\nЦена {ret[-1]}')


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(
        avito_open_command, commands=['Рассмотр_заявок'])
    dp.register_message_handler(
        avito_place_command, commands=['Страна_компании'])
