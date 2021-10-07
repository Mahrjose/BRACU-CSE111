class EPL_Team:
    def __init__(self, name, song="No Slogan"):
        self.name = name
        self.song = song
        self.title = 0

    def increaseTitle(self):
        self.title += 1

    def changeSong(self, song):
        self.song = song

    def showClubInfo(self):
        return f"Name: {self.name}\nSong: {self.song}\nTotal No of title: {self.title}"


manu = EPL_Team("Manchester United", "Glory Glory Man United")
chelsea = EPL_Team("Chelsea")
print("===================")
print(manu.showClubInfo())
print("##################")
manu.increaseTitle()
print(manu.showClubInfo())
print("===================")
print(chelsea.showClubInfo())
chelsea.changeSong("Keep the blue flag flying high")
print(chelsea.showClubInfo())
