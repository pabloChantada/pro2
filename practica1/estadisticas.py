import pandas
import numpy

type_type_data = {
    "Fire": {"Fire": [], "Water": [], "Grass": []},
    "Water": {"Fire": [], "Water": [], "Grass": []},
    "Grass": {"Fire": [], "Water": [], "Grass": []}
}

type_data = {
    "Fire": {"Damage": [], "Healing": []},
    "Water": {"Damage": [], "Healing": []},
    "Grass": {"Damage": [], "Healing": []}
}
indv_data = {}


def stats_indv(attacker, damage, healing=0):
    if attacker.name not in indv_data:
        indv_data.setdefault(
            attacker.name, {"Damage": [damage], "Healing": [healing]})
    else:
        indv_data[attacker.name]["Damage"].append(damage)
        indv_data[attacker.name]["Healing"].append(healing)


def stats_type(attacker, damage, healing=0):
    match attacker.pokemon_type:
        case "Fire":
            type_data["Fire"]["Damage"].append(damage)
            type_data["Fire"]["Healing"].append(healing)
        case "Grass":
            type_data["Grass"]["Damage"].append(damage)
            type_data["Grass"]["Healing"].append(healing)
        case "Water":
            type_data["Water"]["Damage"].append(damage)
            type_data["Water"]["Healing"].append(healing)


def stats_type_type(attacker, defender, damage):
    type_type_data[attacker.pokemon_type][defender.pokemon_type].append(damage)


def update_damage(attacker, defender, damage, healing=0):
    '''
    Crear un dict por pokemon y como value tiene el daño por ronda
    '''
    stats_indv(attacker, damage, healing)
    stats_type(attacker, damage, healing)
    stats_type_type(attacker, defender, damage)


def mean(data):
    return sum(data) / len(data) if len(data) > 0 else 0


def std(data):
    return numpy.std(data) if len(data) > 0 else 0


def stats():
    indexes = ["Avg Damage", "Avg Healing", "Std Damage", "Std Healing"]
    index_type_type = ["Fire vs Fire", "Fire vs Water", "Fire vs Grass",
                         "Water vs Fire", "Water vs Water", "Water vs Grass",
                         "Grass vs Fire", "Grass vs Water", "Grass vs Grass"]
    col_type_type = ["Avg Damage", "Std Damage"]
    df_indv = pandas.DataFrame(indv_data, indexes)
    df_type = pandas.DataFrame(type_data, indexes)
    df_type_type = pandas.DataFrame(type_type_data, index_type_type, col_type_type)

    for key, value in indv_data.items():
        df_indv[key] = [round(mean(value['Damage']), 2), round(mean(value['Healing']), 2), round(
            std(value['Damage']), 2), round(std(value['Healing']), 2)]

    for key, value in type_data.items():
        df_type[key] = [round(mean(value['Damage']), 2), round(mean(value['Healing']), 2), round(
            std(value['Damage']), 2), round(std(value['Healing']), 2)]
    for key, value in type_type_data.items():
        print(key,"--->", value)
        print(key,"--->", mean(value['Fire']))
        print(key,"--->", mean(value['Water']))
        print(key,"--->", mean(value['Grass']))        
        '''df_type_type[key] = \
            [round(mean(value['Fire']), 2), \
            round(mean(value['Water']), 2),\
            round(mean(value['Grass']), 2), \
            round(std(value['Fire']), 2), \
            round(std(value['Water']), 2), \
            round(std(value['Grass']), 2)]'''

    
    print(df_indv)
    print(df_type)
    print(df_type_type)
