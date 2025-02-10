import telebot
from settings import site_settings
from site_api.core import site_api_handler
from telegram_api.utils.bot_handler import BotHandler


tg_bot = telebot.TeleBot(site_settings.tg_token.get_secret_value())
bot_handler = BotHandler(tg_bot,
                         series_by_id_function=site_api_handler.get_series_by_id,
                         movie_by_id_function=site_api_handler.get_movie_by_id)
