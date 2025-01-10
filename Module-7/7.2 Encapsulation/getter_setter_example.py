class Person:
    def __init__(self, name, age):
        # Private attributes
        self.__name = name
        self.__age = age

    # Getter method for name
    def get_name(self):
        return self.__name

    # Setter method for name
    def set_name(self, name):
        if isinstance(name, str) and len(name) > 0:
            self.__name = name
        else:
            print("Invalid name. Name should be a non-empty string.")

    # Getter method for age
    def get_age(self):
        return self.__age

    # Setter method for age
    def set_age(self, age):
        if isinstance(age, int) and age >= 0:
            self.__age = age
        else:
            print("Invalid age. Age should be a non-negative integer.")

# Create a Person object
person = Person("Ram", 30)

# Using getter methods to access private attributes
print(person.get_name())  # Output: Ram
print(person.get_age())   # Output: 30

# Using setter methods to modify private attributes
person.set_name("Roy")
person.set_age(25)

# Using getter methods after modifying values
print(person.get_name())  # Output: Roy
print(person.get_age())   # Output: 25

# Trying to set invalid values
person.set_name("")  # Invalid name
person.set_age(-5)   # Invalid age
