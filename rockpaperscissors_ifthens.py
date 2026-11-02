import random

NAMES = {1: "Rock", 2: "Paper", 3: "Scissors"}

def rps(player1, player2):
    player2 = int(input("1 for Rock, 2 for Paper, 3 for Scissors!: "))
    print(f"Computer: {NAMES[player1]} | You: {NAMES[player2]}")
    if player1 == player2:
        print("Draw!")
    elif player1 == 1 and player2 == 2:
        print(NAMES[player1], "loses to", NAMES[player2])
    elif player1 == 1 and player2 == 3:
        print(NAMES[player1], "wins against", NAMES[player2])
    elif player1 == 2 and player2 == 1:
        print(NAMES[player1], "wins against", NAMES[player2])
    elif player1 == 2 and player2 == 3:
        print(NAMES[player1], "loses to", NAMES[player2])
    elif player1 == 3 and player2 == 1:
        print(NAMES[player1], "loses to", NAMES[player2])
    elif player1 == 3 and player2 == 2:
        print(NAMES[player1], "wins against", NAMES[player2])
    else:
        print("That isn't valid input!")

rps(random.randint(1,3), random.randint(1,3))