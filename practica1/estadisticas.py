import pandas
import numpy

'''
Pablo Chantada Saborido | pablo.chantada@udc.es
Pablo Verdes Sánchez | p.verdess@udc.es
'''

# Datos de tipo vs tipo
type_type_data = {
    "Fire": {"Fire": [], "Water": [], "Grass": []},
    "Water": {"Fire": [], "Water": [], "Grass": []},
    "Grass": {"Fire": [], "Water": [], "Grass": []}
}

# Datos de tipo
type_data = {
    "Fire": {"Damage": [], "Healing": []},
    "Water": {"Damage": [], "Healing": []},
    "Grass": {"Damage": [], "Healing": []}
}
# Datos individuales
indv_data = {}


def stats_indv(attacker, damage, healing=0):
    '''
    Registra las estadísticas de daño y curación para un atacante individual.

    Parameters 
    ----------
    attacker(object): pokemon que ataca.
    damage(int): daño infligido por el atacante.
    healing(int): curación realizada por el atacante. 0 por defecto.
    '''
    # Si el atacante no está en el diccionario, lo agregamos
    if attacker.name not in indv_data:
        indv_data.setdefault(
            attacker.name, {"Damage": [damage], "Healing": [healing]})
    # Si el atacante ya está en el diccionario, actualizamos sus datos
    else:
        indv_data[attacker.name]["Damage"].append(damage)
        indv_data[attacker.name]["Healing"].append(healing)


def stats_type(attacker, damage, healing=0):
    '''
    Registra las estadísticas de daño y curación para un atacante
    según su tipo de Pokémon.

    Parameters 
    ----------
    attacker(object): pokemon que ataca.
    damage(int): daño infligido por el atacante.
    healing(int): curación realizada por el atacante. 0 por defecto.
    '''
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
    '''
    Registra las estadísticas de daño y curación para un atacante según su tipo
    de Pokémon y el tipo del defensor.

    Parameters 
    ----------
    attacker(object): pokemon que ataca.
    damage(int): daño infligido por el atacante.
    healing(int): curación realizada por el atacante. 0 por defecto.
    '''
    #"attacker.pokemon_type": {"defender.pokemon_type": []}
    # "Fire": {"Fire": [], "Water": [], "Grass": []},
    type_type_data[attacker.pokemon_type][defender.pokemon_type].append(damage)


def update_damage(attacker, defender, damage, healing=0):
    '''
    Actualiza las estadísticas de daño para un atacante. 

    Parameters 
    ----------
    attacker(object): pokemon que ataca.
    defender(object): pokemon que defiende.
    damage(int): daño infligido por el atacante.
    healing(int): curación realizada por el atacante. 0 por defecto.

    Esta función actualiza las estadísticas individuales, de tipo y tipo vs tipo.
    En el caso de Tipo vs Tipo se utiliza el defensor para registrar el daño 
    infligido por el atacante.
    '''
    # Estadísticas individuales
    stats_indv(attacker, damage, healing)
    # Estadísticas por tipo
    stats_type(attacker, damage, healing)
    # Estadísticas por tipo vs tipo
    stats_type_type(attacker, defender, damage)


def mean(data):
    '''
    Calcula la media de una lista de datos.

    Parameters 
    ----------
    - data: una lista de números.

    Returns 
    -------
    La media de los números en la lista. Si la lista está vacía, retorna 0.
    '''
    # Si la lista no está vacía, calculamos la media
    return numpy.mean(data) if len(data) > 0 else 0


def std(data):
    '''
    Calcula la deviación estandar de una lista de datos.

    Parameters 
    ----------
    - data: una lista de números.

    Returns 
    -------
    La desviación estandar de los números en la lista. 
    Si la lista está vacía, retorna 0.
    '''
    # Si la lista no está vacía, calculamos la std
    return numpy.std(data) if len(data) > 0 else 0


def stats():
    '''
    Calcula las estadisticas individuales, de Tipo y Tipo vs Tipo de las batallas.

    La función crea y muestra cuatro DataFrames que contienen las siguientes estadísticas:
    - df_indv: promedio de daño, promedio de curación, desviación estándar de daño y desviación estándar de curación para cada individuo.
    - df_type: promedio de daño, promedio de curación, desviación estándar de daño y desviación estándar de curación para cada tipo.
    - df_type_type_mean: promedio de daño para Tipo vs Tipo.
    - df_type_type_std: desviación estándar de daño para Tipo vs Tipo.

    Los datos utilizados para calcular las estadísticas deben estar en los diccionarios indv_data, type_data y type_type_data.
    '''
    # Filas de los dataframes
    indexes = ["Avg Damage", "Avg Healing", "Std Damage", "Std Healing"] # Individuales y tipo
    index_type_type = ["Fire", "Water", "Grass"]                         # Tipo vs Tipo
    
    df_indv = pandas.DataFrame(indv_data, indexes)
    df_type = pandas.DataFrame(type_data, indexes)
    # Hacemos los dataframes de tipo vs tipo cuadrados para una mejor representación
    df_type_type_mean = pandas.DataFrame(type_type_data, index_type_type, index_type_type)
    df_type_type_std = pandas.DataFrame(type_type_data, index_type_type, index_type_type)

    # Recorremos cada par clave-valor del diccionario correspondiente y calculamos las estadísticas
    # añadiendo los resultados a los dataframes
    
    # DATAFRAME INDIVIDUAL
    for key, value in indv_data.items():
        # Avg Damage, Avg Healing, Std Damage, Std Healing
        df_indv[key] = [round(mean(value['Damage']), 2),
                        round(mean(value['Healing']), 2),
                        round(std(value['Damage']), 2), 
                        round(std(value['Healing']), 2)]
    # DATAFRAME TIPO
    for key, value in type_data.items():
        # Avg Damage, Avg Healing, Std Damage, Std Healing
        df_type[key] = [round(mean(value['Damage']), 2),
                        round(mean(value['Healing']), 2), 
                        round(std(value['Damage']), 2),
                        round(std(value['Healing']), 2)]
    # DATAFRAME TIPO VS TIPO (solo se calcula el daño)
    for key, value in type_type_data.items():
        # Media del daño para cada tipo de atacante vs cada tipo de defensor
        df_type_type_mean[key] = [round(mean(value['Fire']), 2),
                                round(mean(value['Water']), 2),
                                round(mean(value['Grass']), 2)]
        # Desviación estándar del daño para cada tipo de atacante vs cada tipo de defensor
        df_type_type_std[key] = [round(std(value['Fire']), 2),
                                round(std(value['Water']), 2),
                                round(std(value['Grass']), 2)]
    # Mostramos los dataframes
    print("\nIndividual Data\n-----------------------\n",df_indv)
    print("\nType Data\n-----------------------\n",df_type)
    print("\nType vs Type Standart Deviation\n-----------------------\n",df_type_type_std)
    print("\nType vs Type Mean\n-----------------------\n",df_type_type_mean)