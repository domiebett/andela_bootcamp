def fizz_buzz(n):
  if type(n) is not int:
    return "Not a number"

  output = ""

  #checks if n is divisible by three or by five
  #and set the the output to n
	if n%3!=0 and n%5!=0:
		output = n

  #checks if n is divisible by 3 and appends "Fizz"
  #to output
	if n%3==0:
    output = output + "Fizz"

  #checks if n is divisble by 5 and appends "Buzz"
  #to output
	if n%5==0:
    output = output + "Buzz"

  return output
