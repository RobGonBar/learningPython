# Function to check if number is prime

def intConvert(userInput):
    return int(input(userInput))

def primeCheck(number):
    if  number == 1:
        prime = False
    elif number == 2:
        prime = True
    #All other primes
    else:
        prime = True
        for x in range (2, number - 1):
            if number % x == 0:
                prime = False
            break
    return prime


def printAnswer(number):
    prime = primeCheck(number)
    if prime:
        descriptor = " is "
    else:
        descriptor = " is not "
    print("The number " + descriptor + "prime")

# Neverending while loop which asks user for a number
# This passes the user input into the intConvert, which passes the answer into printAnswer, which calls the
# primeCheck Function. Once it finishes running through the prime check function, printAnswer shows the result
while 1 == 1:
    printAnswer(intConvert("Enter a number to check. Ctl-C to exit."))
