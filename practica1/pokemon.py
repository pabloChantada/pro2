"""
TODO: Implement in this file the Pokemon hierarchy.
"""

from abc import ABC, abstractmethod
from math import floor


class Pokemon(ABC):
    def __init__(self, name: str, level: int, strength: int, defense: int,
                 hp: int, total_hp: int, agility: int) -> None:
        self.name = name
        self.level = level
        self.strength = strength
        self.defense = defense
        self.hp = hp
        self.total_hp = total_hp
        self.agility = agility
        self.pokemon_type = "None"

    @property
    def name(self):
        # Property (getter) for the name
        return self._name

    @name.setter
    def name(self, value: str):
        # Setter for the name
        if isinstance(value, str) and len(value) > 0:
            self._name = value
        else:
            raise ValueError("Name must be a non-empty string")

    @property
    def level(self):
        # Property (getter) for the name
        return self._level

    @level.setter
    def level(self, value: int):
        # Setter for the name
        if isinstance(value, int) and value > 0:
            self._level = value
        else:
            raise ValueError("Level must be a positive number")

    @property
    def strength(self):
        # Property (getter) for the name
        return self._strength

    @strength.setter
    def strength(self, value: int):
        # Setter for the name
        if isinstance(value, int) and value > 0:
            self._strength = value
        else:
            raise ValueError("Strength must be a positive number")

    @property
    def defense(self):
        # Property (getter) for the name
        return self._defense

    @defense.setter
    def defense(self, value: int):
        # Setter for the name
        if isinstance(value, int) and value > 0:
            self._defense = value
        else:
            raise ValueError("Defense must be a number")

    @property
    def hp(self):
        # Property (getter) for the name
        return self._hp

    @hp.setter
    def hp(self, value: int):
        # Setter for the name
        if isinstance(value, int) and value >= 0:
            self._hp = value
        else:
            raise ValueError("HP must be a positive number")

    @property
    def total_hp(self):
        # Property (getter) for the name
        return self._total_hp

    @total_hp.setter
    def total_hp(self, value: int):
        # Setter for the name
        if isinstance(value, int) and value > 0:
            self._total_hp = value
        else:
            raise ValueError("Total HP must be a positive number")

    @property
    def agility(self):
        # Property (getter) for the name
        return self._agility

    @agility.setter
    def agility(self, value: int):
        # Setter for the name
        if isinstance(value, int) and value > 0:
            self._agility = value
        else:
            raise ValueError("Agility must be a positive number")

    @property
    def pokemon_type(self):
        # Property (getter) for the name
        return self._pokemon_type

    @pokemon_type.setter
    def pokemon_type(self, value: str):
        # Setter for the name
        if isinstance(value, str) and len(value) > 0:
            self._pokemon_type = value
        else:
            raise ValueError("Pokemon Type must be a non-empty string")

    # Estos dos tienen que ser abstractos ?
    def basic_attack(self, opponent: 'Pokemon') -> int:
        damage_dealt = floor(max(1, self.strength - opponent.defense))
        if (opponent.hp - damage_dealt) < 0:
            opponent.hp = 0
            return damage_dealt
        opponent.hp -= damage_dealt
        return damage_dealt

    def is_debilitated(self) -> bool:
        if self.hp <= 0:
            return True
        return False

    # es del propio pokemon o del enemigo
    @abstractmethod
    def effectiveness(self, opponent: 'Pokemon') -> int:
        raise NotImplementedError
        
    def __str__(self):
        return f"{self.name} ({self.pokemon_type})\
            Stats: Level: {self.level}, ATT: {self.strength}, DEF: {self.defense}, \
                AGI: {self.agility}, HP: {self.hp}/{self.total_hp}."


