from pokemon import *

'''
Pablo Chantada Saborido | pablo.chantada@udc.es
Pablo Verdes Sánchez | p.verdess@udc.es
'''

class Trainer():
    '''
    Clase que representa a un entrenador de Pokemon.
    '''
    def __init__(self, name: str, pokemon: list) -> None:
        '''
        Inicializa una instancia de la clase Trainer.

        Parameters 
        ----------
        - name (str): El nombre del entrenador.
        - pokemon (list): Una lista de objetos Pokemon pertenecientes al entrenador.
        '''
        self.name = name
        self.pokemon = pokemon

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        if isinstance(value, str) and len(value) > 0:
            self._name = value
        else:
            raise ValueError("El nombre debe ser una cadena no vacía")

    @property
    def pokemon(self):
        return self._pokemon

    @pokemon.setter
    def pokemon(self, value: list):
        if isinstance(value, list) and len(value) > 0:
            self._pokemon = value
        else:
            raise ValueError("La lista de Pokemon no puede estar vacía")

    def all_debilitated(self) -> bool:
        '''
        Comprueba si todos los Pokemon del entrenador están debilitados.

        Returns 
        -------
        bool: True si todos los Pokemon están debilitados, False en caso contrario.
        '''
        # Recorremos la lista de pokemon del entrenador, si encontramos uno que no este debilitado, devolvemos False
        for index in self.pokemon:
            if index.hp != 0:
                return False
        return True

    def select_first_pokemon(self) -> Pokemon:
        '''
        Selecciona el primer Pokemon disponible del entrenador.

        Returns 
        -------
        Pokemon: El primer Pokemon disponible del entrenador, o None si no hay ninguno disponible.
        '''
        # Recorremos la lista de pokemon del entrenador, si encontramos uno que no este debilitado, lo devolvemos
        for actual_pokemon in self.pokemon:
            if actual_pokemon.hp != 0:
                return actual_pokemon
        return None

    def select_next_pokemon(self, p: Pokemon) -> Pokemon:
        '''
        Selecciona el siguiente Pokemon del entrenador para enfrentarse a un Pokemon dado. Se intenta seleccionar el Pokemon más efectivo contra el Pokemon dado, y si no hay ninguno efectivo, se selecciona el de mayor nivel.

        Parameters
        ---------- 
        p (Pokemon): El Pokemon al que se enfrentará el siguiente Pokemon seleccionado.

        Returns 
        -------
        Pokemon: El siguiente Pokemon seleccionado, o False si no hay ninguno disponible.
        '''
        if Trainer.select_first_pokemon(self) != None:
            # Seleccionamos el primer pokemon como placeholder
            selected = self.pokemon[0]
            # Skipeamos el primero ya que lo seleccionamos antes
            for actual_pokemon in self.pokemon[1:]:
                actual_pokemon.effectiveness(p)
                # Si el pokemon incial seleccionado esta debilitado, lo actualizamos
                if selected.hp == 0:
                    selected = actual_pokemon
                    continue
                # Si el pokemon actual es efectivo contra el pokemon dado y no esta debilitado, se selecciona. Sino, se mantiene el que estaba
                if actual_pokemon.effectiveness(p) > selected.effectiveness(p) and actual_pokemon.hp != 0:
                    selected = actual_pokemon
                # Si el pokemon actual es igual de efectivo que el seleccionado y no esta debilitado, se selecciona si es de mayor nivel.
                elif actual_pokemon.effectiveness(p) == selected.effectiveness(p) and actual_pokemon.hp != 0:
                    if actual_pokemon.level > selected.level:
                        selected = actual_pokemon
            # Devolvemos el pokemon seleccionado
            return selected
        else:
            # Si no hay pokemon disponibles, devolvemos False
            return None
