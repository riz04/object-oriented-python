# Importing Person class
import PersonClass

# Since Student is a Person, we can inherit Student from Person

class Student(PersonClass.Person):
    def __init__(self, name, age, address,  school_name, student_class):
        super().__init__(name, age, address)
        self.student_class = student_class
        self.school_name = school_name

    # student can give intro
    def intro(self):
        # using super(), we can access the methods of the parent class
        super().intro()
        print(f"I am studying in {self.school_name}. I am in {self.student_class} class")

    # student can have given dish for lunch only at lunch time
    # Here we are using the concept of method overriding
    # Parent class Person has the same method but accepts only single argument
    # lunch() method of Student class will have a particular time for lunch
    def lunch(self,dish, time):
        print(f"I ate {dish} in lunch at {time}")

    # student have to study
    def study(self,hours):
        print(f"I study for {hours} hours")

    # student has to give presentation
    def presentation(self, topic):
        print('Going to present---')
        self.intro()
        print(f'I am going to talk about "{topic}""')

student_one = Student("Ram", 13, "Noida", "DAV", "5th")
student_one.intro()

rizul = Student("Rizul", 12, "Delhi", "New Stepping Stone", "6th")
rizul.intro()
rizul.walk(5)
rizul.play(1)
rizul.study(8)
rizul.lunch("Coke", "2:30 pm")
rizul.presentation('How can we re-use coke')

