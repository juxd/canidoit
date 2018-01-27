
# text should be a function that takes in an array of booleans and returns a boolean
def textToLogic(text):
  text = text.lower()
  textAsChars = list(text)
  
  def replaceChar(char1, char2):
    for i in range(0, len(textAsChars)):
      if textAsChars[i] == char1:
        textAsChars[i] = char2
  charCount = 0;
  for i in range(0, 4):
    if any(ord(j) == 112 + i for j in text):
      replaceChar(chr(112 + i), 'params[' + str(charCount) + ']')
      charCount += 1
  replaceChar('~', ' not ')
  replaceChar('^', ' and ')
  replaceChar('v', ' or  ')
  result = ''.join(textAsChars)
  return result

# takes in a predicate in text and returns an array of parameters/variables in it
def paramsGetter(text):
  params = []
  for i in range(0, 4):
    if any(ord(c) == 112 + i for c in text):
      params.append(chr(112 + i))
  return params

