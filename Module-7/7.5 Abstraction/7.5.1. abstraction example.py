from abc import ABC, abstractmethod

# Abstract class
class Animal(ABC):

    @abstractmethod
    def make_sound(self):
        pass

# Subclass
class Dog(Animal):
    
    def make_sound(self):
        return "Woof!"

# Subclass
class Cat(Animal):
    
    def make_sound(self):
        return "Meow!"

# Create objects of the subclasses
dog = Dog()
cat = Cat()

# Calling the make_sound method
print(dog.make_sound())  # Output: Woof!
print(cat.make_sound())  # Output: Meow!
