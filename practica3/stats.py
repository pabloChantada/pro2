'''
Pablo Chantada Saborido | pablo.chantada@udc.es
Pablo Verdes Sánchez | p.verdess@udc.es
'''

import pandas as pd

class Statistics:
    '''
    Clase para realizar cálculos estadísticos y visualizar los resultados.

    Methods
    -------
    - show_films(data): Muestra todas las peliculas del archivo.
    - by_director(data, director_entry): Muestra todas las peliculas de un director.
    - by_year(data, year_entry): Muestra todas las peliculas de un director.
    - metrics(data): Muestra mean y std de: peliculas por director, calificacion por director
    y año.
    '''
    
    def show_films(data):
        '''
        Guarda todas las peliculas en un DataFrame
        
        Parameters
        ----------
        data(list): lista de datos para generar el DataFrame
        '''
        df = pd.DataFrame([
            {
                'Director': pelicula.director,
                'Título': pelicula.title,
                'Año': pelicula.year,
                'Calificación': pelicula.rating
            }
            for pelicula in data
        ])
        return df

    def by_director(data, director_entry):
        '''
        Guarda todas las peliculas por director en un DataFrame
        
        Parameters
        ----------
        data(list): lista de datos para generar el DataFrame
        director_entry(str): nombre del director
        '''
        
        df = Statistics.show_films(data)
        # Obtenemos los datos por director especifico
        filtered_df = df[df["Director"] == director_entry]
        if filtered_df.empty:
            return f"El director {director_entry} no tiene peliculas en el archivo"
        return filtered_df

    def by_year(data, year_entry):
        '''
        Guarda todas las peliculas por año en un DataFrame
        
        Parameters
        ----------
        data(list): lista de datos para generar el DataFrame
        year_entry(int): año de estreno
        
        '''
        
        df = Statistics.show_films(data)
        # Obtenemos los datos por año especifico
        filtered_df = df[df["Año"] == int(year_entry)]
        if filtered_df.empty:
            return f"El año {year_entry} no tiene peliculas en el archivo"
        return filtered_df

    def metrics(data):
        '''
        Guarda las metricas (mean/std) de:
        - Peliculas por director
        - Calificacion por director
        - Calificacion por año
        Se guardan en un DataFrame
        
        Parameters
        ----------
        data(list): lista de datos para generar el DataFrame
        '''
        
        df = Statistics.show_films(data)

        # Calcular el conteo por director
        df1 = df.groupby("Director").size().reset_index(name='Nº Peliculas')
        # Calcular la media y desviación estándar de las calificaciones por director
        df2 = df.groupby("Director")["Calificación"].agg(["mean", "std"]).round(2).reset_index().fillna(0)
        # Calcular la media y desviación estándar de las calificaciones por año
        df3 = df.groupby("Año")["Calificación"].agg(["mean"]).round(2).reset_index().fillna(0)
        
        return df1, df2, df3