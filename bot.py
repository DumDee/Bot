import re
from telegram import Update
from telegram.ext import Updater, CallbackContext, CommandHandler, Filters, MessageHandler, BaseFilter


def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("""
    Бот переводить данные слова с английского на русский и наоборот.
        'apple' : 'яблоко', 
         'bread' : 'хлеб' ,
         'hello' : 'привет',
         'goodbye' : 'пока', 
         'colour': 'цвет',
         'cloud': 'облако',
         'sun': 'солнце',
         'moon': 'луна',
         'night': 'ночь',
         'day': 'день'
    """)


def ru_apple(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('яблоко')

def ru_bread(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('хлеб')

def ru_hello(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('привет')

def ru_goodbye(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('пока')

def ru_colour(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('цвет')

def ru_cloud(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('облако')

def ru_sun(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('солнце')

def ru_moon(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('луна')

def ru_night(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('ночь')

def ru_day(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('день')



def en_apple(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('apple')

def en_bread(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('bread')

def en_hello(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('hello')

def en_goodbye(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('goodbye')

def en_colour(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('colour')

def en_cloud(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('cloud')

def en_sun(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('sun')

def en_moon(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('moon')

def en_night(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('night')

def en_day(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('day')




def not_supported(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Слово "{update.message.text}" не переводится.')


def get_greeting_filter(greeting: str) -> BaseFilter:
    return Filters.regex(re.compile(f'^{greeting}$', re.IGNORECASE)) & Filters.update.message


def main() -> None:
    updater = Updater("5740290006:AAF0XYnZ_D9XmeB53ppZTylsaMEwDJM4ceM")

    updater.dispatcher.add_handler(CommandHandler("help", help_command))
    updater.dispatcher.add_handler(MessageHandler(get_greeting_filter('яблоко'), en_apple))
    updater.dispatcher.add_handler(MessageHandler(get_greeting_filter('хлеб'), en_bread))
    updater.dispatcher.add_handler(MessageHandler(get_greeting_filter('привет'), en_hello))
    updater.dispatcher.add_handler(MessageHandler(get_greeting_filter('пока'), en_goodbye))
    updater.dispatcher.add_handler(MessageHandler(get_greeting_filter('облако'), en_cloud))
    updater.dispatcher.add_handler(MessageHandler(get_greeting_filter('солнце'), en_sun))
    updater.dispatcher.add_handler(MessageHandler(get_greeting_filter('луна'), en_moon))
    updater.dispatcher.add_handler(MessageHandler(get_greeting_filter('ночь'), en_night))
    updater.dispatcher.add_handler(MessageHandler(get_greeting_filter('день'), en_day))
    updater.dispatcher.add_handler(MessageHandler(get_greeting_filter('цвет'), en_colour))
    updater.dispatcher.add_handler(MessageHandler(get_greeting_filter('apple'), ru_apple))
    updater.dispatcher.add_handler(MessageHandler(get_greeting_filter('bread'), ru_bread))
    updater.dispatcher.add_handler(MessageHandler(get_greeting_filter('hello'), ru_hello))
    updater.dispatcher.add_handler(MessageHandler(get_greeting_filter('goodbye'), ru_goodbye))
    updater.dispatcher.add_handler(MessageHandler(get_greeting_filter('colour'), ru_colour))
    updater.dispatcher.add_handler(MessageHandler(get_greeting_filter('cloud'), ru_cloud))
    updater.dispatcher.add_handler(MessageHandler(get_greeting_filter('sun'), ru_sun))
    updater.dispatcher.add_handler(MessageHandler(get_greeting_filter('moon'), ru_moon))
    updater.dispatcher.add_handler(MessageHandler(get_greeting_filter('night'), ru_night))
    updater.dispatcher.add_handler(MessageHandler(get_greeting_filter('day'), ru_day))
    updater.dispatcher.add_handler(MessageHandler(Filters.update.message & Filters.text, not_supported))

    updater.start_polling()

    print('Started')

    updater.idle()


if __name__ == "__main__":
    main()