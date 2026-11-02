def is_it_even(n):
    if n % 2 == 0 :
        print("That's an even number!")
    else:
        print("That's an odd number!")

try:
    n = int(input("Please enter a number to determine if it is even or odd: "))
    is_it_even(n)
except ValueError:
        print("That is not a valid number.")