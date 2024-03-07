import pandas as pd
import sys
import pokemon
import trainer

'''
Pablo Chantada Saborido | pablo.chantada@udc.es
Pablo Verdes Sánchez | p.verdess@udc.es
'''

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

class PokemonSimulator:
    '''A class that simulates Pokemon trainers and their Pokemon.'''

    def create_trainer_and_pokemons(self, text: str):
        '''
        Creates a trainer and their pokemons from a given text input.

        Parameters
        ---------- 
        text (str): Multiline text where the first line is the trainer's name and subsequent lines contain Pokemon details.

        Returns 
        -------
        Trainer: returns an instance of Trainer for each trainer in the text.
        '''

        lines = text.split("\n")
        trainer_name = lines[0]
        pokemons = []

        # Iterating over each pokemon line in the input
        for line in lines[1:]:
            parts = line.split(' (')
            pokemon_name = parts[0]  # Extracting the pokemon's name
            details = parts[1].strip(')').split(
                ', ')  # Splitting other attributes
            # Extracting and converting each attribute
            pokemon_type = details[0].split(': ')[1]
            level = int(details[1].split(': ')[1])
            strength = int(details[2].split(': ')[1])
            defense = int(details[3].split(': ')[1])
            hp = int(details[4].split(': ')[1])
            total_hp = hp  # Setting total_hp equal to the initial hp
            agility = int(details[5].split(': ')[1])
            # Creating pokemons based on their type
            if pokemon_type == 'Fire':
                temperature = float(details[6].split(': ')[1])
                pokemons.append(pokemon.FirePokemon(
                    pokemon_name, level, strength, defense, hp, total_hp, agility, temperature))

            elif pokemon_type == 'Grass':
                healing = float(details[6].split(': ')[1])
                pokemons.append(pokemon.GrassPokemon(
                    pokemon_name, level, strength, defense, hp, total_hp, agility, healing))

            elif pokemon_type == 'Water':
                surge_mode = False
                pokemons.append(pokemon.WaterPokemon(
                    pokemon_name, level, strength, defense, hp, total_hp, agility, surge_mode))

            else:
                raise ValueError(f"Invalid Pokemon type: {pokemon_type}")

        trainer_complete = trainer.Trainer(trainer_name, pokemons)
        return trainer_complete

    def parse_file(self, text: str):
        '''
        Parses the given text to create trainers and their pokemons.

        Parameters
        ----------
        text (str): The full text to be parsed, representing two trainers and their Pokemon.

        Returns 
        -------
        Trainer: returns an instance of Trainer for each trainer in the text.
        '''

        info_trainer_1, info_trainer_2 = text.strip().split("\n\n")

        trainer1 = self.create_trainer_and_pokemons(info_trainer_1)
        trainer2 = self.create_trainer_and_pokemons(info_trainer_2)

        return trainer1, trainer2

def special_attacks(attacker, defender):
    '''
    Realiza ataques especiales basados en el tipo de Pokémon del atacante.

    Parameters
    ----------
    - attacker (Pokemon): El objeto Pokémon atacante.
    - defender (Pokemon): El objeto Pokémon defensor.
    '''
    
    match attacker.pokemon_type:
        case "Fire":
            damage = attacker.fire_attack(defender)
            # Seteamos el daño del segundo ataque a 0 incialmente
            damage2 = 0
            print(f"{attacker.name} usa un ataque de fuego en {defender.name}! (Daño: -{damage} HP: {defender.hp})\n")
            # Si el defensor no esta debilitado, realizamos el segundo ataque
            if defender.is_debilitated() != True:
                damage2 = attacker.embers(defender)
                print(f"{attacker.name} usa brasas en {defender.name}! (Daño: -{damage2} HP: {defender.hp})\n")
            # Guardamos los datos de la batalla
            battle_stats.store_data(attacker, defender, damage, healing=0)

        case "Water":
            damage = attacker.water_attack(defender)
            print(f"{attacker.name} uses a water_attack on {defender.name}! (Damage: -{damage} HP: {defender.hp})\n")
            # Guardamos los datos de la batalla
            battle_stats.store_data(attacker, defender, damage, healing=0)
            
        case "Grass":
            damage = attacker.grass_attack(defender)
            # Curamos al atacante
            healing = attacker.heal()
            print(f"{attacker.name} uses a grass_attack on {defender.name}! (Damage: -{damage} HP: {defender.hp})\n")
            # Mostramos el mensaje de curación
            print(f"{attacker.name} is healing! (Healing: +{healing} HP: {attacker.hp})\n")
            # Guardamos los datos de la batalla
            battle_stats.store_data(attacker, defender, damage, healing)


def normal_attacks(attacker, defender):
    '''
    Realiza un ataque normal del atacante al defensor.

    Parameters
    ----------
    - attacker: El objeto que realiza el ataque.
    - defender: El objeto que recibe el ataque.
    '''

    damage = attacker.basic_attack(defender)
    print(f"{attacker.name} usa un ataque básico en {defender.name}! (Daño: -{damage} HP: {defender.hp})\n")
    # Guardamos los datos de la batalla
    battle_stats.store_data(attacker, defender, damage, healing=0)


def determine_attacker_defender(p1, p2):
    '''
    Determina que Pokemon ataca primero segun su agilidad.
    
    Parameters
    ----------
    p1 (Pokemon): El Pokemon del primer entrenador.
    p2 (Pokemon): El Pokemon del segundo entrenador.
    
    Returns 
    -------
    Pokemon, Pokemon: El Pokemon que ataca primero y el que defiende.
    '''
    # Seteamos el Pokemon del primer entrenador como atacante y el del segundo como defensor incialmente
    attacker = p1
    defender = p2
    
    # Si el Pokemon del segundo entrenador tiene mayor agilidad, lo seteamos como atacante y el del primer entrenador como defensor
    if p2.agility > p1.agility:
        attacker = p2
        defender = p1
        
    return attacker, defender

