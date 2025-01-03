class Sample:
    def __init__(self, items):
        self.items = items

    def __setitem__(self, index, value):
        self.items[index] = value

obj = Sample([10, 20, 30, 40])
obj[2] = 100
print(obj.items)  # Output: [10, 20, 100, 40]
