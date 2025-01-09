class Student:
    subject = "python"  # Class attribute
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    @classmethod
    def get_subject(cls):
        return cls.subject
    
    @classmethod
    def set_subject(cls, new_subject):
        cls.subject = new_subject

# Calling class method
print(Student.get_subject())  # Output: python

# Modifying class attribute using class method
Student.set_subject("Flutter")
print(Student.get_subject())  # Output: Flutter
