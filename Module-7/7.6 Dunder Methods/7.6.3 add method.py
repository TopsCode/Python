class Sample:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return Sample(self.value + other.value)

obj1 = Sample(10)
obj2 = Sample(20)
result = obj1 + obj2
print(result.value)  # Output: 30
