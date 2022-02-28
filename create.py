from aiogram import Bot
from aiogram.dispatcher import Dispatcher

import logging

bot = Bot(token="1002839138:AAFpdrsBgQAPRUykvzF-s7-5ZShjrr1u2F4")
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)
