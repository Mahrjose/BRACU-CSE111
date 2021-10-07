class Programmer:
    def __init__(self, name, language, exp):
        self.name = name
        self.language = language
        self.exp = exp
        self.flag = True

    def addExp(self, additional_exp):
        self.flag = False
        print(f"Updating experience of {self.name}")
        self.exp += additional_exp

    def printDetails(self):
        if self.flag:
            print("Horray! A new programmer is born")
        print(f"Name: {self.name}")
        print(f"Language: {self.language}")
        print(f"Experience: {self.exp} years")


p1 = Programmer("Ethen Hunt", "Java", 10)
p1.printDetails()
print("--------------------------")
p2 = Programmer("James Bond", "C++", 7)
p2.printDetails()
print("--------------------------")
p3 = Programmer("Jon Snow", "Python", 4)
p3.printDetails()
p3.addExp(5)
p3.printDetails()
