import os

import telebot
from telebot import types
from telegram.constants import ParseMode
from dotenv import load_dotenv

from services import *
from logger import get_logger

logger = get_logger(__name__)

load_dotenv()

BOT_TOKEN = os.environ.get('BOT_TOKEN')

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    coins = types.KeyboardButton('coins')
    news = types.KeyboardButton('news')
    exchanges = types.KeyboardButton('exchanges')
    about = types.KeyboardButton('about')

    markup.add(coins, news, exchanges, about)
    bot.send_message(message.chat.id, "How can I help you?", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def bot_handler(message):
    try:
        if message.chat.type == 'private':
            if message.text == 'coins':
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                coin_by_name = types.KeyboardButton('get coin')
                rising_coin = types.KeyboardButton('rising coin')
                decreasing_coin = types.KeyboardButton('decreasing coin')
                back = types.KeyboardButton('back')
                markup.add(coin_by_name, rising_coin, decreasing_coin, back)

                bot.send_message(message.chat.id, "Coins", reply_markup=markup)

            elif message.text == 'news':
                bot.send_message(message.chat.id, "News")
                news = get_news()
                for new in news:
                    bot.send_message(message.chat.id, text=f'*{new}*', parse_mode=ParseMode.MARKDOWN)

            elif message.text == 'about':
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                author = types.KeyboardButton('author')
                bot_info = types.KeyboardButton('bot')
                back = types.KeyboardButton('back')
                markup.add(author, bot_info, back)
                bot.send_message(message.chat.id, "About", reply_markup=markup)

            elif message.text == 'exchanges':
                spot_exchanges = crypto_exchanges()
                bot.send_message(message.chat.id, "Top Cryptocurrency Spot Exchanges")
                for exchange in spot_exchanges:
                    bot.send_message(message.chat.id, exchange)

            elif message.text == 'back':
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                coins = types.KeyboardButton('coins')
                news = types.KeyboardButton('news')
                exchanges = types.KeyboardButton('exchanges')
                about = types.KeyboardButton('about')
                markup.add(coins, news, exchanges, about)
                bot.send_message(message.chat.id, "Menu", reply_markup=markup)

            elif message.text == 'get coin':
                msg = bot.send_message(message.chat.id, "Write the name of coin")
                bot.register_next_step_handler(msg, send_coin_info)

            elif message.text == 'rising coin':
                bot.send_message(message.chat.id, "5 coins with the largest increase in 24 hours")
                pointer, coins = rising_coins()
                if pointer:
                    bot.send_message(message.chat.id, f'<pre>{coins}</pre>', parse_mode=ParseMode.HTML)
                else:
                    bot.send_message(message.chat.id, "Sorry, smth went wrong")

            elif message.text == 'decreasing coin':
                bot.send_message(message.chat.id, "5 coins with the largest decrease in 24 hours")
                pointer, coins = decreasing_coins()
                if pointer:
                    bot.send_message(message.chat.id, f'<pre>{coins}</pre>', parse_mode=ParseMode.HTML)
                else:
                    bot.send_message(message.chat.id, "Sorry, smth went wrong")

            elif message.text == 'author':
                author = about_author()
                bot.send_message(message.chat.id, author)

            elif message.text == 'bot':
                bot.send_photo(message.chat.id, photo=open('telegram_bot/images/logo_back.png', 'rb'))
                bot_info = about_bot()
                bot.send_message(message.chat.id, bot_info)

            else:
                bot.send_message(message.chat.id, "Please, select a command in the menu")
    except Exception as err:
        logger.error(f'[ERROR] {err}')


@bot.message_handler(content_types=['text'])
def send_coin_info(message):
    pointer, coin = get_coin_by_name(message.text)
    if pointer:
        bot.send_message(message.chat.id, f'<pre>{coin}</pre>', parse_mode=ParseMode.HTML)
    else:
        bot.send_message(message.chat.id, "Name of coin is incorrect or there is no info about this coin")


@bot.message_handler(commands=['coin'])
def get_coin(message):
    bot.send_message(message.chat.id, "What coin do you want to get information about? (write name)")
    bot.send_message(message.chat.id, "What coin do you want to get information about? (write name)")


bot.infinity_polling()
