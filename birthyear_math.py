#Age sentence – Ask for a name and birth year, then print a sentence with their approximate age 
# using an f-string. (Sections 3, 5)
from datetime import date
print("Hey bitch!")
name = input("Who am I talking to? ")

def meaning_of_life(prompt):
    answer = input(prompt)
    if answer.strip() == "42":
        print("Don't forget to bring a towel.")
    else:
        print("Well, shit. Wasn't expecting that.")

raw_year = input("And what year were you born? ").strip()

if not raw_year.isdigit():
    #text, or anything that isn't plain digits, gets the "girl" path, then a dead end
    print("Girl. Stop messing around and enter the year in digits.")
    meaning_of_life("Since you're clearly not from around here, what's the meaning of life?")    
else: 
    #digits = normal flow
    birth_year = int(raw_year)
    age = date.today().year - birth_year
    if age < 0:
        meaning_of_life("So you're a time traveler? That year hasn't happened yet. If you're from the future, did they ever find the meaning of life? ")
    else:
        print(f"The math says you, {name}, are about {age} years old.")