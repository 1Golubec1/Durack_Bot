from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, KeyboardButton, InlineKeyboardButton
from config import *
import random
import json

bl = []
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

def gen_deck():
    f = open("cards.txt", 'r', encoding='UTF-8').read().split("\n")
    for _ in range(10):
        random.shuffle(f)
    return f



def save_user(user_id):
    f = open("users.json", "w", encoding="UTF-8")
    f.write(json.dumps(user_id, ensure_ascii=False))
    f.close()

def get_user():
    f = open("users.json", "r", encoding="UTF-8")
    ff = f.read()
    users = {}
    if ff != "":
        f.seek(0)
        users = json.load(f)
        f.close()
    return users



@dp.message_handler(commands=['start'])
async def start_menu(message: types.Message):
    user_id = str(message.from_user.id)
    users = get_user()
    user_add = {}
    user_add[user_id] = {"DECK_CARDS":[], "STATE": None, "DECK_PLAYER": [], "BOT_DECK":[]}
    users.update(user_add)
    save_user(users)
    await message.answer("Все работает", reply_markup=choice)

@dp.message_handler()
async def start_menu(message: types.Message):
    user_id = str(message.from_user.id)
    users = get_user()
    if message.text == "Сыграть в дурака":
        users[user_id]["STATE"] = "DURACK"
        users[user_id]["DECK_CARDS"] = gen_deck()
        save_user(users)
    if users[user_id]["STATE"] == "DURACK":
        coloda = ReplyKeyboardMarkup()
        for i in range(1, 13, 2):
            users[user_id]["DECK_PLAYER"].append(users[user_id]["DECK_CARDS"][i])
            knopka = KeyboardButton(users[user_id]["DECK_CARDS"][i])
            users[user_id]["BOT_DECK"].append(users[user_id]["DECK_CARDS"][i-1])
            coloda.add(knopka)
            users[user_id]["DECK_CARDS"].pop(i)
            save_user(users)
        await message.answer("Тест колоды", reply_markup=coloda)
        print(users[user_id]["BOT_DECK"], "\n", users[user_id]["DECK_PLAYER"])









    # await bot.send_sticker("1084337847", message.sticker)
    # await bot.send_sticker("899364641", message.sticker)
    # if user_id == "1084337847":
    #     await bot.send_message("899364641", message.text)
    #
    #     await bot.send_sticker("1084337847", message.sticker)
    #     print(1)
    # if user_id == "899364641":
    #     await bot.send_message("1084337847", message.text)
    #     if message.sticker != None:
    #         await  bot.send_sticker("899364641", str(message.sticker))


executor.start_polling(dp)