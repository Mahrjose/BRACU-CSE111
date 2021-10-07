class Student:
    def __init__(self, name="default student"):
        self.name = name

    def quizcalc(self, *score):
        average = sum(list(score)) / 3
        self.message = f"Your average quiz score is {average}"

    def printdetail(self):
        print(f"Hello {self.name}")
        print(self.message)


s1 = Student()
s1.quizcalc(10)
print("--------------------------------")
s1.printdetail()
s2 = Student("Harry")
s2.quizcalc(10, 8)
print("--------------------------------")
s2.printdetail()
s3 = Student("Hermione")
s3.quizcalc(10, 9, 10)
print("--------------------------------")
s3.printdetail()
