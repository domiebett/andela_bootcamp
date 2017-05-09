def fizz_buzz(n):
	if type(n) is not int:
		return "Not a number"
  	string = ""
  	if n%3!=0 and n%5!=0:
  		string = n
  	if n%3==0:
		string = string + "Fizz"
	if n%5==0:
  		string = string + "Buzz"

  	return string

