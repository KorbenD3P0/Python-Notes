#4.	Vowel counter – Count the vowels in a string typed by the user. (Sections 5, 8)
print("Sup Bitch, we're counting vowels now")
text = input("Write whatever you want here!: ")

v = 0
for letter in text.lower():
    if letter in "aeiou":
        v += 1

print(f"There were {v} vowels in that string.")