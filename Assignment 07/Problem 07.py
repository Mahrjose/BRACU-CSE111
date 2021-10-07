class Football:
    def __init__(self, team_name, name, role):
        self.__team = team_name
        self.__name = name
        self.role = role
        self.earning_per_match = 0

    def get_name_team(self):
        return "Name: " + self.__name + ", Team Name: " + self.__team


class Player(Football):
    def __init__(self, team_name, name, role, goal, played):
        super().__init__(team_name, name, role)
        self.goal = goal
        self.played = played

    def calculate_ratio(self):
        self.ratio = self.goal / self.played

    def print_details(self):
        earning = (self.goal * 1000) + (self.played * 10)
        print(super().get_name_team())
        print(f"Team Role: {self.role}")
        print(f"Total Goal: {self.goal}, Total Played: {self.played}")
        print(f"Goal Ratio: {self.ratio}")
        print(f"Match Earning: {earning}K")


class Manager(Football):
    def __init__(self, team_name, name, role, win):
        super().__init__(team_name, name, role)
        self.win = win

    def print_details(self):
        earning = self.win * 1000
        print(super().get_name_team())
        print(f"Team Role: {self.role}")
        print(f"Win: {self.win}")
        print(f"Match Earning: {earning}K")


player_one = Player("Juventus", "Ronaldo", "Striker", 25, 32)
player_one.calculate_ratio()
player_one.print_details()
print("------------------------------------------")
manager_one = Manager("Real Madrid", "Zidane", "Manager", 25)
manager_one.print_details()
