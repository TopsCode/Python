class MyClass:
    def greet(self):
        print("Hello!")

try:
    obj = MyClass()
    obj.say_hello()  # Method does not exist
except AttributeError:
    print("Error: The object has no attribute 'say_hello'.")
