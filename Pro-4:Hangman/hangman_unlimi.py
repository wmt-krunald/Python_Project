import random
from word_sample import words
import string

def get_valid_word(words):
    word = random.choice(words) #Take random word from words list
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()

def hangman():
    print("\nLet's Play Hangman. This game has Unlimited moves.")
    word = get_valid_word(words)
    word_letters = set(word)  #Trake of what letters are in word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  #Trake or set of what used letters what user has gussed
    
    #Getting User Input:
    while len(word_letters) > 0:

        #First tell the user which are letters they have used.
        #" ".join(["a", "b", "cd"]) --> "a b cd"
        print("\nYou have used these letters: "," ".join(used_letters))

        #What Current word is (W - R D)
        word_list = [letter if letter in used_letters else "-" for letter in word]
        print("Current Word: ", "".join(word_list))

        user_letter = input("Gusse a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                    
        elif user_letter in used_letters:
                print("\nYou have already used this letter. Please try again.")
        else:
                print("\nInvalid Character. Please Enter a valid Character.")
    
    print(f"\nYeyyy, You Crack the Game. The word is: {word}")

hangman()