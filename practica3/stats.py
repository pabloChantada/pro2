import pandas as pd
class Statistics:
    def show_films(data):
        loaded_data = pd.read_csv(data, sep=";")
        loaded_data.columns = ['Director', 'Título', 'Año', 'Calificación']
        return loaded_data

    def by_director(data, director_entry):
        loaded_data = pd.read_csv(data, sep=";")
        loaded_data.columns = ['Director', 'Título', 'Año', 'Calificación']
        filtered_data = loaded_data[loaded_data["Director"] == director_entry]
        if len(filtered_data) == 0:
            return f"El director {director_entry} no tiene peliculas en el archivo"
        return filtered_data

    def by_year(data, year_entry):
        loaded_data = pd.read_csv(data, sep=";")
        loaded_data.columns = ['Director', 'Título', 'Año', 'Calificación']
        filtered_data = loaded_data[loaded_data["Año"] == int(year_entry)]
        if len(filtered_data) == 0:
            return f"El año {year_entry} no tiene peliculas en el archivo"
        return filtered_data

    def metrics(data):
        loaded_data = pd.read_csv(data, sep=";")
        loaded_data.columns = ['Director', 'Título', 'Año', 'Calificación']
        # Calcular el conteo por director
        df1 = loaded_data.groupby("Director").size().reset_index(name='Nº Peliculas')
        # Calcular la media y desviación estándar de las calificaciones por director
        df2 = loaded_data.groupby("Director")["Calificación"].agg(["mean", "std"]).round(2).reset_index().fillna(0)
        # Calcular la media y desviación estándar de las calificaciones por año
        df3 = loaded_data.groupby("Año")["Calificación"].agg(["mean", "std"]).round(2).reset_index().fillna(0)
        
        return df1, df2, df3