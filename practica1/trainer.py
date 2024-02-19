"""
TODO: Implement in the file the Trainer class
"""
from pokemon import *


class Trainer():
    def __init__(self, name: str, pokemon: list) -> None:
        self.name = name
        self.pokemon = pokemon

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
    def pokemon(self):
        # Property (getter) for the name
        return self._pokemon

    @pokemon.setter
    def pokemon(self, value: list):
        # Setter for the name
        if isinstance(value, list) and len(value) > 0:
            self._pokemon = value
        else:
            raise ValueError("The Pokemon list can't be empty")

    def all_debilitated(self) -> bool:
        '''
        para que se usa p ??
        for index in self.pokemon:
            if index.hp != 0:
                return False
        return True
        '''
        for index in self.pokemon:
            if index.hp != 0:
                return False
        return True

    def select_first_pokemon(self) -> Pokemon:
        for actual_pokemon in self.pokemon:
            if actual_pokemon.hp != 0:
                return actual_pokemon
        return None

    def select_next_pokemon(self, p: Pokemon) -> Pokemon:
        if Trainer.select_first_pokemon(self) != None:
            selected = self.pokemon[0]
            # Skipeamos el primero ya que lo seleccionamos antes
            for actual_pokemon in self.pokemon[1:]:
                actual_pokemon.effectiveness(p)
                if selected.hp == 0:
                    selected = actual_pokemon
                elif actual_pokemon.effectiveness(p) > selected.effectiveness(p)\
                        and actual_pokemon.hp != 0:
                    selected = actual_pokemon
                elif actual_pokemon.effectiveness(p) == selected.effectiveness(p)\
                        and actual_pokemon.hp != 0:
                    if actual_pokemon.level > selected.level:
                        selected = actual_pokemon
            return selected
        else:
            return False
