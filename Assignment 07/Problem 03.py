class Tournament:  # review
    def __init__(self, name="Default"):
        self.__name = name

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name


class Cricket_Tournament(Tournament):
    def __init__(self, name=None, teams=0, type="No type"):
        self.teams = teams
        self.type = type
        self.name = name

        if self.name == None:
            self.name = super().__init__()
        else:
            self.name = super().__init__(name)

    def detail(self):
        name = super().get_name()
        return f"Cricket Tournament Name: {name}\nNumber of Teams: {self.teams}\nType: {self.type}"


class Tennis_Tournament(Tournament):
    def __init__(self, name, player_num):
        self.name = name
        self.player_num = player_num

    def detail(self):
        return (
            f"Tennis Tournamnet Name: {self.name}\nNumber of Players: {self.player_num}"
        )


ct1 = Cricket_Tournament()
print(ct1.detail())
print("-----------------------")
ct2 = Cricket_Tournament("IPL", 10, "t20")
print(ct2.detail())
print("-----------------------")
tt = Tennis_Tournament("Roland Garros", 128)
print(tt.detail())
