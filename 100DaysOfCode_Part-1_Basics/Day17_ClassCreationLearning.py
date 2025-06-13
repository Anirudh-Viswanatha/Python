# #class creation 1
# class Car:
#     def __init__(self, tyres, doors, seats):
#         self.tyres = tyres # convention in class construction is parameter above (tyres) shoudl be same as variable in this line but its not mandatory
#         self.doors = doors
#         self.seats = seats
#         self.silencer = 1  #This is going to always be 1 in the beginning unless customer wants to add more for sound
#     def enter_race_mode(self):
#         self.seats = 1.5
#
#
# #object creation
# fiat = Car(4, 4, 6)
# fiat.silencer+=6
# ferrari = Car(4,2,2)
# truck= Car(12,3,2)
# bus = Car(8,2, 50)
# bus.enter_race_mode()
#
# print(truck.tyres)
# print(bus.seats)
# print(fiat.doors)
# print(fiat.silencer)

#----------------------------------------------------------------------------------------------------#


# Class creation 2
class User:    # classs creation
    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1

user_1 = User("001", "Anirudh") # Object Creation
user_2 = User("002","Nikita") # Object Creation
user_3 = User("003","Priyana") # Object Creation
user_4 = User("004","Sai") # Object Creation

user_1.follow(user_2)
user_2.follow(user_1)
user_3.follow(user_1)
user_2.follow(user_3)
user_3.follow(user_4)
user_4.follow(user_3)
user_4.follow(user_1)


print(f"User_1 Followers:{user_1.followers} and user_1 Following: {user_1.following}")
print(f"User_2 Followers:{user_2.followers} and user_2 Following: {user_2.following}")
print(f"User_3 Followers:{user_3.followers} and user_3 Following: {user_3.following}")
print(f"User_4 Followers:{user_4.followers} and user_4 Following: {user_4.following}")




#----------------------------------------------------------------------------------------------------#




#
#
# #class creation 3
#
# class Human:    # class creation
#     def __init__(self, eyes, nose):   # initialization function /constructor with 2 parameters eyes, nose
#         self.eyes = eyes
#         self.nose = nose
#         print("New user being created again.......")
#
#
# ani = Human(3,1)
# print(ani.nose)
# print(ani.eyes)
