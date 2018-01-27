import PrintLogic
import Parser

def stringToFn(text):
  def resultFn(params):
    return eval(Parser.textToLogic(text))
  return resultFn

def getTable(predicateFn, params):
  table = PrintLogic.generateHead(params)
  table += PrintLogic.generateBody(predicateFn, len(params))
  return table

