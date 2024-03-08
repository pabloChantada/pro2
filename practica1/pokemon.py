from abc import ABC, abstractmethod
from math import floor

'''
Pablo Chantada Saborido | pablo.chantada@udc.es
Pablo Verdes Sánchez | p.verdess@udc.es
'''

class Pokemon(ABC):
    '''
    Clase abstracta que representa un Pokemon.

    Attributes
    ----------
    - name (str): El nombre del Pokemon.
    - level (int): El nivel del Pokemon.
    - strength (int): La fuerza del Pokemon.
    - defense (int): La defensa del Pokemon.
    - hp (int): Los puntos de vida actuales del Pokemon.
    - total_hp (int): Los puntos de vida totales del Pokemon.
    - agility (int): La agilidad del Pokemon.

    Methods
    -------
    basic_attack(self, opponent: 'Pokemon') -> int: calcula el ataque básico del Pokemon, según la defensa del Pokemon contrario.

    is_debilitated(self) -> bool: devuelve True si los puntos de vida del Pokemon son menores o iguales a 0.

    effectiveness(self, opponent: 'Pokemon') -> int: método abstracto que devuelve un string con las estadísticas el Pokemon.
    '''

    def __init__(self, name: str, level: int, strength: int, defense: int,
                 hp: int, total_hp: int, agility: int) -> None:
        '''
        Inicializa una instancia de la clase Pokemon.

        Attributes
        ---------
        - name (str): El nombre del Pokemon.
        - level (int): El nivel del Pokemon.
        - strength (int): La fuerza del Pokemon.
        - defense (int): La defensa del Pokemon.
        - hp (int): Los puntos de vida actuales del Pokemon.
        - total_hp (int): Los puntos de vida totales del Pokemon.
        - agility (int): La agilidad del Pokemon.

        '''
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
        return self._name

    @name.setter
    def name(self, value: str):
        if isinstance(value, str) and len(value) > 0:
            self._name = value
        else:
            raise ValueError("Name must be a non-empty string")

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, value: int):
        if isinstance(value, int) and value > 0:
            self._level = value
        else:
            raise ValueError("Level must be a positive number")

    @property
    def strength(self):
        return self._strength

    @strength.setter
    def strength(self, value: int):
        if isinstance(value, int) and value > 0:
            self._strength = value
        else:
            raise ValueError("Strength must be a positive number")

    @property
    def defense(self):
        return self._defense

    @defense.setter
    def defense(self, value: int):
        if isinstance(value, int) and value > 0:
            self._defense = value
        else:
            raise ValueError("Defense must be a number")

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, value: int):
        if isinstance(value, int) and value >= 0:
            self._hp = value
        else:
            raise ValueError("HP must be a positive number")

    @property
    def total_hp(self):
        return self._total_hp

    @total_hp.setter
    def total_hp(self, value: int):
        if isinstance(value, int) and value > 0:
            self._total_hp = value
        else:
            raise ValueError("Total HP must be a positive number")

    @property
    def agility(self):
        return self._agility

    @agility.setter
    def agility(self, value: int):
        if isinstance(value, int) and value > 0:
            self._agility = value
        else:
            raise ValueError("Agility must be a positive number")

    @property
    def pokemon_type(self):
        return self._pokemon_type

    @pokemon_type.setter
    def pokemon_type(self, value: str):
        if isinstance(value, str) and len(value) > 0:
            self._pokemon_type = value
        else:
            raise ValueError("Pokemon Type must be a non-empty string")

    def basic_attack(self, opponent: 'Pokemon') -> int:
        '''
        Realiza un ataque básico al Pokemon oponente.

        Attributes
        ---------- 
        - opponent (Pokemon): El Pokemon oponente al que se va a atacar.

        Returns
        ------- 
        int: El daño causado al Pokemon oponente.
        '''
        # El daño minimo es 1, no se realizan daños negativos
        damage_dealt = floor(max(1, self.strength - opponent.defense))
        if (opponent.hp - damage_dealt) < 0:
            opponent.hp = 0
            return damage_dealt
        opponent.hp -= damage_dealt
        return damage_dealt

    def is_debilitated(self) -> bool:
        ''''
        Comprueba si el Pokémon está debilitado.

        Returns
        ------- 
        bool: True si el Pokémon está debilitado, False en caso contrario.
        '''
        if self.hp <= 0:
            return True
        return False

    @abstractmethod
    def effectiveness(self, opponent: 'Pokemon') -> int:
        raise NotImplementedError

    def __str__(self):
        '''
        Devuelve las estadisticas del Pokemon en forma de cadena de texto.

        Returns
        -------
        str: Cadena que representa al objeto Pokemon.
        '''
        return f"{self.name} ({self.pokemon_type}) Stats: Level: {self.level}, ATT: {self.strength}, DEF: {self.defense}, AGI: {self.agility}, HP: {self.hp}/{self.total_hp}."


