class PokemonBasic:
    def __init__(self, name="Default", hp=0, weakness="None", type="Unknown"):
        self.name = name
        self.hit_point = hp
        self.weakness = weakness
        self.type = type

    def get_type(self):
        return "Main type: " + self.type

    def get_move(self):
        return "Basic move: " + "Quick Attack"

    def __str__(self):
        return (
            "Name: "
            + self.name
            + ", HP: "
            + str(self.hit_point)
            + ", Weakness: "
            + self.weakness
        )


class PokemonExtra(PokemonBasic):
    def __init__(
        self,
        name="Defalut",
        hp=0,
        weakness=None,
        type=None,
        secondary=None,
        *extra_moves,
    ):
        super().__init__(name, hp, weakness, type)
        self.secondary = secondary
        self.extra_moves = extra_moves

        self.move_lst = list(self.extra_moves)
        self.var1 = []
        self.var2 = ""
        for i in self.extra_moves:
            self.var1 = list(i)
        self.var2 += ", ".join(self.var1)

    def get_type(self):
        if self.secondary == None:
            return f"Main type: {self.type}"
        else:
            return f"Main type: {self.type} Secondary type: {self.secondary}"

    def get_move(self):
        if len(self.extra_moves) == 0:
            return "Basic move: Quick Attack"
        else:
            return f"Basic move: Quick Attack\nOther moves: {str(self.var2)}"


print("\n------------Basic Info:--------------")
pk = PokemonBasic()
print(pk)
print(pk.get_type())
print(pk.get_move())
print("\n------------Pokemon 1 Info:-------------")
charmander = PokemonExtra("Charmander", 39, "Water", "Fire")
print(charmander)
print(charmander.get_type())
print(charmander.get_move())
print("\n------------Pokemon 2 Info:-------------")
charizard = PokemonExtra(
    "Charizard", 78, "Water", "Fire", "Flying", ("Fire Spin", "Fire Blaze")
)
print(charizard)
print(charizard.get_type())
print(charizard.get_move())
