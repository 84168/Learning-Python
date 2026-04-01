# # Question: 1
# class BankAccount:
#     def __init__(self, Account_number, Owner_name, Balance):
#         self.Account_number = Account_number
#         self.Owner_name = Owner_name
#         self.Balance = Balance
    
#     def Deposit(self, amount):
#         self.Balance += amount
    
#     def Withdraw(self, amount):
#         self.Balance -= amount

#     def Check_balance(self):
#         print(f"{self.Owner_name} Your balance is {self.Balance}")

# b1 = BankAccount(100, "Tarun Parmar", 20_00)
# print(b1.Account_number, b1.Owner_name, b1.Balance)

# b1.Deposit(10_00)
# print(b1.Account_number, b1.Owner_name, b1.Balance)

# b1.Withdraw(500)
# print(b1.Account_number, b1.Owner_name, b1.Balance)

# b1.Check_balance()

# # Question: 2
# class Book:
#     def __init__(self, title, author, list_of_review = None): # List is created with None
#         self.title = title
#         self.author = author
        
#         if(list_of_review == None):
#             self.list_of_review = []
#         else:
#             self.list_of_review = [list_of_review]

#     def add_review(self, review):
#         self.list_of_review.append(review)
#         print(review)

#     def countReview(self):
#         print(len(self.list_of_review))
    
# b1 = Book("Ramayan", "valmiki", "historic")
# print(f"{b1.author} , {b1.title}, {b1.list_of_review}")
# b1.countReview()
# b1.add_review("it is oue truth")
# b1.countReview()


# # Question: 3
# class Student:
#     def __init__(self):
#         # PRIVATE ATTRIBUTES
#         self.__name = ""
#         self.__roll_no = -1
#         self.__marks = -1
#     def setter(self, name, roll_no, marks):
#         self.__name = name
#         self.__roll_no = roll_no
#         if marks <= 100 and marks > 1:
#             self.__marks = marks
#         else:
#             print("enter Valid marks")
    
#     def getter(self):
#         print(f"Name is : {self.__name}, marks is : {self.__marks}, roll_no is : {self.__roll_no}")

# s1 = Student()
# s1.setter("tarun parmar" , 800, 900)
# s1.getter()
    
# # Question: 4
# class Shape:
#     def area(self):
#         pass

# class Circle(Shape):
#     pi = 3.14
#     def area(self, radius):
#         print(f"area is {Circle.pi * radius * radius}")

# class Rectangle(Shape):
#     def area(self, length, breadth):
#         print(f"area is {length * breadth}")

# class Triangle(Shape):
#     def area(self, base , height):
#         print(f"area is {(base * height) / 2}")

# c1 = Circle()
# c1.area(2)

# r1 = Rectangle()
# r1.area(2,3)

# t1 = Triangle()
# t1.area(2,2)

# # Question: 5
# class Vehicle:
#     def __init__(self, brand):
#         self.brand = brand
# class Car(Vehicle):
#     def __init__(self, brand, model, seats):
#         super().__init__ (brand)
#         self.model = model
#         self.seats = seats
# class Bike(Vehicle):
#     def __init__(self,brand, model, seats):
#         super().__init__(brand)
#         self.model = model
#         self.seats = seats

# c1 = Car("fortuner", "5g", 3)
# c2 = Car("MG","6g", 5)

# b1 = Bike("hero", "splender", 4)
# b2 = Bike("honda", "splendr pro", 2)

# print(f"{c1.brand}, {c1.model}, {c1.seats}")
# print(f"{c2.brand}, {c2.model}, {c2.seats}")

# print(f"{b1.brand}, {b1.model}, {b1.seats}")
# print(f"{b2.brand}, {b2.model}, {b2.seats}")

# # Question: 6
# from abc import ABC, abstractmethod
# # In Python, just adding the @abstractmethod decorator isn't enough to 
# # stop someone from creating a generic employee. To make a class 
# # truly abstract, it must inherit from ABC (Abstract Base Class).

# class Employee(ABC):

#     @abstractmethod
#     def calculate_salary(self):
#         pass

# class Intern(Employee):
#     days = 20
#     def __init__(self, per_day):
#         self.per_day = per_day
    