class WaterPokemon(Pokemon):
    '''
    Clase del los Pokemon de tipo Agua.

    Parameters
    ----------
    - name (str): El nombre del Pokémon.
    - level (int): El nivel del Pokémon.
    - strength (int): La fuerza del Pokémon.
    - defense (int): La defensa del Pokémon.
    - hp (int): Los puntos de vida actuales del Pokémon.
    - total_hp (int): Los puntos de vida totales del Pokémon.
    - agility (int): La agilidad del Pokémon.
    - surge_mode (bool): Indica si el Pokémon está en modo de oleada.

    Methods
    ------- 
    water_attack(self, p: Pokemon) -> int: Realiza un ataque de agua a otro Pokémon.

    check_surge_activation(self) -> bool: Verifica si el Pokémon está en modo de oleada.

    effectiveness(self, opponent: Pokemon) -> int: Calcula la efectividad del ataque del Pokémon contra otro Pokémon según el tipo.
    '''

    def __init__(self, name: str, level: int, strength: int, defense: int,
                 hp: int, total_hp: int, agility: int, surge_mode: bool) -> None:
        '''
        Inicializa una instancia de WaterPokemon.

        Parameters
        ----------
        - name (str): El nombre del Pokémon.
        - level (int): El nivel del Pokémon.
        - strength (int): La fuerza del Pokémon.
        - defense (int): La defensa del Pokémon.
        - hp (int): Los puntos de vida actuales del Pokémon.
        - total_hp (int): Los puntos de vida totales del Pokémon.
        - agility (int): La agilidad del Pokémon.
        - surge_mode (bool): Indica si el Pokémon está en modo de oleada.

        '''
        super().__init__(name, level, strength, defense, hp, total_hp, agility)

        self.pokemon_type = "Water"
        self.surge_mode = surge_mode

    def water_attack(self, p: Pokemon) -> int:
        '''
        Realiza un ataque de agua a otro Pokémon.

        Parameters
        ---------- 
        - p (Pokemon): El Pokémon objetivo del ataque.

        Returns
        ------- 
        int: El daño infligido al Pokémon objetivo.
        '''
        # Factor multiplicativo del daño según el tipo del Pokémon objetivo
        match p.pokemon_type:
            case "Fire":
                factor = 1.5
            case "Water":
                factor = 1
            case "Grass":
                factor = 0.5
        # Si surge_mode es True, el factor se incrementa en 0.1
        if WaterPokemon.check_surge_activation(self) == True:
            self.surge_mode = True
            factor += 0.1
        else:
            self.surge_mode = False
        # El daño minimo es 1, no se realizan daños negativos
        damage_dealt = floor(max(1, (factor*self.strength)-p.defense))
        if (p.hp - damage_dealt) < 0:
            p.hp = 0
            return damage_dealt
        p.hp -= damage_dealt
        return damage_dealt

    def check_surge_activation(self) -> bool:
        '''
        Verifica si el Pokémon está en modo de oleada.

        Returns:
        bool: True si el Pokémon está en modo de oleada, False de lo contrario.
        '''
        # Si esta por debajo de la mitad de la vida se activa
        if self.hp < (self.total_hp/2):
            return True
        return False

    def effectiveness(self, opponent: Pokemon) -> int:
        '''
        Calcula la efectividad del ataque del Pokémon contra otro Pokémon según el tipo.

        Parameters
        ---------- 
        - opponent (Pokemon): El Pokémon objetivo del ataque.

        Returns
        ------- 
        int: El valor de efectividad del ataque.
        '''
        match opponent.pokemon_type:
            case "Fire":
                return 1
            case "Water":
                return 0
            case "Grass":
                return -1


