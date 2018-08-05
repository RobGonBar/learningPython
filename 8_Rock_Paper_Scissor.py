#Two player rock paper scissor game

player1move = str(input("Player 1, what is your move?"))

player2move = str(input("Player 2, what is your move?"))

if (player1move == "scissors") and (player2move == "rock"):
    print("Player 2 wins")
elif player1move == "rock" and player2move == "paper":
    print("Player 2 wins")
elif player1move == "paper" and player2move == "scissors":
    print("Player 2 wins")
elif player1move == player2move:
    print("Tie")
else:
    print("Player 1 wins")
