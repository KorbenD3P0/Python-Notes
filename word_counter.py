def count_words(text):
    word_count = {}
    words = text.split() 
    for word in words:
        word = word.lower().strip(" .,!?;/'\"()[]")  
        # Normalize the word by converting to lowercase and stripping punctuation
        if not word:
            continue
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count

while True:
    try:
        result = count_words(text=input('Enter some text: '))
        if result == {}:
            print("No words to count.")
        else:
            print(result.items())
            
            break
    except:
        print("An error occurred.")