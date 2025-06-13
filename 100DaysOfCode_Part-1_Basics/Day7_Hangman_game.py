import random
#from replit import clear

from hangman_words import word_list   # or import hangman_words
from hangman_art import *       # or import  hangman_art


chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game =  False
lives = 6

print (logo)
#Testing code
#print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    #clear()   This will clear screen after each new guess. output will be cleaner. This uses clear function in replit module.

    if guess in display:
      print(f"{guess} letter already guessed. Please try a different letter")

  #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

  #Check if user is wrong.
    if guess not in chosen_word:
        print(f"{guess} letter not in the word. You lose a life")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

#Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

  #start printing hangman art for different stages.
    print(stages[lives])