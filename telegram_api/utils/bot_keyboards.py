from telebot import types


main_menu_keyboard = types.InlineKeyboardMarkup()
main_menu_keyboard.add(types.InlineKeyboardButton('Top 100 movies', callback_data='movies'))
main_menu_keyboard.add(types.InlineKeyboardButton('Top 100 series', callback_data='series'))
main_menu_keyboard.add(types.InlineKeyboardButton('Movie by rang', callback_data='movie_by_id'))
main_menu_keyboard.add(types.InlineKeyboardButton('Series by rang', callback_data='series_by_id'))

next_button = types.InlineKeyboardButton('next', callback_data='next')
back_button = types.InlineKeyboardButton('back to the menu', callback_data='back')
previous_button = types.InlineKeyboardButton('previous', callback_data='previous')

default_navigation_keyboard = types.InlineKeyboardMarkup()
default_navigation_keyboard.add(next_button)
default_navigation_keyboard.add(previous_button)
default_navigation_keyboard.add(back_button)

navigation_keyboard_without_previous = types.InlineKeyboardMarkup()
navigation_keyboard_without_previous.add(next_button)
navigation_keyboard_without_previous.add(back_button)

navigation_keyboard_without_next = types.InlineKeyboardMarkup()
navigation_keyboard_without_next.add(previous_button)
navigation_keyboard_without_next.add(back_button)
