class Panda:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    def sleep(self, sleep_time = None):
        if sleep_time is None:
            return f"{self.name}'s duration is unknown thus should have only bamboo leaves"
    
        elif sleep_time >= 3 and sleep_time <= 5:
            return f"{self.name} sleeps {sleep_time} hours daily and should have Mixed Veggies"

        elif sleep_time >= 6 and sleep_time <= 8:
            return f"{self.name} sleeps {sleep_time} hours daily and should have Eggplant & Tofu"

        elif sleep_time >= 9 and sleep_time <= 11:
            return f"{self.name} sleeps {sleep_time} hours daily and should have Broccoli Chicken"


panda1 = Panda("Kunfu","Male", 5)
panda2=Panda("Pan Pan","Female",3)
panda3=Panda("Ming Ming","Female",8)
print("{} is a {} Panda Bear who is {} years old".format(panda1.name,panda1.gender,panda1.age))
print("{} is a {} Panda Bear who is {} years old".format(panda2.name,panda2.gender,panda2.age))
print("{} is a {} Panda Bear who is {} years old".format(panda3.name,panda3.gender,panda3.age))
print("===========================")
print(panda2.sleep(10))
print(panda1.sleep(4))
print(panda3.sleep())