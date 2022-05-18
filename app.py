from telegram.ext import Updater, MessageHandler, Filters

import re
import logging

logging.basicConfig(level=logging.INFO)

goose_launch = '''
ЗАПУСКАЕМ
░ГУСЯ░▄▀▀▀▄░РАБОТЯГИ░░
▄███▀░◐░░░▌░░░░░░░
░░░░▌░░░░░▐░░░░░░░
░░░░▐░░░░░▐░░░░░░░
░░░░▌░░░░░▐▄▄░░░░░
░░░░▌░░░░▄▀▒▒▀▀▀▀▄
░░░▐░░░░▐▒▒▒▒▒▒▒▒▀▀▄
░░░▐░░░░▐▄▒▒▒▒▒▒▒▒▒▒▀▄
░░░░▀▄░░░░▀▄▒▒▒▒▒▒▒▒▒▒▀▄
░░░░░░▀▄▄▄▄▄█▄▄▄▄▄▄▄▄▄▄▄▀▄
░░░░░░░░░░░▌▌░▌▌░░░░░
░░░░░░░░░░░▌▌░▌▌░░░░░
░░░░░░░░░▄▄▌▌▄▌▌░░░░░'''

goose_no = 'CAACAgIAAxkBAAMOYoUHXsCBOC0RhB2cxQiDdb43yx4AAkoAA1KJkSMpXmkxwunDNSQE'

def on_message(update, context):
    bot = context.bot
    chat_id = update.effective_chat.id
    source_message = update.message.text.lower()

    words = re.sub("[^\w]", " ", source_message).split()

    logging.debug(words)

    if "hi" in words:
        bot.send_message(chat_id=chat_id, text="Hello!")
    
    if "запускаем" in words:
        bot.send_message(chat_id=chat_id, text=goose_launch)

    if "no" in words or "нет" in words:
        bot.send_sticker(chat_id=chat_id, sticker=goose_no)

# def on_sticker(update, contaxt):
#     logging.info(update.message.sticker)

updater = Updater(
    token='5384271849:AAEPgkMhmIVfacmPmXY_3ffoOcbYz4o28ZE',
    use_context=True
)

dispatcher = updater.dispatcher

dispatcher.add_handler(MessageHandler(Filters.text, on_message))
# dispatcher.add_handler(MessageHandler(Filters.sticker, on_sticker))

logging.info("Started")

updater.start_polling()