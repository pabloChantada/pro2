'''
Pablo Chantada Saborido | pablo.chantada@udc.es
Pablo Verdes Sánchez | p.verdess@udc.es
'''

import pandas as pd

class Statistics:
    '''
    Clase que calcula estadísticas de un arbol AVL.
    '''
    def avl_to_list(tree):
        '''
        Convierte un árbol AVL en una lista de listas conteniendo información de cada curso.
        
        Parameters 
        ----------
        - tree (AVL): El árbol AVL que contiene los nodos con datos del curso.
        
        Returns 
        -------
        - list: Una lista de listas, donde cada sublista contiene datos de un curso específico:
        [nombre, duración, número de estudiantes, nivel, idioma, precio].
        '''
        data = []
        for i in tree:
            data.append([
                tree[i].name,
                tree[i].duration,
                tree[i].students,
                tree[i].level,
                tree[i].language,
                tree[i].price,
            ])
        return data
    
    def mean_language(tree):
        '''
        Calcula la media y la desviación estándar del número de estudiantes agrupados por idioma.
        
        Parameters 
        ----------
        - tree (AVL): El árbol AVL de donde se extraerán los datos.
        
        Returns 
        -------
        - DataFrame: Un DataFrame de Pandas con la media y desviación estándar de estudiantes por idioma.
        '''
        # Formateamos el arbol para poder trabajar con los dataframes
        formatted_data = Statistics.avl_to_list(tree)
        df = pd.DataFrame(formatted_data, columns=['name', 'duration', 'students', 'level', 'language', 'price'])
        # Agrupamos: numero medio de alumnos por idioma 
        result = df.groupby('language')['students'].agg(['mean', 'std']).round(2).fillna(0)
        # Mostramos el resultado y lo devolvemos
        print(result)
        return result

    def mean_level(tree):
        '''
        Calcula la media y la desviación estándar del número de estudiantes agrupados por nivel.
        
        Parameters 
        ----------
        - tree (AVL): El árbol AVL de donde se extraerán los datos.
        
        Returns 
        -------
        - DataFrame: Un DataFrame de Pandas con la media y desviación estándar de estudiantes por nivel.
        '''
        # Formateamos el arbol para poder trabajar con los dataframes
        formatted_data = Statistics.avl_to_list(tree)
        df = pd.DataFrame(formatted_data, columns=['name', 'duration', 'students', 'level', 'language', 'price'])
        # Agrupamos: numero medio de alumnos por nivel
        result = df.groupby('level')['students'].agg(['mean', 'std']).round(2).fillna(0)
        # Mostramos el resultado y lo devolvemos
        print(result)
        return result

    
    def total_income(tree):
        '''
        Calcula el ingreso total generado por todos los cursos en el árbol.
        
        Parameters 
        ----------
        - tree (AVL): El árbol AVL de donde se extraerán los datos.
        
        Returns 
        -------
        - float: El ingreso total -> producto del precio, número de estudiantes y duración de cada curso.
        '''
        # Formateamos el arbol para poder trabajar con los dataframes
        formatted_data = Statistics.avl_to_list(tree)
        # Create DataFrame with appropriate column names
        df = pd.DataFrame(formatted_data, columns=['name', 'duration', 'students', 'level', 'language', 'price'])
        # Calculamos los ingresos totales posibles
        df['total_income'] = df['price'] * df['students'] * df['duration']
        total_revenue = df['total_income'].sum()
        # Mostramos el resultado y lo devolvemos
        print(f"Total revenue: {total_revenue}")
        return total_revenue

    