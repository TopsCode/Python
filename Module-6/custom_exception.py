# Defining a custom exception
class NegativeValueError(Exception):
    def __init__(self, message="Value cannot be negative"):
        self.message = message
        super().__init__(self.message)

# Function that raises the custom exception
def check_value(value):
    if value < 0:
        raise NegativeValueError(f"Negative value encountered: {value}")
    else:
        print(f"The value is: {value}")

# Test the custom exception
try:
    num = int(input("Enter a number: "))
    check_value(num)
except NegativeValueError as e:
    print(f"Error: {e}")
