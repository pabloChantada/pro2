from rich import print

from estadisticas import update_damage, stats
import sys
import pokemon
import trainer

class PokemonSimulator:
    """A class that simulates Pokemon trainers and their Pokemon."""

    def create_trainer_and_pokemons(self, text: str):
        """
        Creates a trainer and their pokemons from a given text input.

        Parameters:
        text (str): Multiline text where the first line is the trainer's name and subsequent lines contain Pokemon details.

        Returns:
        None: The function is currently set up to return None. Intended to return a Trainer instance in future development.
        """

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
                # Printing the attributes for now
                # print (f"name: {pokemon_name}, level: {level}, strength: {strength}, defense: {defense}, hp: {hp}, total_hp: {total_hp}, agility: {agility}, temperature: {temperature} ")
            elif pokemon_type == 'Grass':
                healing = float(details[6].split(': ')[1])
                pokemons.append(pokemon.GrassPokemon(
                    pokemon_name, level, strength, defense, hp, total_hp, agility, healing))
                # Printing the attributes for now
                # print (f"name: {pokemon_name},  level: {level}, strength: {strength}, defense: {defense}, hp: {hp}, total_hp: {total_hp}, agility: {agility}, healing: {healing} ")
            elif pokemon_type == 'Water':
                surge_mode = False
                pokemons.append(pokemon.WaterPokemon(
                    pokemon_name, level, strength, defense, hp, total_hp, agility, surge_mode))
                # Printing the attributes for now
                # print (f"name: {pokemon_name}, level: {level}, strength: {strength}, defense: {defense}, hp: {hp}, total_hp: {total_hp}, agility: {agility}, surge_mode: {surge_mode} ")
            else:
                raise ValueError(f"Invalid Pokemon type: {pokemon_type}")

        # Reminder to implement the instance creation of Trainer
        trainer_complete = trainer.Trainer(trainer_name, pokemons)
        # Function is intended to return a Trainer instance in future development
        return trainer_complete

    def parse_file(self, text: str):
        """
        Parses the given text to create trainers and their pokemons.

        Parameters:
        text (str): The full text to be parsed, representing two trainers and their Pokemon.

        Returns:
        None: Currently does not return anything. Intended to return a list of Trainer instances in future development.
        """

        info_trainer_1, info_trainer_2 = text.strip().split("\n\n")

        trainer1 = self.create_trainer_and_pokemons(info_trainer_1)
        trainer2 = self.create_trainer_and_pokemons(info_trainer_2)

        return trainer1, trainer2


def special_attacks(attacker, defender, attacker_color, defender_color):
    match attacker.pokemon_type:
        case "Fire":
            damage = attacker.fire_attack(defender)
            damage2 = 0
            print(f"[{attacker_color}]{attacker.name}[/{attacker_color}] uses a fire_attack on [{defender_color}]{defender.name}[/{defender_color}]! (Damage: -{damage} HP: {defender.hp})\n")
            if defender.is_debilitated() != True:
                damage2 = attacker.embers(defender)
                print(f"[{attacker_color}]{attacker.name}[/{attacker_color}] uses embers on [{defender_color}]{defender.name}[/{defender_color}]! (Damage: -{damage2} HP: {defender.hp})\n")
            update_damage(attacker, defender, damage)

        case "Water":
            damage = attacker.water_attack(defender)
            print(f"[{attacker_color}]{attacker.name}[/{attacker_color}] uses a water_attack on [{defender_color}]{defender.name}[/{defender_color}]! (Damage: -{damage} HP: {defender.hp})\n")
            update_damage(attacker, defender, damage)
        case "Grass":
            damage = attacker.grass_attack(defender)
            healing = attacker.heal()
            print(f"[{attacker_color}]{attacker.name}[/{attacker_color}] uses a grass_attack on [{defender_color}]{defender.name}[/{defender_color}]! (Damage: -{damage} HP: {defender.hp})\n")
            print(f"[{attacker_color}]{attacker.name}[/{attacker_color}] is [bright_green]healing! (Healing: +{healing} HP: {attacker.hp}[/bright_green])\n")
            update_damage(attacker, defender, damage, healing)


