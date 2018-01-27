import telegram
import config
import logging
from telegram.ext import Updater, CommandHandler
import LogicHandler, Parser

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

bot = telegram.Bot(token=config.token)
updater = Updater(token=config.token)
dispatcher = updater.dispatcher
handleLimit = 3

def start(bot, update):
  bot.send_message(chat_id=update.message.chat_id, text='HI')

def handleInput(bot, update):
  predicateFn = LogicHandler.stringToFn(update.message.text)
  params = Parser.paramsGetter(update.message.text)
  res = LogicHandler.getTable(predicateFn, params)
  bot.send_message(chat_id=update.message.chat_id, text = "```" +res+"```")

startHandler = CommandHandler('start', start)
inputHandler = CommandHandler('parsethis', handleInput)
dispatcher.add_handler(startHandler)
dispatcher.add_handler(inputHandler)
updater.start_polling()