class GrassPokemon(Pokemon):
    '''
    Clase del los Pokemon de tipo Planta.

    Parameters
    ----------
    - name (str): El nombre del Pokémon.
    - level (int): El nivel del Pokémon.
    - strength (int): La fuerza del Pokémon.
    - defense (int): La defensa del Pokémon.
    - hp (int): Los puntos de vida actuales del Pokémon.
    - total_hp (int): Los puntos de vida totales del Pokémon.
    - agility (int): La agilidad del Pokémon.
    - healing (float): La cantidad de curación que el Pokémon puede realizar.
    Si el Pokemon no perdio vida, no se cura.

    Methods
    ------- 
    grass_attack(self, p: Pokemon) -> int: Realiza un ataque de planta a otro Pokémon.

    heal(self) -> int: Realiza una curación subre si mismo.

    effectiveness(self, opponent: Pokemon) -> int: Calcula la efectividad del ataque del Pokémon contra otro Pokémon según el tipo.
    '''

    def __init__(self, name: str, level: int, strength: int, defense: int,
                 hp: int, total_hp: int, agility: int, healing: float) -> None:
        super().__init__(name, level, strength, defense, hp, total_hp, agility)
        '''
        Inicializa una instancia de GrassPokemon.

        Parameters
        ----------
        - name (str): El nombre del Pokémon.
        - level (int): El nivel del Pokémon.
        - strength (int): La fuerza del Pokémon.
        - defense (int): La defensa del Pokémon.
        - hp (int): Los puntos de vida actuales del Pokémon.
        - total_hp (int): Los puntos de vida totales del Pokémon.
        - agility (int): La agilidad del Pokémon.
        - healing (float): La cantidad de curación que el Pokémon puede realizar.
        '''

        self.pokemon_type = "Grass"
        self.healing = healing

    def grass_attack(self, p: Pokemon) -> int:
        '''
        Realiza un ataque de planta a otro Pokémon.

        Parameters
        ---------- 
        - p (Pokemon): El Pokémon objetivo del ataque.

        Returns
        ------- 
        int: El daño infligido al Pokémon objetivo.
        '''
        # Factor multiplicativo del daño según el tipo del Pokémon objetivo
        match p.pokemon_type:
            case "Fire":
                factor = 0.5
            case "Water":
                factor = 1.5
            case "Grass":
                factor = 1
        # El daño minimo es 1, no se realizan daños negativos
        damage_dealt = floor(max(1, (factor*self.strength)-p.defense))
        if (p.hp - damage_dealt) < 0:
            p.hp = 0
            return damage_dealt
        p.hp -= damage_dealt
        return damage_dealt

    def heal(self) -> int:
        '''
        Método que cura al Pokémon y devuelve la cantidad de puntos de salud curados. Al curar la vida del Pokemon no puede superar su total_hp.

        Returns
        -------
        int: La cantidad de puntos de salud curados.
        '''
        if self.hp == self.total_hp:
            return 0
        heal = floor(self.healing * self.hp)
        self.hp += heal
        # Evitamos que la vida del Pokemon supere su total_hp
        if self.hp > self.total_hp:
            self.hp = self.total_hp
        return heal

    def effectiveness(self, opponent: Pokemon) -> int:
        '''
        Calcula la efectividad del ataque del Pokémon contra otro Pokémon según el tipo.

        Parameters
        ---------- 
        - opponent (Pokemon): El Pokémon objetivo del ataque.

        Returns
        ------- 
        int: El valor de efectividad del ataque.
        '''
        match opponent.pokemon_type:
            case "Fire":
                return -1
            case "Water":
                return 1
            case "Grass":
                return 0


