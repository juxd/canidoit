import telegram
import config
import logging
from telegram.ext import Updater, MessageHandler, CommandHandler, Filters
import LogicHandler, Parser, Error

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

bot = telegram.Bot(token=config.token)
updater = Updater(token=config.token)
dispatcher = updater.dispatcher

msg_for_comparison = []

# def start(bot, update):
#   bot.send_message(chat_id=update.message.chat_id, text='Hi! /help if you need more instructions')

def parseInput(bot, update):
  msgText = update.message.text.replace("/parsethis ", "")
  if (Error.error(msgText)):
     bot.send_message(chat_id=update.message.chat_id, text = "Error in Notation! Try Again!",
                    parse_mode="Markdown")
  else:
    predicateFn = LogicHandler.stringToFn(Parser.textToLogic(msgText))
    params = Parser.paramsGetter(msgText)
    res = LogicHandler.getTable(predicateFn, params)

    bot.send_message(chat_id=update.message.chat_id, text = "```" + res + "```",

                    parse_mode="Markdown")

def helpInput(bot, update):
  bot.send_message(chat_id=update.message.chat_id, text='Welcome to CS1231! I am James and can only process 4 variables - p, q, r and s. Watch out for your notation too! After typing in the command /parsethis, type the notation you want to convert!')

def compareInput(bot, update):
  sentMsg = bot.send_message(chat_id=update.message.chat_id, text = "Reply me with the first predicate!")
  dispatcher.add_handler(collectHandler)
 
def collectMsg(bot, update):
  msg = update.message
  if (Error.error(msg.text)):
    bot.send_message(chat_id=msg.chat_id, text = "Error in Notation! Try Again!",
                    parse_mode="Markdown")
  else:
    msg_for_comparison.append(msg.text)
    if len(msg_for_comparison) >= 2:
      print(msg_for_comparison)
      compareMsgs(msg, msg_for_comparison)
    elif len(msg_for_comparison) == 1:
      bot.send_message(chat_id=msg.chat_id, text = "Good, now reply me one more!")

def compareMsgs(msg, msg_for_comparison):
  print(msg_for_comparison)
  dispatcher.remove_handler(collectHandler)
  text1 = msg_for_comparison[0]
  text2 = msg_for_comparison[1]
  params = Parser.paramsGetter(text1)
  pred1 = LogicHandler.stringToFn(Parser.textToLogic(text1))
  pred2 = LogicHandler.stringToFn(Parser.textToLogic(text2))
  result = ""

  if LogicHandler.sameParamAmt(text1, text2):
    result = LogicHandler.getDiff(pred1, pred2, params)
  else:
    result = "Different amount of arguments provided!"

  bot.send_message(chat_id=msg.chat_id, text = result, parse_mode="Markdown")
  msg_for_comparison=[]

# startHandler = CommandHandler('start', start)
inputHandler = CommandHandler('parsethis', parseInput)
helpHandler = CommandHandler('help', helpInput )
compareHandler = CommandHandler('compare', compareInput)
collectHandler = MessageHandler(Filters.reply, collectMsg)

dispatcher.add_handler(helpHandler)
# dispatcher.add_handler(startHandler)
dispatcher.add_handler(inputHandler)
dispatcher.add_handler(compareHandler)
updater.start_polling()
