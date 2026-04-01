# Abstraction, hiding internal details and showing only essential featutres
# Abstract class-> blueprint for other classes we use ABC Module to create Abstract Classes
# from abc import ABC, abstractmethod

# class Animal(ABC):
#     @abstractmethod
#     def make_sound(self):
#         pass                        # represents, for now this method is doing nothing
        

# class Lion(Animal):
#     def make_sound(self):
#         print("!roar")

# class Cow(Animal):
#     def make_sound(self):
#         print("!moo")

# class Bird(Animal):
#     def make_sound(self):
#         print("!chi")

# l1 = Lion()
# c1 = Cow()
# b1 = Bird()
# b1.make_sound()
# c1.make_sound()
# l1.make_sound()


# POLYMORPHISM, multiple methods with same name but different function
# -> operatore overloading ex,{+}
print(1+2, "hello"+"python")
# 1. FUNCTION OVERRIDING: (INHERITANCE SHOULD PRESENT) redefining parent class methods in child class
# class Employee:
#     def designation(self):
#         print("designation is Employee")

# class Teacher(Employee):
#     def designation(self):
#         print("designation is Tracher")


# t1 = Teacher()
# e1 = Employee()
# e1.designation()
# t1.designation()


# DUCK TYPING, walk like a duck and quack like a duck
#  -> both have same name but have different function

class Teacher():
    def get_designation(self):
        print("is a teacher")

class Accountant():
    def get_designation(self):
        print("is a accountant")
    
t1 = Teacher()
t1.get_designation()

a1 = Accountant()
a1.get_designation()

