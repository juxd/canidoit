def textToLogic(text):
  print(text)
  text = text.replace("p", "params\[p\]")
  text = text.replace("q", "params\[q\]")
  text = text.replace("~", " not ")
  text = text.replace("^", " and ")
  text = text.replace("v", " or ")
  print(text)
  return text;

def StringToFn(text):
  def ResultFn(params):
    return eval(text)
  return ResultFn


