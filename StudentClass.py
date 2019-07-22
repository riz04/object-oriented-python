
class Student:
    # When you create an instance of student, 
    # __init__ assigns the values to the properties of the class
    def __init__(self,name,age,address, school_name, student_class):
        self.name = name
        self.age = age
        self.address = address
        self.school_name = school_name
        self.student_class = student_class

    # Note: When we want to access the properties of the class, 
    # we use self.property name for ex- self.name & self.age
    
    # student can give intro
    def intro(self):
        print(f"I am {self.name}. I am {self.age} years old")
        print(f"I am studying in {self.school_name}. I am in {self.student_class} class")


    # student can walk with the given speed
    def walk(self,speed):
        print(f"My walking speed is {speed} km/h")
    
    # student can play for given hours    
    def play(self,hours):
        print(f"I play for {hours} hours")

    # student can have given dish for lunch only at lunch time
    def lunch(self,dish, time):
        print(f"I ate {dish} in lunch")

    # student have to study
    def study(self,hours):
        print(f"I study for {hours} hours")

student_one = Student("Ram", 18, "Noida", "DAV", "12th")
student_one.intro()
student_one.study(5)
        
