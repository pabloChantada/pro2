'''
Pablo Chantada Saborido | pablo.chantada@udc.es
Pablo Verdes Sánchez | p.verdess@udc.es
'''

from positional_list import SortedPositionalList, Peliculas
from stats import Statistics

def parse_file(lines):
    '''
    Añade los datos de un archivo a una SortedPositionalList
    
    Parameters
    ----------
    lines(file): archivo a dividir
    '''

    lines = [x.strip("\n").split("; ") for x in lines]
    films = SortedPositionalList()
    for line in lines:
        try:
            # Director/a, Título,  Año  de  estreno,  Puntuación media
            # Nos aseguramos de que tengan los campos necesarios
            if len(line) != 4:
                print(f"Linea {line} saltada por un fallo en los datos")
                continue
            director, title, year, rating = line
            # Convertimos los datos a los valores nesarios
            year = int(year)  # Convertir el año a entero
            rating = float(rating)  # Convertir la puntuación a flotante
            # Creamos el objeto pelicula
            pelicula = Peliculas(director, title, year, rating)
            films.add(pelicula)
        except ValueError as e:
            print(f"Error en la linea {line}: {e}\n")

    return films

def films_unique(data):
    '''
    Crea una lista posicional ordenada a partir de unos datos, eliminando los repetidos
    
    Parameters
    ----------
    data(list): datos a escribir en el achivo
    
    Returns
    ----------
    SortedPositionalList sin peliculas repetidas
    '''
    
    unique_films = SortedPositionalList()
    last_film = None
    # Se recorren los titulos, si son iguales se va guardando la version mas reciente
    # en cada iteracion, hasta cambiar de pelicula/director por lo que tenemos la
    # version mas reciente
    for film in data:
        # Si es el primer film o cambia el título o director, agregar directamente
        if not last_film or (film.director, film.title) != (last_film.director, last_film.title):
            if last_film:
                unique_films.add(last_film)
            # Actualizamos la ultima pelicula 
            last_film = film
        else:
            # Comprobamos el año
            if film.year > last_film.year:
                last_film = film  # Mantenemos el más reciente
    # Añadimos la ultima pelicula de la lista
    if last_film:
        unique_films.add(last_film)
        
    return unique_films
        
def write_file(data, file_name):
    '''
    Escribe datos sobre un archivo dado
    
    Parameters
    ----------
    data(list): datos a escribir en el achivo
    file_name: nombre del nuevo archivo
    '''
    # Abrimos el archivo
    with open(file_name, 'w') as f:
        # Escribimos las columnas
        f.write("Director; Title; Year; Rating\n")
        for film in data:
            # Añadimos cada dato de la pelicula a el archivo
            film_line = f"{film.director}; {film.title}; {film.year}; {film.rating}"
            f.write(f"{film_line}\n")
            
def show_menu_options():
    '''
    Se muestran al usuario las opciones posibles
    '''
    
    print("1. Cargar archivo (Generar Lista Posicional Ordenada)")
    print("2. Eliminar duplicados")
    print("3. Todas las películas de la plataforma")
    print("4. Las películas rodadas por un/a director/a")
    print("5. Las películas estrenadas en un año")
    print("6. Número de películas por director/a")
    print("7. Puntuación media por director/a")
    print("8. Puntuación media por año de estreno")
    print("9. Parar la ejecución.")

def execute_options(user_input):
    '''
    Ejecuta la opción seleccionada del menu
    
    Parameters
    ----------
    user_input(str): opcion seleccionada por el usuario
    '''
    # Guardamos films como global para usarla en iteraciones posteriores
    global films
    
    match user_input:
        # Leer archivo
        case "1":
            try:
                file = str(input("Introduzca el nombre del archivo original: "))
                with open(file) as f:
                    lines = f.readlines()
                    films = parse_file(lines)
            except FileNotFoundError as e:
                print(f"Introduzca correctamente el nombre del archivo: {e}\n\n")             
            print("Lista Posicional Generada.\n")
        # Generar archivo sin repetidos
        case "2":
            try:
                unique = films_unique(films)
                print("Archivo con peliculas unicas generado.\n")
                write_file(unique, "unique_sorted_films.csv")
            except FileNotFoundError as e:
                print(f"Debe guardar primero el archivo: {e}\n") 
        # Mostrar todas las peliculas
        case "3":
            try:
                print(Statistics.show_films(films))
            except FileNotFoundError as e:
                print(f"Debe guardar primero el archivo: {e}\n") 
        # Mostrar peliculas por director
        case "4": 
            try: 
                director = str(input("Introduzca el nombre del director: "))
                print(Statistics.by_director(films, director))
            except FileNotFoundError as e:
                print(f"Debe guardar primero el archivo: {e}\n")
        # Mostrar peliculas por año
        case "5":
            try:
                year = str(input("Introduzca el año de estreno: "))
                print(Statistics.by_year(films, year))
            except FileNotFoundError as e:
                print(f"Debe guardar primero el archivo: {e}\n")
        # Mostrar numero de peliculas por director        
        case "6":
            try:
                print(Statistics.metrics(films)[0])
            except FileNotFoundError as e:
                print(f"Debe guardar primero el archivo: {e}\n")
        # Mostrar calificacion por director
        case "7":
            try:
                print(Statistics.metrics(films)[1])
            except FileNotFoundError as e:
                print(f"Debe guardar primero el archivo: {e}\n")
        # Mostrar calificaciones por año
        case "8":
            try:
                print(Statistics.metrics(films)[2])
            except FileNotFoundError as e:
                print(f"Debe guardar primero el archivo: {e}\n")
        # Parar la ejecución del progama
        case "9":
            print("Parando la ejecución...")
            return
        case _:
            print("Opción incorrecta, vuelva a seleccionar o detenga la ejecución con 9\n")

def menu():
    '''
    Muestra un menu por pantalla con 9 opciones
    '''
    print("\nSeleccione una de las siguientes opciones (para parar la ejeución pulse CTRL + C):\n")
    # Creamos un placeholder del user_input como un string vacio
    user_input = ""
    # Repetimos mientras no se seleccione cerrar el progama
    while user_input != "9":
        # Mostramos las opciones
        show_menu_options()
        user_input = str(input("\n______________________\nEscriba aqui la selección: "))
        # Ejecutamos la opcion seleccionada
        execute_options(user_input)       
    
    
if __name__ == "__main__":
    menu()
