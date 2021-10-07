class Batsman:
    def __init__(self, *var):
        if len(var) == 2:
            runs, balls = var
        else:
            player, runs, balls = var

        if len(var) != 2:
            self.name = player
        else:
            self.name = "New Batsman"

        self.runs = runs
        self.balls = balls

    def setName(self, name):
        self.name = name

    def battingStrikeRate(self):
        return (self.runs) / (self.balls) * 100

    def printCareerStatistics(self):
        print(f"Name: {self.name}")
        print(f"Runs Scored: {self.runs}, Balls Faced: {self.balls}")


b1 = Batsman(6101, 7380)
b1.printCareerStatistics()
print("============================")
b2 = Batsman("Liton Das", 678, 773)
b2.printCareerStatistics()
print("----------------------------")
print(b2.battingStrikeRate())
print("============================")
b1.setName("Shakib Al Hasan")
b1.printCareerStatistics()
print("----------------------------")
print(b1.battingStrikeRate())
