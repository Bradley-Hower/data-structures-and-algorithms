def multi_bracket_validation(input):
  parenthesis = None
  curly_bracket = None
  bracket = None


  for i in input:
    if i == "(":
      parenthesis = "left"
    elif i == ")":
      if parenthesis == "left":
        parenthesis = "right"
      else:
        parenthesis = "Fault"
    elif i == "{":
      curly_bracket = "left"
    elif i == "}":
      if curly_bracket == "left":
        curly_bracket = "right"
      else:
        curly_bracket = "Fault"
    elif i == "[":
      bracket = "left"
    elif i == "]":
      if bracket == "left":
        bracket = "right"
      else:
        bracket = "Fault"

  if parenthesis == "left" or curly_bracket == "left" or bracket == "left":
    return False
  elif parenthesis == "Fault" or curly_bracket == "Fault" or bracket == "Fault":
    return False
  else:
    return True

