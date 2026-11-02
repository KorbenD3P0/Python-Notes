#1.	Temperature converter – Ask for a Fahrenheit temperature and print Celsius, 
# using C = (F − 32) × 5/9, rounded to 1 decimal. (Sections 2, 4, 5)

print("Hey, bitch!")
while True:
    try:
        F = float(input("Time to enter some info. What's the temp out in farenheit? "))
    except ValueError:
        print("Error, try entering numbers instead!")
    else:
        C = (F - 32) * 5/9
        print(f"Did you know it's {C:.1f} degrees out?\nThat damn metric system, I tell you!")
        break