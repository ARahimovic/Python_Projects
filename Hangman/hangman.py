import requests
import random
import keyboard
import time
'''
Game rules
player has limited number of guesses
the player guess one letter at a time 
if letter is correct, all instance of that letter are revealed
for each wrong guess , a part of hangman is drawn

game is lost if player use all incorrect guess
'''
def generateRandomWord():
    #we need to choose a random word
    random_words_url = "https://www.mit.edu/~ecprice/wordlist.10000"
    response = requests.get(random_words_url)
    words = response.content.splitlines()
    random_word = random.choice(words).decode("utf-8")

    return random_word


def letterCount(text):

    letter_count = {}
    for c in text:
        letter_count[c] = letter_count.get(c, 0) + 1
    
    return letter_count


def takeUserInput():
    while True:
        letter = input("Guess a letter : ")
        if len(letter) == 1 and letter.isalpha():
            break
        else:
            print("Invalid format, you need to input a letter")
    
    return letter

def exit_or_no():
    print("Press :\n1.Enter to replay\t\t\t2.Esc to escape")
    while True:
        if keyboard.is_pressed('esc'):
            print("exiting game ....")
            return True
        elif keyboard.is_pressed('enter'):
            return False
        time.sleep(0.1)

if __name__ == "__main__":

    hangman_stages = [
   r"""
    -----
    |   |
        |
        |
        |
        |
   -----|
    """,
    r"""
    -----
    |   |
    0   |
        |
        |
        |
   -----|
    """,
    r"""
    -----
    |   |
    0   |
    |   |
        |
        |
   -----|
    """,
    r"""
    -----
    |   |
    0   |
    |\  |
        |
        |
   -----|
    """,
    r"""
    -----
    |   |
    0   |
   /|\  |
        |
        |
   -----|
    """,
    r"""
    -----
    |   |
    0   |
   /|\  |
     \  |
        |
   -----|
    """,
    r"""
    -----
    |   |
    0   |
   /|\  |
   / \  |
        |
   -----|
    """
    ]
    
    while True :
        random_word = generateRandomWord().lower()
        letter_count = letterCount(random_word)
        place_holder = "_ "* len(random_word)
        hasWon = False
        allowed_guesses = 6
        while allowed_guesses > 0 :
            print(f"Word to guess : {place_holder}\n" + hangman_stages[6-allowed_guesses].rjust(50)) 
            letter = takeUserInput().lower()
            if letter in random_word:
                for i,c in enumerate(random_word):
                    if c == letter:
                        place_holder = place_holder[:i*2] + c + place_holder[(i*2)+1:]

                if place_holder.strip().replace(" ","") == random_word :
                    hasWon = True
                    break
            else :
                allowed_guesses -= 1
                print(f"Wrong Guess, {allowed_guesses} guess left")
                
        if hasWon:
            print(f"You Won!\nYou Guessed the Correct word : {random_word}")
        else :
            print(hangman_stages[-1])
            print(f"You lost\nCorrect word was : {random_word}")

        
        if exit_or_no() :
            break 
        else:
            continue
