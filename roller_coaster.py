MIN_HEIGHT= 48
MIN_AGE_ALONE = 12

def ride_check():
    answer = input("True or False: Do you have heart issues?: ").strip().lower()
    if answer == "true":
        print("Sorry buddy, maybe go get that bum ticker checked!")
        return
    if answer == "false":
        try:
            height = int(input("Enter your height in inches: "))
            if height < MIN_HEIGHT:
                print("You do not meet the height requirement.")
                return
            print("Meets height requirement.")
            age = int(input("Enter your age: "))
            if age < MIN_AGE_ALONE:
                print("You must ride with an adult.")
            else:
                print("You may ride on your own.")
        except ValueError:
            print("Whoops! That's not a valid entry.")
    else:
        print("Please answer True or False.")
            
ride_check()
