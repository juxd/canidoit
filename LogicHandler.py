def textToLogic(text):
  print(text)
  text = text.replace("p", "params[0]")
  text = text.replace("q", "params[1]")
  text = text.replace("r", "params[2]")
  text = text.replace("s", "params[3]")
  text = text.replace("~", " not ")
  text = text.replace("^", " and ")
  text = text.replace("v", " or ")
  print(text)
  return text;

def StringToFn(text):
  def ResultFn(p, q):
    return eval(text)
  return ResultFn


