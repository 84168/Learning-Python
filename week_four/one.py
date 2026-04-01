# OOPS
# CLASS : blueprint of an object
# OBJECTS: instabce of class

# class Student:
#     subject = "python"
#     college = "ABC"
#     year = "fourth year"

#     # Jo obj call kregi self ki value is equal to that object
#     # its a parametrized constructor
#     def __init__(self, name, cgpa): # self storing the current instance of the class
#         self.name = name # differnt for all user
#         self.cgpa = cgpa
#         print("constructor was called")

#     def get_cgpa(self):
#         return self.cgpa


# stud1 = Student("tarun", 9)  #object stud1 python auto create init method and execute it 
# stud2 = Student("arun",9.8)  # crete init method if not creaeted by user
# print(stud1.name)
# print(stud2.name)
# print(stud1.subject)
# print(stud1.get_cgpa()) # print cgpa of obj stud1

# Attributes
# class -> belong to class -> common to all EX.(college name) -> can be invoke by both object and class
# Instance -> belong to object -> unique. EX.(name,subject,cgpa) -> onlly invoke by object 
# Instance has high priority than class Attribute, if both have same attribite with same name then value of instance attribute is printed

# class Student:
#     college_name = "ABC " # Class Attribute
#     def __init__(self, name, gpa):
#         self.name = name  # Instance Attribute 
#         self.gpa = gpa

# stu1 = Student("rahul", 9.0)
# print(stu1.name)
# print(stu1.gpa)
# # print(Student.name) # Show Error : AttributeError: type object 'Student' has no attribute 'name'
# print(stu1.college_name)
# print(Student.college_name)


# Mehods
# INSTANCE , CLASS AND STATIC METHODS

# INSTANCE METHOD
class laptop:
    storage_type ="ssd"

    def __init__(self, RAM, storage):
        self.RAM = RAM
        self.storage = storage

    @classmethod # Decorator : it changes the behavoour of method for which it is defined for
    def get_storage_type(cls): # Class Method : can access all the class Attributes
        print(f"storage Type = {cls.storage_type}")

    def get_info(self): # Instance Method
        print(f"laptop has {self.RAM} RAM and {self.storage} {self.storage_type}") # self.storage_type (Class type attr) also accessed

l1 = laptop("16gb", "512gb")
l2 = laptop("8gb", "256gb")

l1.get_info()
l2.get_info()