# Inheritance, reusing attr and methods from a parents (Base) class
# use protected : when we dont want to give access outside the class but sub class can access the Attribute
# use private : whien we dont watn to give access to outside the class and sub class

# class Employee:
#     start_time = "10am"
#     end_time = "6pm"
#     def change_Time(self, new_end_time):
#         self.end_time = new_end_time

# class Teachers(Employee):               # SUBCLASS
#     def __init__(self, subject):
#         self.subject = subject

# class AdminStaff(Employee):
#     def __init__(self, role):
#         self.role = role


# t1 = Teachers("Maths")
# print(t1.subject)
# t1.change_Time("5am")                   # Only for the object t1 the time is changed
# print(t1.start_time, t1.end_time)       # INHERITED FROM PARENT CLASS EMPLOYEE

# t2 = Teachers("science")
# print(t2.start_time, t2.end_time)

# staff1 = AdminStaff("manager")
# print(f"{staff1.role} {staff1.start_time} {staff1.end_time}")

# TYPES
# 1. Single Level Inheritance only one parent and one child
# hierarchical one parent -> multiple children
# 2. multi Level parent -> child (parent) -> grand child
# 3. multiple inheritance, 

# MULTILEVEL: 
# class Employee:
#     start_time = "10am"
#     end_time = "5pm"

# class AdminStaff(Employee):
#     def __init__(self, role):
#         self.role = role

# class Accountant(AdminStaff):
#     def __init__(self, salary, role):
#         super().__init__(role)             # we use super to call the constructor of parent class to assign role
#         self.salary = salary
        

# acc1 = Accountant(20_000,"CA")             # we have to pass salary and role both cause accountant inherited the AdminStaff and admin staff needs role
# print(acc1.salary, acc1.role, acc1.start_time, acc1.end_time)


#  MULTIPLE INHERITANCE
class Teacher:
    def __init__(self, salary):
        self.salary = salary
    
class Student:
    def __init__(self, gpa):
        self.gpa = gpa

class TA(Teacher, Student):
    def __init__(self, salary, gpa, name):
        super().__init__(salary)
        Student.__init__(self, gpa)  
        self.name = name


TA1 = TA(100_000, 9.0, "Tarun")
print(f"{TA1.salary}, {TA1.gpa}, {TA1.name}")
