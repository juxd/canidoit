import telegram
import config
import logging
from telegram.ext import Updater, CommandHandler
import LogicHandler, Parser, Error

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

bot = telegram.Bot(token=config.token)
updater = Updater(token=config.token)
dispatcher = updater.dispatcher
handleLimit = 3

def start(bot, update):
  bot.send_message(chat_id=update.message.chat_id, text='Hi! /help if you need more instructions')

def handleInput(bot, update):
  msgText = update.message.text.replace("/parsethis ", "")
  if (Error.error(msgText)):
     bot.send_message(chat_id=update.message.chat_id, text = "Error in Notation! Try Again!",
                    parse_mode="Markdown")
  else:
    predicateFn = LogicHandler.stringToFn(Parser.textToLogic(msgText))
    params = Parser.paramsGetter(msgText)
    res = LogicHandler.getTable(predicateFn, params)
    bot.send_message(chat_id=update.message.chat_id, text ="```"+res+"```",
                    parse_mode="Markdown")

def helpInput(bot, update):
  bot.send_message(chat_id=update.message.chat_id, text='Welcome to CS1231! I am James and can only process 4 variables - p, q, r and s. Watch out for your notation too! After typing in the command /parsethis, type the notation you want to convert!')

startHandler = CommandHandler('start', start)
inputHandler = CommandHandler('parsethis', handleInput)
helpHandler = CommandHandler('help', helpInput )
dispatcher.add_handler(helpHandler)
dispatcher.add_handler(startHandler)
dispatcher.add_handler(inputHandler)
updater.start_polling()
