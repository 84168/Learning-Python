# ENCAPSULATION , wrapping data and functions into single unit
# 1. public , attribute accessible at both inside and outside the class
# 2. private, only inside the class
# 3. protected, only in class and subclass
# In Protected, it is only by convention we can access it outside the class but we generally do not do it or Enforced
# In private it is enforced id we use it outside the class it shows us the error 

class BankAccount:
    def __init__(self, name, balance):
        self.name = name                 # PUBLIC
        # self._balance = balance          # Protected (single underscore)
        self.__balance = balance          # Private (double underscore)

    def get_balance(self): # use this to access the private balance
        return self.__balance
    
    def set_balance(self, new_balance): # to update the private balance
        self.__balance = new_balance


acc1 =  BankAccount("rahul", 100_000)

# we can access private attribute as :
print(acc1._BankAccount__balance)

# print(acc1.name, acc1.get_balance())
# print(acc1.name, acc1.set_balance(200_000))
# print(acc1.name, acc1.get_balance())
