from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, KeyboardButton, InlineKeyboardButton
TOKEN = "6257155364:AAFgF6PiedehxeIhcZs7sx8JBtIqf03wJYg"

play_durack = KeyboardButton("Сыграть в дурака")

choice = ReplyKeyboardMarkup(resize_keyboard=True)

choice.add(play_durack)
