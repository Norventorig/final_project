from telebot import TeleBot
from telegram_api.utils.IMDB_data_handler import imdb_data_handler
from telegram_api.utils.bot_keyboards import main_menu_keyboard, \
                                                default_navigation_keyboard, \
                                                navigation_keyboard_without_previous, \
                                                navigation_keyboard_without_next


class BotHandler:
    def __init__(self, bot: TeleBot, movie_by_id_function, series_by_id_function, crud, db, user_model, history_model):
        self.bot = bot

        self.navigation_keyboard_without_next = navigation_keyboard_without_next
        self.main_menu_keyboard = main_menu_keyboard
        self.default_navigation_keyboard = default_navigation_keyboard
        self.navigation_keyboard_without_previous = navigation_keyboard_without_previous

        self.user_waiting_for_input = {}
        self.imdb_data_handler = imdb_data_handler

        self.movie_by_id_function = movie_by_id_function
        self.series_by_id_function = series_by_id_function
        self.crud = crud
        self.db = db
        self.user_model = user_model
        self.history_model = history_model

        self.register_handlers()

    def make_record_db(self, message, query_body):
        with self.db:
            user = self.crud.retrieve(model=self.user_model, conditions=self.user_model.chat_id == message.chat.id)

            if not user:
                self.crud.create(model=self.user_model,
                                 data=[{'chat_id': message.chat.id,
                                        'user_name': message.from_user.username,
                                        'name': message.from_user.first_name,
                                        'last_name': message.from_user.last_name}])

                user = self.crud.retrieve(model=self.user_model,
                                          conditions=self.user_model.chat_id == message.chat.id)

            self.crud.create(model=self.history_model,
                             data=[{'query_body': query_body, 'author': user[0]}])

    def register_handlers(self):
        self.bot.register_message_handler(self.start, commands=['start'])

        self.bot.register_message_handler(self.history, commands=['history'])

        self.bot.register_message_handler(self.antispam,
                                          func=lambda message: message.chat.id not in self.user_waiting_for_input,
                                          content_types=['text', 'photo', 'sticker', 'video', 'audio'])

        self.bot.register_message_handler(self.process_user_input,
                                          func=lambda message: message.chat.id in self.user_waiting_for_input)

        self.bot.register_callback_query_handler(self.ask_for_media_id,
                                                 func=lambda call: call.data in ('series_by_id', 'movie_by_id'))

        self.bot.register_callback_query_handler(self.user_handler,
                                                 func=lambda call: call.data in
                                                                   ('movies', 'series', 'next', 'previous', 'back'))

        self.bot.register_message_handler(self.send_data)

    def start(self, message):
        self.bot.send_message(chat_id=message.chat.id,
                              text='Я тг бот IMDB! '
                                 'Мои задача - ознакомить вас с лучшими фильмами и сериалами по мнению IMDB',
                              reply_markup=self.main_menu_keyboard)

    def history(self, message):
        with self.db:
            histories = self.crud.retrieve(self.history_model, conditions=self.history_model.author == message.chat.id)
            histories = '\n'.join([f'{i.query_body} -- {i.date}' for i in histories])

            self.bot.send_message(chat_id=message.chat.id,
                                  text=histories)

        self.bot.send_message(chat_id=message.chat.id,
                              text='Я тг бот IMDB! '
                                 'Мои задача - ознакомить вас с лучшими фильмами и сериалами по мнению IMDB',
                              reply_markup=self.main_menu_keyboard)

    def antispam(self, message):
        self.bot.delete_message(message.chat.id, message.message_id)

    def send_data(self, call):
        movie_data = self.imdb_data_handler.processing_func(self.imdb_data_handler.media_id)

        if movie_data.status_code == 200:
            movie_data = movie_data.json()

            new_text = f'{movie_data["thumbnail"]}\n' \
                    f'TITLE: {movie_data["title"]}\n' \
                    f'RELEASE YEAR: {movie_data["year"]}\n' \
                    f'RATING: {movie_data["rating"]}\n' \
                    f'DESCRIPTION: {movie_data["description"]}\n' \
                    f'GENRE: {movie_data["genre"]}\n' \
                    f'TRAILER: {movie_data["trailer"]}'

            self.bot.edit_message_text(text=new_text,
                                       chat_id=call.message.chat.id,
                                       message_id=call.message.id,
                                       reply_markup=self.default_navigation_keyboard
                                       if 100 > self.imdb_data_handler.media_id > 1 else
                                       (self.navigation_keyboard_without_previous
                                        if self.imdb_data_handler.media_id == 1 else
                                        self.navigation_keyboard_without_next))

            self.make_record_db(message=call.message, query_body=movie_data)

        else:
            self.bot.answer_callback_query(call.id, text='Что то пошло не так')
            self.make_record_db(message=call.message, query_body='Error')

    def ask_for_media_id(self, call):
        self.bot.edit_message_text(text='Отправьте в чат номер произведения о котором вы хотите получить информацию!',
                                   chat_id=call.message.chat.id,
                                   message_id=call.message.id)

        self.user_waiting_for_input[call.message.chat.id] = call

    def process_user_input(self, message):
        call = self.user_waiting_for_input[message.chat.id]
        self.bot.delete_message(chat_id=message.chat.id,
                                message_id=message.message_id)

        if call.data == 'movie_by_id':
            self.imdb_data_handler.media_id = int(message.text)
            self.imdb_data_handler.processing_func = self.movie_by_id_function

        else:
            self.imdb_data_handler.media_id = int(message.text)
            self.imdb_data_handler.processing_func = self.series_by_id_function

        del self.user_waiting_for_input[message.from_user.id]

        call.message.text = call.data + message.text

        self.send_data(call=call)

    def user_handler(self, call):
        if call.data == 'back':
            self.bot.edit_message_text(chat_id=call.message.chat.id,
                                       text='Я тг бот IMDB! Мои задача - '
                                            'ознакомить вас с лучшими фильмами и сериалами по мнению IMDB',
                                       reply_markup=self.main_menu_keyboard, message_id=call.message.id)

        else:
            if call.data == 'movies':
                self.imdb_data_handler.media_id = 1
                self.imdb_data_handler.processing_func = self.movie_by_id_function

            elif call.data == 'series':
                self.imdb_data_handler.media_id = 1
                self.imdb_data_handler.processing_func = self.series_by_id_function

            elif call.data == 'next':
                self.imdb_data_handler.media_id += 1

            elif call.data == 'previous':
                self.imdb_data_handler.media_id -= 1

            self.send_data(call=call)

        call.message.text = call.data
