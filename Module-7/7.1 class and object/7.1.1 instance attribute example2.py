# instance attribute 

class Car:
    def __init__(self, brand, model):
        self.brand = brand    # Instance attribute
        self.model = model  # Instance attribute

# Creating instances of the Car class
car1 = Car("Toyota", "Camry")
car2 = Car("Honda", "Civic")

print(car1.brand)  # Output: Toyota
print(car2.make)  # Output: Honda
