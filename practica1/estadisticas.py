import pandas
import numpy
'''
cambiarlo a en vez de numeros a listas, por eso no funciona
'''
data = {
    "Fire": {"Fire": 0, "Water": 0, "Grass": 0, "Damage": 0, "Healing": 0, "Counter Type": 0},
    "Water": {"Fire": 0, "Water": 0, "Grass": 0, "Damage": 0, "Healing": 0, "Counter Type": 0},
    "Grass": {"Fire": 0, "Water": 0, "Grass": 0, "Damage": 0, "Healing": 0, "Counter Type": 0}
}


def update_damage(attacker, defender, damage, healing=0):
    data[attacker.pokemon_type]["Damage"] += damage
    data[attacker.pokemon_type]["Healing"] += healing
    data[attacker.pokemon_type]["Counter Type"] += 1
    data[attacker.pokemon_type][defender.pokemon_type] += damage
    data.setdefault(
        attacker.name, {"Damage": damage, "Healing": healing, "Counter Indv": + 1})


def stats():
    '''
     (3) el daño promedio que cada tipo de Pokémon inflige acada uno de los otros tipos, 
    '''
    col = ["Fire", "Water", "Grass"]
    df = pandas.DataFrame(index=col, columns=[
                          "Avg Damage", "Std Damage", "Avg Heal", "Std Heal"])
    df1 = pandas.DataFrame(columns=[
                           "Avg Damage", "Std Damage", "Avg Heal", "Std Heal"])

    average_damage_type = {}
    average_heal_type = {}
    std_damage_type = {}
    std_heal_type = {}

    for t in col:
        total_damage = [data[t][defender] for defender in col]
        total_heal = [data[t]["Healing"] for _ in data]
        total_interactions = data[t]["Counter Type"]
        average_damage_type[t] = round(
            sum(total_damage) / total_interactions, 3)
        average_heal_type[t] = round(sum(total_heal) / total_interactions, 3)
        std_damage_type[t] = round(numpy.std(total_damage), 3)
        std_heal_type[t] = round(numpy.std(total_heal), 3)

    average_damage_tt = {}
    average_heal_tt = {}
    std_damage_tt = {}
    std_heal_tt = {}
    for attacker in col:
        for defender in col:
            total_damage = data[attacker][defender]
            total_heal = data[attacker]["Healing"]
            total_interactions = data[attacker]["Counter Type"]
            average_damage_tt[(attacker, defender)] = round(
                total_damage / total_interactions, 3)
            average_heal_tt[(attacker, defender)] = round(
                total_heal / total_interactions, 3)
            std_damage_tt[(attacker, defender)] = round(
                numpy.std(total_damage), 3)
            std_heal_tt[(attacker, defender)] = round(numpy.std(total_heal), 3)

    average_damage_indv = {}
    average_heal_indv = {}
    std_damage_indv = {}
    std_heal_indv = {}
    for i in data.keys():
        if i in col:
            continue
        total_interactions = data[i]["Counter Indv"]
        average_damage_indv[i] = round(
            data[i]["Damage"] / total_interactions, 3)
        average_heal_indv[i] = round(
            data[i]["Healing"] / total_interactions, 3)
        std_damage_indv[i] = round(numpy.std(total_damage), 3)
        std_heal_indv[i] = round(numpy.std(total_heal), 3)

    for i in col:
        df.loc[i, "Avg Damage"] = average_damage_type[i]
        df.loc[i, "Std Damage"] = std_damage_type[i]
        df.loc[i, "Avg Heal"] = average_heal_type[i]
        df.loc[i, "Std Heal"] = std_heal_type[i]

    for key in average_damage_indv:
        df.loc[key, "Avg Damage"] = average_damage_indv[key]
        df.loc[key, "Std Damage"] = std_damage_indv[key]
        df.loc[key, "Avg Heal"] = average_heal_indv[key]
        df.loc[key, "Std Heal"] = std_heal_indv[key]

    '''for key in average_damage_tt.keys():
        attacker, defender = key
        print(attacker, defender)
        
        df1.loc[key, "Avg Damage"] = average_damage_tt[key]
        df1.loc[key, "Std Damage"] = std_damage_tt[key]
        df1.loc[key, "Avg Heal"] = average_heal_tt[key]
        df1.loc[key, "Std Heal"] = std_heal_tt[key]'''
    # df_combined = pandas.concat([df1, df2], axis=1)
    print(df)
    print(average_damage_tt)
