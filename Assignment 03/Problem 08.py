class DemonSlayer:
    def __init__(self, name, style, number_of_technique, kill):
        self.name = name
        self.style = style
        self.number_of_technique = number_of_technique
        self.kill = kill


tanjiro = DemonSlayer("Tanjiro", "Water Breathing", 10, 10)
print("Name:", tanjiro.name)
print("Fighting Style:", tanjiro.style)
print(
    f"Knows {tanjiro.number_of_technique} technique(s) and has killed {tanjiro.kill} demon(s)"
)
print("===================")
zenitsu = DemonSlayer("Zenitsu", "Thunder Breathing", 1, 4)
print("Name:", zenitsu.name)
print("Fighting Style:", zenitsu.style)
print(
    f"Knows {zenitsu.number_of_technique} technique(s) and has killed {zenitsu.kill} demon(s)"
)
print("===================")
inosuke = DemonSlayer("Inosuke", "Beast Breathing", 5, 7)
print("Name:", inosuke.name)
print("Fighting Style:", inosuke.style)
print(
    f"Knows {inosuke.number_of_technique} technique(s) and has killed {inosuke.kill} demon(s)"
)
print("===================")
print(
    f"{tanjiro.name}, {zenitsu.name}, {inosuke.name} knows total {tanjiro.number_of_technique + zenitsu.number_of_technique + inosuke.number_of_technique} techniques"
)
print(f"They have killed total {tanjiro.kill + zenitsu.kill + inosuke.kill} demons")
