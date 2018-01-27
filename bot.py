import telegram
import config
from telegram.ext import Updater, CommandHandler

print (config.token)
bot = telegram.Bot(token=config.token)
updater = Updater(token=config.token)
dispatcher = updater.dispatcher
handleLimit = 3

def start(bot, update):
  bot.send_message(chat_id=update.message.chat_id, text='HI')

def 

startHandler = CommandHandler('start', start)
dispatcher.add_handler(startHandler)
updater.start_polling()
