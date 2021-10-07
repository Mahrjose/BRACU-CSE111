class Pokemon:
    def __init__(
        self, pokemon1_name, pokemon2_name, pokemon1_power, pokemon2_power, damage_rate
    ):
        self.pokemon1_name = pokemon1_name
        self.pokemon2_name = pokemon2_name
        self.pokemon1_power = pokemon1_power
        self.pokemon2_power = pokemon2_power
        self.damage_rate = damage_rate


team_pika = Pokemon("pikachu", "charmander", 90, 60, 10)
print("=======Team 1=======")
print("Pokemon 1:", team_pika.pokemon1_name, team_pika.pokemon1_power)
print("Pokemon 2:", team_pika.pokemon2_name, team_pika.pokemon2_power)
pika_combined_power = (
    team_pika.pokemon1_power + team_pika.pokemon2_power
) * team_pika.damage_rate
print("Combined Power:", pika_combined_power)
# ============================================================================== #
team_bulb = Pokemon("bulbasaur", "squirtle", 80, 70, 9)
print("=======Team 1=======")
print("Pokemon 1:", team_bulb.pokemon1_name, team_bulb.pokemon1_power)
print("Pokemon 2:", team_bulb.pokemon2_name, team_bulb.pokemon2_power)
bulb_combined_power = (
    team_bulb.pokemon1_power + team_bulb.pokemon2_power
) * team_bulb.damage_rate
print("Combined Power:", bulb_combined_power)
