import random

NAMES = {1: "Rock", 2: "Paper", 3:"Scissors"}
WINS = {1:3, 3:2, 2:1}

def rps(chosen):
    player2 = int(input("1 for Rock, 2 for Paper, 3 for Scissors!: "))
    print(f"Computer: {NAMES[chosen]} | You: {NAMES[player2]}")
    if chosen == player2:
        print("Draw, Sucka!")
    elif WINS[chosen] == player2:
        print(f"Computer wins with {NAMES[chosen]}!")
    else:
        print(f"You Win with {NAMES[player2]}!")

rps(random.randint(1,3))