#     def calculate_salary(self):
#         print(f"Salary is : {self.per_day * Intern.days}")

# class FullTime(Employee):
#     days = 30
#     def __init__(self, per_day):
#         self.per_day = per_day
    
#     def calculate_salary(self):
#         print(f"Salary is : {self.per_day * FullTime.days}")

# class ContractEmp(Employee):
#     days = 10
#     def __init__(self, per_day):
#         self.per_day = per_day
    
#     def calculate_salary(self):
#         print(f"Salary is : {self.per_day * ContractEmp.days}")

# i1 = Intern(300)
# f1 = FullTime(500)
# c1 = ContractEmp(1000)

# i1.calculate_salary()
# f1.calculate_salary()
# c1.calculate_salary()

# # Question: 7
# class Person:
#     def __init__(self, name, age = None, address = None):
#         self.name = name
#         self.age = age
#         self.address = address
    
# p1 = Person("tarun Parmar")
# p2 = Person("arun parmar", 23)
# p3 = Person("varun Parmar", 21, "inndore")

# print(f"{p1.name}{p1.age}, {p1.address}")
# print(f"{p2.name}{p2.age}, {p2.address}")
# print(f"{p3.name}{p3.age}, {p3.address}")
        
# # Question: 8
# class Player:
#     player_count = 0
#     def __init__(self, name, level):
#         self.name = name
#         self.level = level
#         Player.player_count += 1
#     def playerCount(self):
#         print(f"Total number of players are {self.player_count}")

# p1 = Player("tarun","l1")
# p2 = Player("arun","l2")
# p2 = Player("varun", "l3")
# p1.playerCount()

# # Question: 9
# class Herbivore:
#     def eats(self):
#         print("it eats GRASS")

# class Carnivore:
#     def eats(self):
#         print("it eats NonVeg")

# class Omnivore:
#     def eats(self):
#         print("it eats both veg and non veg")

# class bear(Herbivore, Carnivore, Omnivore):
#     def __init__(self):
#         super().eats()
#         Carnivore.eats(self)
#         Omnivore.eats(self)
    
# b1 = bear()


# Question: 10
class Message:
    message_counter = 1

    def __init__(self, sender, content):
        self.sender = sender
        self.content = content
        self.id = Message.message_counter
        Message.message_counter += 1
    
    def __str__(self):
        return f"({self.id}) {self.sender.username}: {self.content}"
    
class User:
    def __init__(self, username):
        self.username = username
        self.chatroom = None

    def join_chatroom(self, chatroom):
        if self.chatroom:
            print(f"{self.username} is already in chatroom")
        else:
            chatroom.add_user(self)
            self.chatroom = chatroom
            print(f"{self.username} joined {chatroom.name}")
    
    def leave_chatroom(self):
        if not self.chatroom:
            print(f"{self.chatroom} is not in any chatroom")
        else:
            self.chatroom.remove_user(self)
            print(f"{self.username} left {self.chatroom.name}")
            self.chatroom = None
    
    def send_message(self, content):
        if not self.chatroom:
            print(f"{self.username} cannot send a message ")
        else:
            self.chatroom.broadcast(self, content)

class ChatRoom:
    def __init__(self, name):
        self.name = name
        self.users = []
        self.messages = []

    def add_user(self, user):
            self.users.append(user)
        
    def remove_user(self,user):
            self.users.remove(user)
        
    def broadcast(self, sender, content):
            message = Message(sender, content)
            self.messages.append(message)
            print(message)

    def show_chat_history(self):
            print(f"\nChat History of {self.name}: ")
            for msg in self.messages:
                print(msg)

if __name__ == "__main__":
    room = ChatRoom("Python Learning")

    u1 = User("Alice")
    u2 = User("bob")
    u3 = User("charlie")

    u1.join_chatroom(room)
    u2.join_chatroom(room)

    u1.send_message("hello everyoone")
    u2.send_message("hi !Alice")

    u3.join_chatroom(room)
    u3.send_message("hey guys ")

    room.show_chat_history()

    u1.leave_chatroom()
    u2.leave_chatroom()
    u3.leave_chatroom()