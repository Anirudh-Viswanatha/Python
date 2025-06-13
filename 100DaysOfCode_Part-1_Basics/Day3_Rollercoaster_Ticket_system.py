print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if height >= 120:
  print("you can ride the rollercoaster!")
  age = int(input("What is your age? "))
#   photo = input ("Do you want a photo? Y or N ") # $3 extra for photo
  if age < 12 :
    bill = 5
    print ("child tickets are $5.")
    # if photo == "Y":
    #   print ("Please pay $8.")   Note: Tried to hardcode here which might not be great option,instead should do something like below using bill variable.
    # else:
    #   print ("Please pay $5.")
  elif age >=12 and age <=18: 
    bill = 7
    print ("Youth tickets are $7.")
    # if photo == "Y":
    #   print ("Please pay $10.")
    # else:
    #   print ("Please pay $7.")
  else:
    bill = 12
    print("Adult tickets are $12.")
    # if photo == "Y":
    #   print ("Please pay $15.")
    # else:
    #   print ("Please pay $12.")  
  photo = input ("Do you want a photo? Y or N ") # $3 extra for photo
  if photo == "Y":
    bill += 3
   #print (f"Your bill is {bill}")  Note: instead of writing total bill print twice (within if and else) we can do sometihng like this. here if condition is calculating photo (Yes=+$3) and then using single print statement final bill. 
# else:  
#   print (f"Your bill is {bill}")
  print (f"Your bill is {bill}")
else:
  print("Sorry, you are not tall enough to ride the roller coaster.")
  