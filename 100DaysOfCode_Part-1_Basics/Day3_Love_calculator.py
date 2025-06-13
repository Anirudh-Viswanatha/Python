print("The Love Calculator is calculating your score...")
name1 = input("What is your name? ") # What is your name?
name2 = input("What is their name? ") # What is their name?
combine_name=name1+name2
lowercase=combine_name.lower()
t=(lowercase.count("t"))
r=(lowercase.count("r"))
u=(lowercase.count("u"))
e=(lowercase.count("e"))
l=(lowercase.count("l"))
o=(lowercase.count("o"))
v=(lowercase.count("v"))
e1=(lowercase.count("e"))
first=t+r+u+e
second=l+o+v+e1
love_score=str(first)+str(second) 
love_score=int(love_score) #can combine both lines as love_score=int(str(first)+str(second))
if love_score < 10 or love_score > 90:
  print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score>40 and love_score<50:
  print (f"Your score is {love_score}, you are alright together.")
else:
  print(f"Your score is {love_score}.")


