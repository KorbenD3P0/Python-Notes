while True: 
    #this is a loop
    #it only lets the user continue once True, 
    #so a ValueError would cause a repeat prompt
    try:
        price = float(input("Please enter the total of your order: ").replace("$", ""))
        break
    except ValueError:
        #There are more error types that allow programmers
        #to stack several except blocks, one per error type
        print("Please enter a valid number like 49.99, not letters.")
if price >= 50:
    print ("You qualify for free shipping!")
elif price <0:
    print("Oh, so we owe YOU money? Ain't that about a...")
else:
    print("Shipping fee required.")
