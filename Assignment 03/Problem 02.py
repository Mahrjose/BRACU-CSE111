class Flower:
    def __init__(self):
        pass


flower1 = Flower()
flower1.name = "Rose"
flower1.color = "Red"
flower1.num_of_petal = 6
print("Name of this flower:", flower1.name)
print("Color of this flower:", flower1.color)
print("Number of petal:", flower1.num_of_petal)
print("=====================")
# ======================================================================#
flower2 = Flower()
flower2.name = "Orchid"
flower2.color = "Purple"
flower2.num_of_petal = 4
print("Name of this flower:", flower2.name)
print("Color of this flower:", flower2.color)
print("Number of petal:", flower2.num_of_petal)
# ======================================================================#
print("flower1 memory adress: ", flower1)
print("flower2 memory adress: ", flower2)
if flower2 == flower1:
    print("They are same")
else:
    print("They are different")
