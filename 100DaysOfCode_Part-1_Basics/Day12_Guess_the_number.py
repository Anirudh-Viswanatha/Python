    #Number Guessing Game Objectives:

    # Include an ASCII art logo.
    # Allow the player to submit a guess for a number between 1 and 100.
    # Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
    # If they got the answer correct, show the actual answer to the player.
    # Track the number of turns remaining.
    # If they run out of turns, provide feedback to the player. 
    # Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random
import art
# Intro
print(art.logo)
print("Welcome to the Number Guessing Game!")

#step1 (Pick a random number)
print("I'm thinking of a number between 1 and 100")
Random_number = random.randint(1, 100)
# print(Random_number) Testing code

#step 2
level_select = input("Choose a difficulty. Type 'easy' or 'hard': ")
def level():
  if level_select == "hard":
    return 5
  elif level_select == "easy":
    return 10

#step 3
def guess_a_num():
  global user_guess
  user_guess = int(input("Make a guess:"))
  return user_guess

#step 4 (comparision)
life_count = level()
should_continue = True

while should_continue:
  if life_count > 0:
    print(f"you have {life_count} attempts remaining to guess the number")
    guess_a_num()
    if user_guess > Random_number:
      print("Too high.")
      if life_count > 1:
        print("Guess again.")
      life_count -= 1
    elif user_guess < Random_number:
      print("Too Low.")
      if life_count > 1:
        print("Guess again.")
      life_count -= 1
    elif user_guess == Random_number:
      print(f"You got it! The answer was {Random_number}.")
      should_continue = False
  else:
    should_continue = False
    print("You've run out of guesses, you lose.")
