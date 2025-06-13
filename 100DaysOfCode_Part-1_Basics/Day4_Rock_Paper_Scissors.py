# rock = '''
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# '''

# paper = '''
#     _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)
# '''

# scissors = '''
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# '''

# #Write your code below this line 👇
# import random


# player = int(input("What do you choose? Type 0 for Rock, 1 for paper or 2 for scissors \n"))
# # print (player)
# if player > 2 or player < 0:
#   print("Invalid Input, You lose")
# else:
#   if player == 0:
#     print(rock)
#   elif player == 1:
#     print(paper)
#   elif player == 2:
#     print(scissors)



#   print ("Computer Chose:\n ")
#   computer_chose=random.randint(0,2)

#   if computer_chose == 0:
#     print(rock)
#   elif computer_chose == 1:
#     print(paper)
#   elif computer_chose == 2:
#     print(scissors)

#   if player == computer_chose:
#     print ("It's a draw!")
#   elif player == 0 and computer_chose == 1:
#     print ("You lose!")
#   elif player == 0 and computer_chose == 2:
#     print("You win!")
#   elif player ==1 and computer_chose == 0:
#     print ( "You win!")
#   elif player == 1 and computer_chose == 2:
#     print ("You lose!")
#   elif player == 2 and computer_chose == 0:
#     print ("You lose!")
#   elif player == 2 and compuer_chose == 1:
#     print ("You win!")


# -----------------------------------------------------
# Option 2: Much more Optimized Way

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

game_images = [rock, paper, scissors]

user_pick = int(input("What do you choose? Type 0 for Rock, 1 for paper or 2 for scissors \n"))
if user_pick > 2 or user_pick < 0:
  print("Invalid input, you lose")
else:
  print(game_images[user_pick])

  print ("Computer Chose:")
  computer_chose=random.randint(0,2)
  print(game_images[computer_chose])

  if user_pick == computer_chose:
    print ("It's a draw!")
  elif user_pick == 0 and computer_chose == 1:
    print ("You lose!")
  elif user_pick == 0 and computer_chose == 2:
    print("You win!")
  elif user_pick ==1 and computer_chose == 0:
    print ( "You win!")
  elif user_pick == 1 and computer_chose == 2:
    print ("You lose!")
  elif user_pick == 2 and computer_chose == 0:
    print ("You lose!")
  elif user_pick == 2 and compuer_chose == 1:
    print ("You win!")

