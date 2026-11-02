door_unlock = False

def access_granted():
    global door_unlock 
    """'global' affects variables at the top of the file
	and triple quotes can initiate comments like a #"""
    door_unlock = True
    print("Congratulations! You have primo access.")

swiped = input("Please swipe your access card (User1 or User2): ")
card_valid = (swiped == "User1")
card_invalid = (swiped == "User2")
if card_valid:
    pin = input("Access Card Accepted! Please enter PIN (User1 or User2): ")
    pin_correct = (pin =="User1")
    if pin_correct:
        access_granted()
        print(door_unlock)
    else:
        print("Sorry, sucka! Access Denied!")
elif card_invalid:
    print("Away, beast! Invalid access card!")
else: 
    print("That's a credit card, you fool!")
