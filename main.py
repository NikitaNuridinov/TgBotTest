from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton, \
    ReplyKeyboardRemove
from aiogram.types.message import ContentType
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN=("6803275134:AAE4Mru7BwHbZDbGAG5u9d2JdpDbVbBZQDI")

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

KB1 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb1_1 = KeyboardButton("/help")
kb1_2 = KeyboardButton("/hello")
KB1.add(kb1_1).insert(kb1_2)


KB3 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb3_1 = KeyboardButton("/go")
kb3_2 = KeyboardButton("/search")
KB3.add(kb3_1).add(kb3_2)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text="""
<em><b>Дбро пожаловать на сервис по подбору автомобилей!</b>
Поиск можно производить по странам производителей, 
либо искать машины определенного бренда</em>
В случае если вы решите начать поиск сначала, 
вызовите команду /search
                          """,
                         parse_mode="html",
                         reply_markup=KB1)
    await message.delete()



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False)


@dp.message_handler(commands=['hello'])
async def send_welcome(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text=f""")
                           """,
                           parse_mode="html")
    await bot.send_message(chat_id=message.from_user.id,
                           text="""
Введите нужную вам страну и напишите её следующим сообщением!
Пишите без ошибок!
отправить /go!""",
                           parse_mode="html",
                           reply_markup=KB3)
    await message.delete()
