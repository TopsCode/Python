class Person:
    def __init__(self, name, subject):
        self.name = name  # Instance attribute
        self.subject = subject    # Instance attribute
    
    def greet(self):  # Instance method
        return f"Hello, my name is {self.name} and my subject is  {self.subject} "

# Creating an instance (object) of the Person class
person1 = Person("Anjali", "Python")

# Accessing attributes and calling methods
print(person1.name)  # Output: Anjali
print(person1.greet())  # Output: Hello, my name is Anjali and my subject is Python.
