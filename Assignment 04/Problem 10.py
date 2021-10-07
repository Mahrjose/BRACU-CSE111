class Avengers:
    def __init__(self, name, partner):
        self.name = name
        self.partner = partner

    def super_powers(self, *power):
        powers = ""
        for i in power:
            powers += i
            powers += ", "
        self.powers = powers

    def printAvengersDetail(self):
        print(f"Name: {self.name}")
        print(f"Partner: {self.partner}")
        print(f"Super powers: {self.powers[:-2]}")


a1 = Avengers("Captain America", "Bucky Barnes")
a1.super_powers("Stamina", "Slowed ageing")
a2 = Avengers("Doctor Strange", "Ancient One")
a2.super_powers("Mastery of magic")
a3 = Avengers("Iron Man", "War Machine")
a3.super_powers("Genius level intellect", "Scientist ")
print("=========================")
a1.printAvengersDetail()
print("=========================")
a2.printAvengersDetail()
print("=========================")
a3.printAvengersDetail()
print("=========================")
