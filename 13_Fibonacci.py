#Asks the user how many Fibonacci numbers to create and then generates them
def askUser():
    userNumber = int(input("How many Fibonacci numbers do you want to generate? "))
    return userNumber

def createSequence(number):
    sequence = []

    i = 1

    if number == 1:
        sequence = [1]
    elif number == 2:
        sequence = [1,1]
    else:
        sequence = [1,1]
        while len(sequence) < number:
            sequence.append(sequence[i] + sequence[i-1])
            i += 1
    print(sequence)

createSequence(askUser())
