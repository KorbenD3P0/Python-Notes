import random

die1 = random.randint(1,6)
die2 = random.randint(1,6)

if die1 == 1 and die2 ==1:
    print("Snake eyes!")
elif die1 and die2 == 7:
    print("7! Lucky sumbitch!")
else:
    print("You rolled: ", die1, die2)