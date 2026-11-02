import random

HANDS = {1: "Rock", 2: "Paper", 3: "Scissors"}
NAMES = {"r":1, "p":2, "s":3}

def rps(player1):
    choice = input("r for Rock, p for Paper, s for Scissors!: ")
    if choice not in NAMES:
        print("That isn't valid input!")
        return
    player2 = NAMES[choice]
    print(f"Computer: {HANDS[player1]} | You: {HANDS[player2]}")
    if player1 == player2:
        print("Draw!")
    elif player1 == 1 and player2 == 2:
        print(HANDS[player1], "loses to", HANDS[player2])
    elif player1 == 1 and player2 == 3:
        print(HANDS[player1], "wins against", HANDS[player2])
    elif player1 == 2 and player2 == 1:
        print(HANDS[player1], "wins against", HANDS[player2])
    elif player1 == 2 and player2 == 3:
        print(HANDS[player1], "loses to", HANDS[player2])
    elif player1 == 3 and player2 == 1:
        print(HANDS[player1], "loses to", HANDS[player2])
    elif player1 == 3 and player2 == 2:
        print(HANDS[player1], "wins against", HANDS[player2])
    else:
        print("That isn't valid input!")

rps(random.randint(1,3))