import random

def guessing_game():
    answer = random.randint(1,100)
    while True: 
        try:
            entry = int(input("Guess a number 1-100!: "))
        except TypeError: 
            print("Type Error, sucka!")
            continue
        except ValueError:
            print("Value Error, sucka!")
            continue

        if entry < 1 or entry > 100:
            print("Stay between 1 and 100, sucka!")
        elif entry < answer:
            print("Higher!")
        elif entry > answer:
            print("Lower!")
        else:
            print("Lucky dog, you got a match!")
            break

guessing_game()