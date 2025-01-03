class Sample:
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        return self.value == other.value

obj1 = Sample(10)
obj2 = Sample(10)
print(obj1 == obj2)  # Output: True
