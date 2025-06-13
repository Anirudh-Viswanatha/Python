# Class Inheritance Concepts.


# Creating Animal Class
class Animal:
    def __init__(self):
        self.number_of_eyes = 2
    
    def breathe(self):
        print("inhale, Exhale")



# Creating Fish Class and trying to inherit Animal attributes and methods into Fish
class Fish(Animal):
    def __init__(self):
        super().__init__()

    def breathe(self):
        super().breathe()
        print("Doing this underwater")
    
    def swim(self):
        print("Move forward in water")
    


# Creating Object from Fish Class, When creating objects from Fish Class, It will inherit properties(Attributes and Methods) from Animal Class as well as we did a super.__init__() above
        
nemo = Fish()
nemo.swim()
nemo.breathe()
print(nemo.number_of_eyes)



    
