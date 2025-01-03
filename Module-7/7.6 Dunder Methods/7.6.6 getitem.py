class Sample:
    def __init__(self, items):
        self.items = items

    def __getitem__(self, index):
        return self.items[index]

obj = Sample([10, 20, 30, 40])
print(obj[2])  # Output: 30
