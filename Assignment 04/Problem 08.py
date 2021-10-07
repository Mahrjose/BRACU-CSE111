class Student:
    def __init__(self, name, ID, dept="CSE"):
        self.name = name
        self.ID = ID
        self.dept = dept

    def dailyEffort(self, hours):
        self.hours = hours

    def printDetails(self):
        print(f"Name: {self.name}")
        print(f"ID: {self.ID}")
        print(f"Department: {self.dept}")
        print(f"Daily Effort: {self.hours} hour(s)")

        if self.hours <= 2:
            print("Suggestion: Should give more effort!")
        elif self.hours <= 4:
            print("Suggestion: Keep up the good work!")
        else:
            print("Suggestion: Execellent! Now motivate others.")


harry = Student("Harry Potter", 123)
harry.dailyEffort(3)
harry.printDetails()
print("========================")
john = Student("John Wick", 456, "BBA")
john.dailyEffort(2)
john.printDetails()
print("========================")
naruto = Student("Naruto Uzumaki", 777, "Ninja")
naruto.dailyEffort(6)
naruto.printDetails()
