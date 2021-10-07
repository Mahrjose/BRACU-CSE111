class Country:
    def __init__(self):
        self.name = "Bangladesh"
        self.continent = "Asia"
        self.capital = "Dhaka"
        self.fifa_ranking = 187


country = Country()
print("Name:", country.name)
print("Continent:", country.continent)
print("Capital:", country.capital)
print("Fifa Ranking:", country.fifa_ranking)
print("===================")
country.name = "Belgium"
country.continent = "Europe"
country.capital = "Brussels"
country.fifa_ranking = 1
print("Name:", country.name)
print("Continent:", country.continent)
print("Capital:", country.capital)
print("Fifa Ranking:", country.fifa_ranking)
