'''
Pablo Chantada Saborido | pablo.chantada@udc.es
Pablo Verdes Sánchez | p.verdess@udc.es
'''

import sys
import pandas as pd
import matplotlib.pyplot as plt
from classes import Process, ManagerQueue
from array_queue import ArrayQueue

class Statistics():
    '''
    Clase para realizar cálculos estadísticos y visualizar los resultados.

    Methods
    -------
    - penalization_mean: Calcula el número de penalizaciones por usuario.
    - show_penalization_mean: Muestra un gráfico de barras con las penalizaciones agrupadas por usuario.
    - stay_mean: Calcula el tiempo de espera promedio por tipo de cola.
    - show_stay_mean: Muestra un gráfico de barras con los tiempos de espera promedio por tipo de cola.
    '''
    
    def penalization_mean(self, data):
        '''
        Calcula el número de penalizaciones por usuario.

        Parameters
        ----------
        - data: Lista de listas con los datos de penalización por usuario.

        Returns
        -------
        - penalization_count: DataFrame con el número de penalizaciones por usuario.
        '''
        # Generamos el dataframe con los datos de penalización por usuario
        df = pd.DataFrame(data, columns=["User", "Penalization"])
        # Agrupamos por usuario y mostramos la media y la suma de las penalizaciones
        result = df.groupby("User").agg({"Penalization" :["mean","sum"]}).round(2)
        return result 
    
    def show_penalization_mean(self, data):    
        '''
        Muestra un gráfico de barras con las penalizaciones agrupadas por usuario.
        
        Parameters
        ----------
        - data: DataFrame con los datos de penalización por usuario.
        '''
        # Reiniciamos el índice del dataframe, se convierten el indice en una columna
        data_reset = data.reset_index()
        # Obtenemos los usuarios y las penalizaciones
        users = data_reset[data_reset.columns[0]]
        penalizations = data_reset[data_reset.columns[1]]
        
        # Crear el gráfico de barras
        plt.bar(users, penalizations)
        plt.xlabel('Usuario')                               # Etiqueta eje x
        plt.ylabel('Penalización')                          # Etiqueta eje y
        plt.title('Penalizaciones agrupadas por Usuario')   # Título del gráfico
        plt.show()                                          # Mostrar gráfico
    
        
    def stay_mean(self, data):
        '''
        Calcula el tiempo de espera promedio por tipo de cola.

        Parameters
        ----------
        - data: Lista de listas con los datos de tiempo de espera por tipo de cola.

        Returns
        -------
        - mean_wait_times: DataFrame con el tiempo de espera promedio por tipo de cola.
        '''
        # Generamos el dataframe con los datos de tiempo de espera por tipo de cola
        df = pd.DataFrame(data, columns=["Tipo de Cola", "Tiempo de Espera"])
        # Agrupamos por tipo de cola y mostramos la media y la suma de los tiempos de espera
        result = df.groupby("Tipo de Cola").agg({"Tiempo de Espera" :["mean","sum"]}).round(2)
        return result
    
    def show_stay_mean(self, data): 
        '''
        Muestra un gráfico de barras con los tiempos de espera promedio por tipo de cola.

        Parameters
        ----------
        - data: DataFrame con los datos de tiempo de espera promedio por tipo de cola.
        '''
        # Reiniciamos el índice del dataframe, se convierten el indice en una columna
        data_reset = data.reset_index()
        # Obtenemos los tipos de cola y los tiempos de espera
        queue_type = data_reset[data_reset.columns[0]] 
        time = data_reset[data_reset.columns[1]]
        
        # Crear el gráfico de barras
        plt.bar(queue_type, time)
        plt.xlabel('Tipo de Cola')                                       # Etiqueta eje x
        plt.ylabel('Tiempo de Espera Promedio')                          # Etiqueta eje y                
        plt.title('Tiempos de Espera Promedio por Tipo de Cola')         # Título del gráfico
        plt.show()                                                       # Mostrar gráfico                 

def parse_file(lines):
    '''
    Convierte las líneas de un archivo en una cola de registros.

    Parameters
    ----------
    lines (list): documento csv con los datos a procesar.

    Returns
    -------
    record_queue(queue): Una cola de registros.
    '''
    # Se eliminan los saltos de línea y se separan los elementos por el espacio
    lines = [x.strip("\n").split(" ") for x in lines]
    record_queue = ArrayQueue()
    # Se añaden los elementos a la cola de registros
    for line in lines:
        # id_proceso, id_usuario, tipo_recurso, tiempo_proceso, tiempo_ejecucion
        record_queue.enqueue(Process(line[0], line[1], line[2], line[3], int(line[4])))
        
    return record_queue
            
def main():
    '''
    Función principal del programa.

    Lee un archivo de entrada y realiza el procesamiento de los registros.
    Realiza un seguimiento de los procesos y muestra las estadísticas finales.
    '''
    with open(sys.argv[1]) as f:
        # Leemos los datos y creamos el gestor de colas
        lines = f.readlines()
        record_queue = parse_file(lines)
        manager = ManagerQueue()
        
        # Tiempo inicial
        time = 0
        # Mientras la cola de registros/cola de procesos no esté vacía o haya procesos en ejecución
        while not record_queue.is_empty() or not manager.all_empty() or not manager.all_processes_finished():
            time += 1
            if not record_queue.is_empty():
            # Si la cola de registros no esta vacia se añade el proceso a las cola correspondiente
                actual_process = record_queue.dequeue()
                # Actualizamos el tiempo de unión del proceso a la cola
                actual_process._join_time = time
                # Lo insertamos en la cola correspondiente
                manager.manage_queue(actual_process, time)
            # Intentamos iniciar la ejeciciópn
            manager.process_queues(time)
            # Comprobamos si hay procesos que han terminado
            manager.check_process(time)

        # Generamos las estadísticas finales
        penalization = Statistics().penalization_mean(manager.stats_penalties) # Penalizaciones por usuario
        stay = Statistics().stay_mean(manager.stats_process)                   # Tiempo de espera por tipo de cola
        print("\nPenalizaciones por usuario: \n-----------------------------\n", penalization)
        print("\nTiempo de espera por tipo de cola: \n-----------------------------\n", stay)
        # Mostramos las estadísticas finales en forma de grafico
        Statistics().show_penalization_mean(penalization)
        Statistics().show_stay_mean(stay)
        
if __name__ == "__main__":
    main()