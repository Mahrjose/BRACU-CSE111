class Student:

    ID = 0

    def __init__(self, name, department, age, cgpa):
        self.name = name
        self.department = department
        self.age = age
        self.cgpa = cgpa

    def get_details(self):
        print(f"ID: {Student.ID}")
        print(f"Name: {self.name}")
        print(f"Department: {self.department}")
        print(f"Age: {self.age}")
        print(f"CGPA: {self.cgpa}")

    @classmethod
    def from_String(cls, str_info):
        name, department, age, cgpa = str_info.split("-")
        return cls(name, department, age, cgpa)


s1 = Student("Samin", "CSE", 21, 3.91)
s1.get_details()
print("-----------------------")
s2 = Student("Fahim", "ECE", 21, 3.85)
s2.get_details()
print("-----------------------")
s3 = Student("Tahura", "EEE", 22, 3.01)
s3.get_details()
print("-----------------------")
s4 = Student.from_String("Sumaiya-BBA-23-3.96")
s4.get_details()

# Quesiton -1
print(
    "Changing the class variable value will also change all the instance value that inherited the same variable from the class"
)
print(
    "But changing a instance variable will only change the varialbe value inside of that specific instance\n"
)

# Quesiotn -2
print(
    "Instance methods cannot be accessed without the instance of that class, but class methods don't need a instance to be used"
)
