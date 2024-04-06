import sys
from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *
from pandastable import Table
import pandas as pd

from linked_list import SortedPositionalList

'''
TO-DO

REINCIAR DATAFRAMES
COMO IMPLEMENTAR PELICULA ?¿?¿?¿
    PELICULA ES SortedPositionalList??
COLOCAR TITULOS EN LAS METRICAS
'''
# Turn into CONSTANTS
window_height = 800                                     # Altura de la ventana
window_width = 1100                                    # Ancho de la ventana


def parse_file(lines):
    lines = [x.strip("\n").split("; ") for x in lines]
    films = SortedPositionalList()
    for line in lines:
        # Director/a, Título,  Año  de  estreno,  Puntuación media
        films.add(line)
    # Ordenar por Autor, año y titulo -> empates            
    return films


def show_films(window, data):
    # Creamos el frame para el dataframe
    
    loaded_data = pd.read_csv(data, sep=";")
    loaded_data.columns = ['Director', 'Título', 'Año', 'Calificación']
    dataframe = Frame(window)
    dataframe.grid()                            # Posicion del frame
    # Creamos la tabla con el dataframe
    # showtoolbar=True, showstatusbar=True
    table = Table(dataframe, dataframe=loaded_data, width=window_width - 90)
    table.show()

def by_director(window, data, director_entry):
    director = director_entry.get()  # Obtenemos el director del Entry widget
    loaded_data = pd.read_csv(data, sep=";")
    loaded_data.columns = ['Director', 'Título', 'Año', 'Calificación']
    filtered_data = loaded_data[loaded_data["Director"] == director]
    dataframe = Frame(window)
    dataframe.grid()  # Posición del frame
    table = Table(dataframe, dataframe=filtered_data, width=window_width - 90)
    table.show()

def by_year(window, data, year_entry):
    year = year_entry.get()
    loaded_data = pd.read_csv(data, sep=";")
    loaded_data.columns = ['Director', 'Título', 'Año', 'Calificación']
    filtered_data = loaded_data[loaded_data["Año"] == int(year)]
    dataframe = Frame(window)
    dataframe.grid()                            # Posicion del frame
    # Creamos la tabla con el dataframe
    # showtoolbar=True, showstatusbar=True
    table = Table(dataframe, dataframe=filtered_data, width=window_width - 90)
    table.show()

def metrics(window, data):
    loaded_data = pd.read_csv(data, sep=";")
    loaded_data.columns = ['Director', 'Título', 'Año', 'Calificación']
    # Calcular el conteo por director
    df1 = loaded_data.groupby("Director").size().reset_index(name='Nº Peliculas')
    # Calcular la media y desviación estándar de las calificaciones por director
    df2 = loaded_data.groupby("Director")["Calificación"].agg(["mean", "std"]).round(2).reset_index().fillna(0)
    # Calcular la media y desviación estándar de las calificaciones por año
    df3 = loaded_data.groupby("Año")["Calificación"].agg(["mean", "std"]).round(2).reset_index().fillna(0)

    # Crear un Frame para cada tabla y mostrarla
    frame1 = Frame(window)
    frame1.grid(row=1, column=0, padx=10, pady=10)
    label1 = Label(frame1, text="Conteo por Director")
    label1.grid(row=0, column=0, padx=10, pady=5)  # Ajuste aquí para estar en columna 0
    table1 = Table(frame1, dataframe=df1, width=350)
    table1.show()

    frame2 = Frame(window)
    frame2.grid(row=1, column=1, padx=10, pady=10)
    label2 = Label(frame2, text="Calificaciones por Director")
    label2.grid(row=0, column=0, padx=10, pady=5)  # Ajuste aquí para estar en columna 0
    table2 = Table(frame2, dataframe=df2, width=400)
    table2.show()

    frame3 = Frame(window)
    frame3.grid(row=2, column=0)
    label3 = Label(frame3, text="Calificaciones por Año")
    label3.grid(row=0, column=0)  # Ajuste aquí para estar en columna 0
    table3 = Table(frame3, dataframe=df3, width=225)
    table3.show()

   
def menu(data):
    window = Tk()
    window.title("Menú de Peliculas")              # Titulo de la ventana

    screen_height = window.winfo_screenheight()             # Alto de la pantalla
    screen_width = window.winfo_screenwidth()               # Largo de la pantalla
    # Ajustamos la coordenada x a la pantalla
    x = int((screen_width / 2) - (window_width / 2))
    # Ajustamos la coordenada y a la pantalla
    y = int((screen_height / 2) - (window_height / 2))
    # Ajustamos la geometria de la ventana
    window.geometry("{}x{}+{}+{}".format(window_width, window_height, x, y))
    # Hacemos que la ventana no se pueda redimensionar
    window.resizable(False, False)

    # BUTTONS
    button_frame = Frame(window)
    button_frame.grid()

    all_films = Button(button_frame, text="All Films", width=10,
                       command=lambda: show_films(window, data))
    all_films.grid(row=0, column=0, pady=1, sticky="w")
    
    director = Entry(button_frame, width=20)
    director.grid(row=1, column=1, pady=1, sticky="w")
    show_director = Button(button_frame, text="Filter by Director", width=15,
                       command=lambda: by_director(window, data, director))
    show_director.grid(row=1, column=0, pady=1, sticky="w")
    
    year = Entry(button_frame, width=20)
    year.grid(row=2, column=1, pady=1, sticky="w")
    show_year = Button(button_frame, text="Filter by Year", width=15,
                       command=lambda: by_year(window, data, year))
    show_year.grid(row=2, column=0, pady=1, sticky="w")
    
    stats = Button(button_frame, text="Metrics", width=10,
                       command=lambda: metrics(window, data))
    stats.grid(row=3, column=0, pady=1, sticky="w")
    
    # Para poder eliminarlo con la X
    window.protocol("WM_DELETE_WINDOW", sys.exit)
    window.mainloop()

    
def main():
    with open(sys.argv[1]) as f:
        lines = f.readlines()
        films = parse_file(lines)

    sorted_duplicate = "sorted_films.txt"
    
    unique_films = []
    last_film = None
    # se recorren los titulos, si son iguales se va guardando la version mas reciente
    # en cada iteracion, hasta cambiar de pelicula/director por lo que tenemos la
    # version mas reciente
    for film in films:
        # Si es el primer film o cambia el título o director, agregar directamente
        if not last_film or (film[0], film[1]) != (last_film[0], last_film[1]):
            if last_film:
                unique_films.append(last_film)
            last_film = film
        # Si es un duplicado (mismo título y director), mantener el más reciente (esto se garantiza por el orden)
        else:
            last_film = film  # Esto garantiza que siempre tengamos la versión más reciente

    # Asegúrate de agregar el último film procesado
    if last_film:
        unique_films.append(last_film)
    
    # Mejor esta version que una que lo hace con readlines y reescribiendo el archivo ?
    sorted_unique = 'unique_sorted_films.csv'
    with open(sorted_unique, 'w') as f:
        f.write("Director; Title; Year; Rating\n")
        for film in unique_films:
            film_line = "; ".join(film)
            f.write(f"{film_line}\n")
    
    with open(sorted_duplicate, 'w') as f:
        for film in films:
            film_line = "; ".join(film)
            f.write(f"{film_line}\n")
    
    menu(sorted_duplicate)
if __name__ == "__main__":
    main()