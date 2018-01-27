# this function prints a row given the booleans in an array
def printLine(params, predicateFn): 
  result = " "
  def singleChar(boolean):
    if boolean:
      return "T"
    else:
      return "F"
      
  for i in params:
    result += singleChar(i) + " | "
  result += "  " + singleChar(predicateFn(params)) + "    \n"
  return result

# this function takes in an array of parameters and prints header for the table
def generateHead(params):
  result = " "
  for i in params:
    result += i + " | "
  result+= "result \n"
  for i in params:
    result += "---|"
  result+= "---------\n"
  return result

# takes in a function that takes in a array, and an integer corresponding to the number of entries in the array
def generateBody(predicateFn, noOfParams):
  result = ""
  params = [True] * noOfParams

  def makeRows(countLeft):
    result = ""
    
    if countLeft == 1:
      params[noOfParams - 1] = True
      result += printLine(params, predicateFn)
      params[noOfParams - 1] = False
      result += printLine(params, predicateFn)
      return result
    else:
      params[noOfParams - countLeft] = True
      result += makeRows(countLeft - 1)
      params[noOfParams - countLeft] = False
      result += makeRows(countLeft - 1)
      return result
   
  result += makeRows(noOfParams)
  return result

def compareBody(predicateFn1, predicateFn2, noOfParams):
  params = [True] * noOfParams
  badParams = []
  result = ""
  def getBadParams(countLeft):
    if countLeft == 0:
      if predicateFn1(params) != predicateFn2(params):
        badParams.append(params.copy())
    else:
      params[noOfParams - countLeft] = True
      getBadParams(countLeft - 1)
      params[noOfParams - countLeft] = False
      getBadParams(countLeft - 1)

  getBadParams(noOfParams)
  if len(badParams) == 0:
    result += "They are logically equivalent!"
    return result
  else:
    result += str(len(badParams)) + " mismatches have been found: \n ```"

    for p in badParams:
      print(p)
      result += "For Predicate 1,    "
      result += printLine(p, predicateFn1)
      result += "But for Predicate 2,"
      result += printLine(p, predicateFn2)
      result += "\n"
    result += "```"
    return result