def perform_round(attacker, defender, round_counter):
    '''
    Realiza una ronda con los Pokemons actuales. Se realiza un ataque especial si el contador de rondas es impar, y un ataque normal si es par.
    
    Parameters
    ----------
    attacker (Pokemon): El Pokemon que ataca.
    defender (Pokemon): El Pokemon que defiende.
    round_counter (int): El contador de rondas.
    
    Returns 
    -------
    bool: True si uno de los Pokemon es debilitado, False en caso contrario.
    '''
    # Si el contador de rondas es impar, se realiza un ataque especial.
    if round_counter % 2 != 0:
        # Realizamos el ataque especial del atacante
        special_attacks(attacker, defender)
        # Indicamos si el defensor esta debilitado
        if defender.is_debilitated() == True:
            print(f"{defender.name} is debilitated\n")
            return True
        # Realizamos el ataque especial del defensor
        special_attacks(defender, attacker)
        # Indicamos si el atacante esta debilitado
        if attacker.is_debilitated() == True:
            print(f"{attacker.name} is debilitated\n")
            return True
    # Sino, se realiza un ataque normal.
    else:
        # Realizamos el ataque normal del atacante
        normal_attacks(attacker, defender)
        # Indicamos si el defensor esta debilitado
        if defender.is_debilitated() == True:
            print(f"{defender.name} is debilitated\n")
            return True
        # Realizamos el ataque normal del defensor
        normal_attacks(defender, attacker)
        # Indicamos si el atacante esta debilitado
        if attacker.is_debilitated() == True:
            print(f"{attacker.name} is debilitated\n")
            return True
    return False

def fight(p1, p2):
    '''
    Realizamos la pelea entre dos Pokemons. La pelea termina si uno de los Pokemons es debilitado.
    
    Parameters
    ----------
    p1 (Pokemon): El Pokemon del primer entrenador.
    p2 (Pokemon): El Pokemon del segundo entrenador.
    '''
    # Seteamos el contador de rondas en 0
    round_counter = 0
    # Mientras ninguno de los Pokemons este debilitado, realizamos una ronda
    while p1.is_debilitated() == False and p2.is_debilitated() == False:
        round_counter += 1
        print(f"\n┌───────── Round {round_counter} ─────────┐")
        print(f"Fighter 1: {p1}")
        print(f"Figther 2: {p2}\n")
        # Determinamos el atacante y el defensor
        attacker, defender = determine_attacker_defender(p1, p2)
        # Mientras que perform_round no devuelva nada (es decir, mientras que ninguno de los Pokemons este debilitado), seguimos realizando rondas
        if perform_round(attacker, defender, round_counter):
            True

def main():
    '''
    La función principal que lee de un archivo y comienza la simulación.
    '''

    with open(sys.argv[1]) as f:
        pokemon_text = f.read()
        simulator = PokemonSimulator()
        trainer1, trainer2 = simulator.parse_file(pokemon_text)

        # Seleccionamos los primeros Pokemons de cada entrenador
        p1 = trainer1.select_first_pokemon()
        p2 = trainer2.select_first_pokemon()
        # Mientras los entrenadores tengan Pokemons disponibles, seguimos realizando batallas
        while trainer1.all_debilitated() == False and trainer2.all_debilitated() == False:
            print(f"\n\n================================= Battle between: {trainer1.name} vs {trainer2.name} begins!  {trainer1.name} chooses {p1.name} | {trainer2.name} chooses {p2.name} =================================")
            # Realizamos una batalla entre los Pokemons actuales
            fight(p1, p2)
            # Si el Pokemon del primer entrenador esta debilitado, seleccionamos el siguiente Pokemon
            if p1.is_debilitated() == True:
                p1 = trainer1.select_next_pokemon(p2)
                # Si no hay mas Pokemons disponibles, terminamos la batalla
                if p1 is None:
                    break
                print(f"{trainer1.name} chooses {p1.name}")
                
            # Si el Pokemon del segundo entrenador esta debilitado, seleccionamos el siguiente Pokemon
            elif p2.is_debilitated() == True:
                p2 = trainer2.select_next_pokemon(p1)
                # Si no hay mas Pokemons disponibles, terminamos la batalla
                if p2 is None:
                    break
                print(f"{trainer2.name} chooses {p2.name}")

        # Seteamos el primer entrenador como ganador inicial
        winner = trainer1
        # Si los pokemons del primer entrenador estan debilitados, el segundo entrenador es el ganador
        if trainer1.select_first_pokemon == None:
            winner = trainer2
        
        print(f"=================================\
                End of the Battle: {winner.name} wins!\
                =================================")


if __name__ == '__main__':
    
    # Creamos una instancia de BattleStats
    battle_stats = BattleStats()
    # Ejecutamos las battallas
    main()
    # Calcular las estadísticas
    individual_stats, type_stats, type_vs_type_stats = battle_stats.calculate_stats()

    # Mostrar las estadísticas
    print("\n##############################")
    print("   Individual statistics      ")
    print("##############################\n")
    print(individual_stats)
    print("\n##############################")
    print("   Type statistics      ")
    print("##############################\n")
    print(type_stats)
    print("\n##############################")
    print("   Type vs Type statistics      ")
    print("##############################\n")
    print(type_vs_type_stats)