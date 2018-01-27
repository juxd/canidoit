import PrintLogic
import Parser

def stringToFn(text):
  def resultFn(params):
    return eval(text)
  return resultFn

def getTable(predicateFn, params):
  table = PrintLogic.generateHead(params)
  table += PrintLogic.generateBody(predicateFn, len(params))
  return table

def sameParamAmt(text1, text2):
  if len(Parser.paramsGetter(text1)) == len(Parser.paramsGetter(text2)):
    return True
  else:
    return False

def getDiff(predicate1, predicate2, params):
  return PrintLogic.compareBody(predicate1, predicate2, len(params))

