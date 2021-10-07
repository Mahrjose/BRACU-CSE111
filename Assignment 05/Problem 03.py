class Team:
    def __init__(self, name=None):
        self.__name = name
        self.__li = []

    def setName(self, name):
        if self.__name == None:
            self.__name = name

    def addPlayer(self, name):
        self.__li.append(name.player)

    def printDetail(self):
        print("=====================")
        print("Team: ", self.__name)
        print("List of players: ")
        print(self.__li)
        print("=====================")


class Player:
    def __init__(self, player):
        self.player = player


b = Team()
b.setName("Bangladesh")
mashrafi = Player("Mashrafi")
b.addPlayer(mashrafi)
tamim = Player("Tamim")
b.addPlayer(tamim)
b.printDetail()
a = Team("Australia")
ponting = Player("Ponting")
a.addPlayer(ponting)
lee = Player("Lee")
a.addPlayer(lee)
a.printDetail()
