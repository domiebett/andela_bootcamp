def data_type(value):
  
  if type(value) is str:
    return len(value)
    
  elif type(value) is bool:
    return value
    
  elif type(value) is int:
    if (value < 100):
      return "less than 100"
    elif (value == 100):
      return "equal to 100"
    elif (value > 100):
      return "more than 100"
      
  elif type(value) is list:
    length = len(value)
    if (length >=3):
      return value[2]
    return None
      
  elif value is None:
    return "no value"
