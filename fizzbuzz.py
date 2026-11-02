#Print the numbers 1 to 30, but print Fizz for multiples of 3, 
#Buzz for multiples of 5, and FizzBuzz for multiples of both. (Section 8)
import time
print("Surprise, bitch, bet you thought you'd coded the last of me")
print("JK, let's do some more")

def fizzbuzz(limit=30, delay=0.5):
    for n in range(1, limit + 1):
        if n % 3 == 0 and n % 5 == 0:
            print("FizzBuzz")
        elif n % 3 == 0:
            print("Fizz")
            time.sleep(delay)
        elif n % 5 == 0:
            print("Buzz")
            time.sleep(delay)
        else:
            print(n)
            time.sleep(delay)

fizzbuzz()