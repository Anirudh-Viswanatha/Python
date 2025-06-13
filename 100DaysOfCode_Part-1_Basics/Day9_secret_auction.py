from replit import clear
#HINT: You can call clear() to clear the output in the console.
import art
print(art.logo)

dict = {}

bid_on = True

while bid_on:
  def auction():
    name = input("what is your name?: ")
    bid = int(input("What is your bid?:" ))
    dict[name] = bid
  auction()
  continue_bid = input("Are there any other bidders? Type 'yes' or 'no'.: ")
  clear()
  if continue_bid == "yes": #----> No need to write this instead we can only one condition like if continue_bid =="no", then do someything. If continue_bid is not "no" (which is yes), it will run in loops.
    bid_on = True
  elif continue_bid =="no":
    bid_on = False
    largest_bid = 0
    for key in dict:
      if largest_bid <= dict[key]:
        largest_bid = dict[key]
        winner = key
    print (f"Winner is {winner} with a bid of ${largest_bid}")

    
# --------------------------------------------------------------------------------
# Optimized version:


# from replit import clear
# #HINT: You can call clear() to clear the output in the console.
# import art
# print(art.logo)

# dict = {}

# bid_on = True

# while bid_on:
#   def auction():
#     name = input("what is your name?: ")
#     bid = int(input("What is your bid?:" ))
#     dict[name] = bid
#     continue_bid = input("Are there any other bidders? Type 'yes' or 'no'.: ")
#     clear()
#     if continue_bid =="no":
#       bid_on = False
#       largest_bid = 0
#       for key in dict:
#         if largest_bid <= dict[key]:
#           largest_bid = dict[key]
#           winner = key        
#       print (f"Winner is {winner} with a bid of ${largest_bid}")
#   auction()

    