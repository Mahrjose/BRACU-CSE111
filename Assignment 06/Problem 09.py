class Student:

    total_student = 0
    brac_student = 0
    other_student = 0

    def __init__(self, name, dept, institute="BRAC University"):
        self.name = name
        self.dept = dept
        self.institute = institute

        if institute == "BRAC University":
            Student.brac_student += 1
        else:
            Student.other_student += 1

        Student.total_student += 1

    def individualDetail(self):
        print(f"Name: {self.name}")
        print(f"Department: {self.dept}")
        print(f"Institution: {self.institute}")

    @classmethod
    def printDetails(cls):
        print(f"Total Student(s): {cls.total_student}")
        print(f"BRAC University Student(s): {cls.brac_student}")
        print(f"Other Institution Student(s): {cls.other_student}")

    @classmethod
    def createStudent(cls, name, dept, institute=None):
        if institute == None:
            return cls(name, dept)
        else:
            return cls(name, dept, institute)


Student.printDetails()
print("#########################")
mikasa = Student("Mikasa Ackerman", "CSE")
mikasa.individualDetail()
print("------------------------------------------")
Student.printDetails()
print("========================")
harry = Student.createStudent(
    "Harry Potter", "Defence Against Dark Arts", "Hogwarts School"
)
harry.individualDetail()
print("-------------------------------------------")
Student.printDetails()
print("=========================")
levi = Student.createStudent("Levi Ackerman", "CSE")
levi.individualDetail()
print("--------------------------------------------")
Student.printDetails()
