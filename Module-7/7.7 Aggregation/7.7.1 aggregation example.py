class Department:
    def __init__(self, name):
        self.name = name

    def display_info(self):
        return f"Department: {self.name}"

class University:
    def __init__(self, name):
        self.name = name
        self.departments = []  # A list to hold Department objects

    def add_department(self, department):
        self.departments.append(department)

    def display_departments(self):
        print(f"Departments in {self.name} University:")
        for department in self.departments:
            print(department.display_info())

# Create Department objects
department1 = Department("Computer Science")
department2 = Department("Electrical Engineering")
department3 = Department("Mechanical Engineering")

# Create University object
university = University("Tech University")

# Add departments to the university
university.add_department(department1)
university.add_department(department2)
university.add_department(department3)

# Display departments in the university
university.display_departments()
