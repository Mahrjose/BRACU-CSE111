class Joker:
    def __init__(self, name, power, is_he_psycho):
        self.name = name
        self.power = power
        self.is_he_psycho = is_he_psycho


j1 = Joker("Heath Ledger", "Mind Game", False)
print(j1.name)
print(j1.power)
print(j1.is_he_psycho)
print("=====================")
j2 = Joker("Joaquin Phoenix", "Laughing out Loud", True)
print(j2.name)
print(j2.power)
print(j2.is_he_psycho)
print("=====================")

if j1 == j2:
    print("same")
else:
    print("different")

j2.name = "Heath Ledger"
if j1.name == j2.name:
    print("same")
else:
    print("different")

print("=====================")
# Subtask -2
print(
    "Because they are 2 different instances of Joker class & their memory locations are different"
)
# Subtask -3
print("Because j1.name & j2.name have the same string.")
