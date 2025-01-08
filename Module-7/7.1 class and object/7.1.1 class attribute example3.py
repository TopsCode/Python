class Car:
    wheels = 4  # Class attribute (shared by all instances)

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

# Creating instances of the Car class
car1 = Car("Toyota", "Camry")
car2 = Car("Honda", "Civic")

print(car1.wheels)  # Output: 4 (shared by all instances)
print(car2.wheels)  # Output: 4