class WaterPokemon(Pokemon):
    def __init__(self, name: str, level: int, strength: int, defense: int,
                 hp: int, total_hp: int, agility: int, surge_mode: bool) -> None:
        super().__init__(name, level, strength, defense, hp, total_hp, agility)

        self.pokemon_type = "Water"
        self.surge_mode = surge_mode

    def water_attack(self, p: Pokemon) -> int:
        match p.pokemon_type:
            case "Fire":
                factor = 1.5
            case "Water":
                factor = 1
            case "Grass":
                factor = 0.5
        # solo si esto se cumple se hace daño o siempre
        if WaterPokemon.check_surge_activation(self) == True:
            self.surge_mode = True
            factor += 0.1
        else:
            self.surge_mode = False

        damage_dealt = floor(max(1, (factor*self.strength)-p.defense))
        if (p.hp - damage_dealt) < 0:
            p.hp = 0
            return damage_dealt
        p.hp -= damage_dealt
        return damage_dealt

    def check_surge_activation(self) -> bool:
        if self.hp < (self.total_hp/2):
            return True
        return False

    def effectiveness(self, opponent: Pokemon) -> int:
        match opponent.pokemon_type:
            case "Fire":
                return 1
            case "Water":
                return 0
            case "Grass":
                return -1


class GrassPokemon(Pokemon):
    def __init__(self, name: str, level: int, strength: int, defense: int,
                 hp: int, total_hp: int, agility: int, healing: float) -> None:
        super().__init__(name, level, strength, defense, hp, total_hp, agility)

        self.pokemon_type = "Grass"
        self.healing = healing

    def grass_attack(self, p: Pokemon) -> int:
        match p.pokemon_type:
            case "Fire":
                factor = 0.5
            case "Water":
                factor = 1.5
            case "Grass":
                factor = 1

        damage_dealt = floor(max(1, (factor*self.strength)-p.defense))
        if (p.hp - damage_dealt) < 0:
            p.hp = 0
            return damage_dealt
        p.hp -= damage_dealt
        return damage_dealt

    def heal(self) -> int:
        # considera a self.healing como un str ???
        print(type(self.healing))
        print(type(self.hp))
        heal = floor(float(self.healing) * self.hp)
        self.hp += heal
        if self.hp > self.total_hp:
            self.hp = self.total_hp
        return heal

    def effectiveness(self, opponent: Pokemon) -> int:
        match opponent.pokemon_type:
            case "Fire":
                return -1
            case "Water":
                return 1
            case "Grass":
                return 0


class FirePokemon(Pokemon):
    def __init__(self, name: str, level: int, strength: int, defense: int,
                 hp: int, total_hp: int, agility: int, temperature: float) -> None:
        super().__init__(name, level, strength, defense, hp, total_hp, agility)

        self.pokemon_type = "Fire"
        self.temperature = temperature

    def fire_attack(self, p: Pokemon) -> int:
        match p.pokemon_type:
            case "Fire":
                factor = 1
            case "Water":
                factor = 0.5
            case "Grass":
                factor = 1.5

        damage_dealt = floor(max(1, (factor*self.strength)-p.defense))
        if (p.hp - damage_dealt) < 0:
            p.hp = 0
            return damage_dealt
        p.hp -= damage_dealt
        return damage_dealt

    def embers(self, p: Pokemon) -> int:
        damage_dealt = floor(self.strength * float(self.temperature))
        if (p.hp - damage_dealt) < 0:
            p.hp = 0
            return damage_dealt
        p.hp -= damage_dealt
        return damage_dealt

    def effectiveness(self, opponent: Pokemon) -> int:

        match opponent.pokemon_type:
            case "Fire":
                return 0
            case "Water":
                return -1
            case "Grass":
                return 1


'''blastoise = WaterPokemon("Blastoise", 20, 25, 18, 50, 50, 15, "Water", False)
gyarados = WaterPokemon("Gyarados", 30, 30, 20, 80, 80, 12, "Water", True)

venusaur = GrassPokemon("Venusaur", 25, 20, 15, 60, 60, 10, "Grass", 0.1)
sceptile = GrassPokemon("Sceptile", 20, 25, 12, 45, 45, 20, "Grass", 0.2)

charizard = FirePokemon("Charizard", 30, 35, 20, 60, 60, 15, "Fire", 1000)
infernoape = FirePokemon("Infernape", 25, 30, 18, 50, 50, 22, "Fire", 2000)

print(blastoise.effectiveness(gyarados))
print(venusaur.effectiveness(sceptile))
print(charizard.effectiveness(infernoape))
'''
