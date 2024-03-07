import pandas as pd


class BattleStats:
    '''
    Clase que almacena y calcula estadísticas de enfrentamientos entre pokémon.
    '''

    def __init__(self):
        '''
        Inicializa una instancia de la clase BattleStats.
        '''
        self.data_individual = []
        self.data_type = []
        self.data_type_type = []

    def store_data(self, attacker, defender, damage, healing):
        '''
        Almacena los datos de un enfrentamiento entre dos pokémon.

        Parameters 
        ----------
        - attacker (Pokemon): El pokémon atacante.
        - defender (Pokemon): El pokémon defensor.
        - damage (float): El daño infligido por el atacante.
        - healing (float): La cantidad de curación realizada por el atacante.
        '''
        # Individual -> [Nombre, Daño, Curación]
        self.data_individual.append([attacker.name, damage, healing])
        # Tipo -> [Tipo, Daño, Curación]
        self.data_type.append([attacker.pokemon_type, damage, healing])
        # Tipo vs Tipo -> [Tipo Atacante, Tipo Defensor, Daño]
        self.data_type_type.append(
            [attacker.pokemon_type, defender.pokemon_type, damage])

    def calculate_stats(self):
        '''
        Calcula las estadísticas de los enfrentamientos almacenados.

        Returns 
        -------
        tuple: Una tupla que contiene tres DataFrames:
            - individual_pokemons_grouped: Estadísticas agrupadas por pokémon individual.
            - type_pokemons_grouped: Estadísticas agrupadas por tipo de pokémon.
            - type_vs_type_grouped: Estadísticas agrupadas por tipo de pokémon atacante y tipo de pokémon defensor.
        '''
        # Pokemons individuales
        individual_pokemons = pd.DataFrame(self.data_individual, columns=[
                                           "Pokemon", "Avg Damage", "Avg Healing"])
        individual_pokemons_grouped = individual_pokemons.groupby("Pokemon").agg(
            {"Avg Damage": ["mean", "std"], "Avg Healing": ["mean", "std"]}).round(2).fillna(0)
        # Tipos de pokemons
        type_pokemons = pd.DataFrame(self.data_type, columns=[
                         "Type", "Avg Damage", "Avg Healing"])
        type_pokemons_grouped = type_pokemons.groupby("Type").agg({"Avg Damage": ["mean", "std"], "Avg Healing": ["mean", "std"]}).round(2).fillna(0)
        # Tipos de pokemons vs tipos de pokemons
        type_vs_type = pd.DataFrame(self.data_type_type, columns=[
                                    "Attacker", "Defender", "Avg Damage"])
        type_vs_type_grouped = type_vs_type.groupby(["Attacker", "Defender"]).agg(
            {"Avg Damage": ["mean", "std"]}).round(2).fillna(0)

        return individual_pokemons_grouped, type_pokemons_grouped, type_vs_type_grouped
