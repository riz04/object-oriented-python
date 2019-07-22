# Learning to model a real world object in Python using class

class Person:
    # When you create an instance of person, 
    # __init__ assigns the values to the properties of the class
    def __init__(self,name,age,address):
        self.name = name
        self.age = age
        self.address = address

    # Note: When we want to access the properties of the class, 
    # we use self.property name for ex- self.name & self.age
    
    # person can give intro
    def intro(self):
        print(f"I am {self.name}. I am {self.age} years old")

    # person can walk with the given speed
    def walk(self,speed):
        print(f"My walking speed is {speed} km/h")
    
    # person can play for given hours    
    def play(self,hours):
        print(f"I play for {hours} hours")

    # person can have given dish for lunch
    def lunch(self,dish):
        print(f"I ate {dish} in lunch")




