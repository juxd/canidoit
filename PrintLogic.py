# this function prints a row given the booleans in an array
def printLine(params, predicateFn): 
  result = "| "
  def singleChar(boolean):
    if boolean:
      return "T"
    else:
      return "F"
      
  for i in params:
    result += singleChar(i) + " | "
  result += "  " + singleChar(predicateFn(params)) + "    |\n"
  return result

# this function takes in an array of parameters and prints header for the table
def generateHead(params):
  result = "| "
  for i in params:
    result += i + " | "
  result+= "result | \n"
  result+= "=======================\n"
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