class FirePokemon(Pokemon):
    '''
    Clase del los Pokemon de tipo Fuego.

    Parameters
    ----------
    - name (str): El nombre del Pokémon.
    - level (int): El nivel del Pokémon.
    - strength (int): La fuerza del Pokémon.
    - defense (int): La defensa del Pokémon.
    - hp (int): Los puntos de vida actuales del Pokémon.
    - total_hp (int): Los puntos de vida totales del Pokémon.
    - agility (int): La agilidad del Pokémon.
    - temperature(float): La temperatura del Pokémon, que afecta a su ataque de ascuas.

    Methods
    ------- 
    fire_attack(self, p: Pokemon) -> int: Realiza un ataque de fuego a otro Pokémon.

    embers(self, p: Pokemon) -> int: Realiza un ataque de ascuas a otro Pokémon.

    effectiveness(self, opponent: Pokemon) -> int: Calcula la efectividad del ataque del Pokémon contra otro Pokémon según el tipo.
    '''

    def __init__(self, name: str, level: int, strength: int, defense: int,
                 hp: int, total_hp: int, agility: int, temperature: float) -> None:
        super().__init__(name, level, strength, defense, hp, total_hp, agility)
        '''
        Inicializa una instancia de FirePokemon.

        Parameters
        ----------
        - name (str): El nombre del Pokémon.
        - level (int): El nivel del Pokémon.
        - strength (int): La fuerza del Pokémon.
        - defense (int): La defensa del Pokémon.
        - hp (int): Los puntos de vida actuales del Pokémon.
        - total_hp (int): Los puntos de vida totales del Pokémon.
        - agility (int): La agilidad del Pokémon.
        - temperature(float): La temperatura del Pokémon, que afecta a su ataque de ascuas.
        '''
        self.pokemon_type = "Fire"
        self.temperature = temperature

    def fire_attack(self, p: Pokemon) -> int:
        '''
        Realiza un ataque de fuego a otro Pokémon.

        Parameters
        ---------- 
        - p (Pokemon): El Pokémon objetivo del ataque.

        Returns
        ------- 
        int: El daño infligido al Pokémon objetivo.
        '''
        # Factor multiplicativo del daño según el tipo del Pokémon objetivo
        match p.pokemon_type:
            case "Fire":
                factor = 1
            case "Water":
                factor = 0.5
            case "Grass":
                factor = 1.5
        # El daño minimo es 1, no se realizan daños negativos
        damage_dealt = floor(max(1, (factor*self.strength)-p.defense))
        if (p.hp - damage_dealt) < 0:
            p.hp = 0
            return damage_dealt
        p.hp -= damage_dealt
        return damage_dealt

    def embers(self, p: Pokemon) -> int:
        '''
        Calcula el daño causado por el ataque "embers" a un Pokémon objetivo. Se realiza después de un ataque de clase (fire_attack).

        Parámetros:
        - p: El Pokémon objetivo al que se le aplicará el ataque.

        Retorna:
        - El daño causado al Pokémon objetivo.
        '''

        damage_dealt = floor(self.strength * self.temperature)
        if (p.hp - damage_dealt) < 0:
            p.hp = 0
            return damage_dealt
        p.hp -= damage_dealt
        return damage_dealt

    def effectiveness(self, opponent: Pokemon) -> int:
        '''
        Calcula la efectividad del ataque del Pokémon contra otro Pokémon según el tipo.

        Parameters
        ---------- 
        - opponent (Pokemon): El Pokémon objetivo del ataque.

        Returns
        ------- 
        int: El valor de efectividad del ataque.
        '''
        match opponent.pokemon_type:
            case "Fire":
                return 0
            case "Water":
                return -1
            case "Grass":
                return 1
