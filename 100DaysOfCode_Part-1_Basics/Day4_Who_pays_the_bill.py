import random
names = names_string.split(", ")
# print(len(names))
buyer = random.randint(0,(len(names)-1))
print (f"{names[buyer]} is going to buy the meal today!")
