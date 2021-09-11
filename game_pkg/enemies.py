class Enemy:
    def __init__(self, name, health_points, ability_points, power, defense, max_ability_points, elemental_set) -> None:
        self.name = name
        self.health_points = health_points
        self.ability_points = ability_points
        self.power = power
        self.defense = defense
        self.max_ability_points = max_ability_points
        self.elemental_set = elemental_set

    def get_name(self, value):
        self.name = value
