class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def describe(self):
        return f"{self.name} is {self.age} years old."

student = Student("Bunny", 13)
print(student.describe())  # Output: Buddy is 13 years old.
