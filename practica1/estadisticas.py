import pandas
import numpy
'''
cambiarlo a en vez de numeros a listas, por eso no funciona
3 datagramas por pantalla
'''
data = {
    "Fire": {"Fire": 0, "Water": 0, "Grass": 0, "Damage": 0, "Healing": 0, "Counter Type": 0},
    "Water": {"Fire": 0, "Water": 0, "Grass": 0, "Damage": 0, "Healing": 0, "Counter Type": 0},
    "Grass": {"Fire": 0, "Water": 0, "Grass": 0, "Damage": 0, "Healing": 0, "Counter Type": 0}
}

indv_data = {
    "Name": "",
    "Damage": []
}

type_data = {}  
type_type_data = {}

def update_damage(attacker, defender, damage, healing=0):
    '''
    Crear un dict por pokemon y como value tiene el daño por ronda
    '''
    if attacker.name in indv_data:
        indv_data["Damage"].append(damage)
    else:
        indv_data.update({"attacker.name", "damage"})
    #type_data[attacker.pokemon_type] = {"Damage": damage, "Healing": healing, "Counter Indv": + 1}
    #type_type_data[attacker.pokemon_type][defender.pokemon_type] = {"Fire": 0, "Water": 0, "Grass": 0, "Damage": 0, "Healing": 0, "Counter Type": 0}

def mean_indv(data):
    pass

def stats():
    
    df_indv = pandas.DataFrame()
    df_type = pandas.DataFrame(type_data)
    df_type_type = pandas.DataFrame(type_type_data)
    for i in range(len(indv_data)):
        print(indv_data)    
