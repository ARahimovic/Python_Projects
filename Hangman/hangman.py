import requests
import random

#we need to choose a random word
random_words_url = "https://www.mit.edu/~ecprice/wordlist.10000"
response = requests.get(random_words_url)
words = response.content.splitlines()

random_word = random.choice(words).decode("utf-8")

print(random_word)

word_length = len(random_word)

placeHolder = "_ "*word_length
print(placeHolder)

numGuesses = 6
tries = 0
while  tries < numGuesses:
    userGuess = input("enter word")
    userGuess = userGuess.strip().lower()
    
    if len(userGuess) == 1:
        if userGuess in random_word:
            print("guess correct letter")
        else:
            print("letter not in word")
    
    elif len(userGuess) == word_length:
        if userGuess == word_length :
            print("you guess correctly")
            break
        else:
             print("wrong answer")
    else:
        print("invalid guess")

    tries += 1

    