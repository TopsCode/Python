class BankAccount:
    def __init__(self, account_holder, balance):
        # Public attribute
        self.account_holder = account_holder
        # Private attribute (name mangling)
        self.__balance = balance  # Private attribute

    # Public method to access private attribute (getter method)
    def get_balance(self):
        return self.__balance

    # Public method to modify private attribute (setter method)
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Deposit amount must be positive.")

    # Public method to modify private attribute (setter method)
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Invalid withdrawal amount.")

# Create an instance of the BankAccount class
account = BankAccount("John Doe", 1000)

# Accessing public attribute directly
print(account.account_holder)  # Output: John Doe

# Accessing private attribute directly will cause an error
# print(account.__balance)  # AttributeError: 'BankAccount' object has no attribute '__balance'

# Using getter method to access the private attribute
print(account.get_balance())  # Output: 1000

# Using setter methods to modify the private attribute
account.deposit(500)
print(account.get_balance())  # Output: 1500

account.withdraw(200)
print(account.get_balance())  # Output: 1300

# Trying to access private attribute using name mangling
print(account._BankAccount__balance)  # Output: 1300 (not recommended, it's not intended to be accessed like this)
