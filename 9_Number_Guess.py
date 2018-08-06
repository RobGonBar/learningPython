#Number guessing game
import random
#test
randomNumber = random.randint(1,9)
userGuess = 0
count = 0

while(userGuess != "Exit" and userGuess != randomNumber):
    try:
        userGuess = input("Guess a number between 1 and 9 ")
        if(userGuess == "exit"):
            break
        # Transforms the userGuess into an integer userNumber
        userNumber = int(userGuess)
        #Compares the guess to the randomNumber and gives the user a clue
        if(userNumber > randomNumber):
            print("Sorry, thats too high")
            count += 1
        elif(userNumber < randomNumber):
            print("Sorry, thats too low")
            count += 1
        elif(userNumber is None):
            print("Sorry, you need to enter a number")
        else:
            count = str(count)
            userNumber = str(userNumber)
            print("Thats right! It took you " + count + " tries to guess the number " + userNumber)
            break
    #Exception in case the user does not enter anything
    except(SyntaxError, ValueError):
        print("You didn't enter a number")
