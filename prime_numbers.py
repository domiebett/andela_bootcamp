import math

def prime_numbers(n):
    number=0;
    divider=2;

    while divider!=n:
    
        prime_number=True;

        for i in range(2, int(math.sqrt(divider)+1)):
            if divider%i==0:
                prime_number=False;
                break;

        if (prime_number):
            number+=1
            print(divider)
        divider+=1