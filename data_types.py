def data_type(value):
  
  #checks if value is string and returns its length
  if type(value) is str:
    return len(value)
  
  #checks if value is of type boolean and returns 
  #the value
  elif type(value) is bool:
    return value
    
  #checks if value is an Integer and returns statement 
  #if it is more, less or equal to 100
  elif type(value) is int:
    if (value < 100):
      return "less than 100"
    elif (value == 100):
      return "equal to 100"
    elif (value > 100):
      return "more than 100"
  
  #checks if value is of the type list and returns 
  #the third value or none if third value doesnt exist.
  elif type(value) is list:
    length = len(value)
    if (length >=3):
      return value[2]
    return None
      
  #checks if value is none and returns string "no value"
  elif value is None:
    return "no value"

