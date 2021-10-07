class Team:
    def __init__(self, name):
        self.name = "default"
        self.total_player = 5

    def info(self):
        print("We love sports")


class FootBallTeam(Team):
    def __init__(self, name):
        super().__init__(name)
        self.name = name
        self.total_player = 11

    def info(self):
        print(f"Our name is {self.name}\nWe play Football")
        super().info()


class CricketTeam(Team):
    def __init__(self, name):
        super().__init__(name)
        self.name = name
        self.total_player = 11

    def info(self):
        print(f"Our name is {self.name}\nWe play Cricket")
        super().info()


class Team_test:
    def check(self, tm):
        print("=========================")
        print("Total Player:", tm.total_player)
        tm.info()


f = FootBallTeam("Brazil")
c = CricketTeam("Bangladesh")
test = Team_test()
test.check(f)
test.check(c)
