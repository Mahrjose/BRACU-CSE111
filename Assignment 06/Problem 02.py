class Assassin:

    assassin_count = 0

    def __init__(self, name, success):
        self.name = name
        self.success = success
        Assassin.assassin_count += 1

    def printDetails(self):
        print(f"Name: {self.name}")
        print(f"Success rate: {self.success}%")
        print(f"Total number of Assassin: {Assassin.assassin_count}")

    @classmethod
    def failureRate(cls, name, rate):
        success = 100 - rate
        return cls(name, success)

    @classmethod
    def failurePercentage(cls, name, percentage):
        success = 100 - percentage
        return cls(name, success)


john_wick = Assassin("John Wick", 100)
john_wick.printDetails()
print("================================")
nagisa = Assassin.failureRate("Nagisa", 20)
nagisa.printDetails()
print("================================")
akabane = Assassin.failurePercentage("Akabane", 10)
akabane.printDetails()