def normal_attacks(attacker, defender, attacker_color, defender_color):

    damage = attacker.basic_attack(defender)
    print(f"[{attacker_color}]{attacker.name}[/{attacker_color}] uses a basic_attack on [{defender_color}]{defender.name}[/{defender_color}]! (Damage: -{damage} HP: {defender.hp})\n")
    update_damage(attacker, defender, damage)


def fight(p1, p2):
    round_counter = 0
    while p1.is_debilitated() == False and p2.is_debilitated() == False:
        round_counter += 1
        print(f"\n┌───────── Round {round_counter} ─────────┐")
        print(f"Fighter 1: [bright_blue]{p1}[/bright_blue]")
        print(f"Figther 2: [bright_red]{p2}[/bright_red]\n")
        p1_color = "bright_blue"
        p2_color = "bright_red"
        
        if p1.agility > p2.agility:
            attacker = p1
            defender = p2
        elif p2.agility > p1.agility:
            attacker = p2
            defender = p1
        else:
            attacker = p1
            defender = p2
            
        if round_counter % 2 != 0:
            # impares
            special_attacks(attacker, defender, p1_color, p2_color)
            if defender.is_debilitated() == True:
                print(f"[dark_red]{defender.name} is debilitated\n[/dark_red]")
                break
            special_attacks(defender, attacker, p2_color, p1_color)
            if attacker.is_debilitated() == True:
                print(f"[dark_red]{attacker.name} is debilitated\n[/dark_red]")
                break
        else:
            normal_attacks(attacker, defender, p1_color, p2_color)
            if defender.is_debilitated() == True:
                print(f"[dark_red]{defender.name} is debilitated\n[/dark_red]")
                break
            normal_attacks(defender, attacker, p2_color, p1_color)
            if attacker.is_debilitated() == True:
                print(f"[dark_red]{attacker.name} is debilitated\n[/dark_red]")
                break

def main():
    """
    The main function that reads from a file and starts the simulation.
    """

    with open(sys.argv[1]) as f:
        pokemon_text = f.read()
        simulator = PokemonSimulator()
        trainer1, trainer2 = simulator.parse_file(pokemon_text)

        p1 = trainer1.select_first_pokemon()
        p2 = trainer2.select_first_pokemon()
        print(f"\n\n================================= Battle between: [bright_red]{trainer1.name}[/bright_red] vs [bright_blue]{trainer2.name}[/bright_blue] begins!  [bright_red]{trainer1.name}[/bright_red] chooses [bright_red]{p1.name}[/bright_red] | [bright_blue]{trainer2.name}[/bright_blue] chooses [bright_blue]{p2.name}[/bright_blue] =================================")
        while trainer1.all_debilitated() == False and trainer2.all_debilitated() == False:
            fight(p1, p2)
            if p1.is_debilitated() == True:
                p1 = trainer1.select_next_pokemon(p2)
                if p1 is False:
                    break
                print("=================================")
                print(f"\n ================================= [bright_red]{trainer1.name}[/bright_red] chooses [bright_red]{p1.name}[/bright_red] =================================")

            elif p2.is_debilitated() == True:
                p2 = trainer2.select_next_pokemon(p1)
                if p2 is False:
                    break
                print(f"\n================================= [bright_blue]{trainer2.name}[/bright_blue] chooses [bright_blue]{p2.name}[/bright_blue] =================================")

        if trainer1.select_first_pokemon == None:
            winner = trainer2
        else:
            winner = trainer1
        print(f"=================================\
            End of the Battle: [green]{winner.name}[/green] wins!\
            =================================")


if __name__ == '__main__':
    main()
    stats()