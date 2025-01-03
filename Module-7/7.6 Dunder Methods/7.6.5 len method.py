class MyClass:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)

obj = MyClass([1, 2, 3])
print(len(obj))  # Output: 3
