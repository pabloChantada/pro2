from linked_list import SortedPositionalList, Peliculas
from stats import Statistics

'''
TO-DO
COMO IMPLEMENTAR PELICULA ?¿?¿?¿
    PELICULA ES SortedPositionalList??
'''

def parse_file(lines):
    lines = [x.strip("\n").split("; ") for x in lines]
    films = SortedPositionalList()
    for line in lines:
        try:
            # Director/a, Título,  Año  de  estreno,  Puntuación media
            if len(line) != 4:
                print(f"Linea {line} saltada por un fallo en los datos")
                continue
            director, title, year, rating = line
            year = int(year)  # Convertir el año a entero
            rating = float(rating)  # Convertir la puntuación a flotante
            pelicula = Peliculas(director, title, year, rating)
            films.add(pelicula)
        except ValueError as e:
            print(f"Error en la linea {line}: {e}")
    # Ordenar por Autor, año y titulo -> empates            
    return films

def films_unique(data):
    unique_films = SortedPositionalList()
    last_film = None
    # se recorren los titulos, si son iguales se va guardando la version mas reciente
    # en cada iteracion, hasta cambiar de pelicula/director por lo que tenemos la
    # version mas reciente
    for film in data:
        # Si es el primer film o cambia el título o director, agregar directamente
        if not last_film or (film.director, film.title) != (last_film.director, last_film.title):
            if last_film:
                unique_films.add(last_film)
            last_film = film
        else:
            if film.year > last_film.year:
                last_film = film  # Mantenemos el más reciente
    if last_film:
        unique_films.add(last_film)
    return unique_films
        
def write_file(data, file_name):
    
    with open(file_name, 'w') as f:
        f.write("Director; Title; Year; Rating\n")
        for film in data:
            film_line = f"{film.director}; {film.title}; {film.year}; {film.rating}"
            f.write(f"{film_line}\n")

def menu(data):
    write_file(films_unique(data),"unique_sorted_films.csv")
    write_file(data, "sorted_films.csv")
    
    options = ["1","2","3","4","5", "6"]
    user_input = 0
    print("\nSeleccione una de las siguientes opciones (para parar la ejeución pulse CTRL + C):\n")
    while user_input not in options:
        print("1. Todas las películas de la plataforma")
        print("2. Las películas rodadas por un/a director/a")
        print("3. Las películas estrenadas en un año")
        print("4. Número de películas por director/a")
        print("5. Puntuación media por director/a")
        print("6. Puntuación media por año de estreno")
        user_input = str(input("\n______________________\nEscriba aqui la selección: "))
        match user_input:
            case "1":
                print("\nPelículas repetidas: \n")
                print(Statistics.show_films("sorted_films.csv"))
                print("\nPelículas unicas: \n")
                print(Statistics.show_films("unique_sorted_films.csv"))
            case "2": 
                director = str(input("Introduzca el nombre del director: "))
                print("\nPelículas repetidas: \n")
                print(Statistics.by_director("sorted_films.csv", director))
                print("\nPelículas unicas: \n")
                print(Statistics.by_director("unique_sorted_films.csv", director))
            case "3":
                year = str(input("Introduzca el año de estreno: "))
                print("\nPelículas repetidas: \n")
                print(Statistics.by_year("sorted_films.csv", year))
                print("\nPelículas unicas: \n")
                print(Statistics.by_year("unique_sorted_films.csv", year))
            case "4":
                print("\nPelículas repetidas: \n")
                print(Statistics.metrics("sorted_films.csv")[0])
                print("\n unicas: \n")
                print(Statistics.metrics("unique_sorted_films.csv")[0])
            case "5":
                print("\nPelículas repetidas: \n")
                print(Statistics.metrics("sorted_films.csv")[1])
                print("\nPelículas unicas: \n")
                print(Statistics.metrics("unique_sorted_films.csv")[1])
            case "6":
                print("\nPelículas repetidas: \n")
                print(Statistics.metrics("sorted_films.csv")[2])
                print("\nPelículas unicas: \n")
                print(Statistics.metrics("unique_sorted_films.csv")[2])
            case _:
                print("Opción incorrecta, vuelva a seleccionar o detenga la ejecución con CTRL + C\n")           
    
def main():
    file = str(input("Introduzca el nombre del archivo a leer: "))
    # Imagino que generas los filtrados aqui y despues le dice que archivo quiere abrir
    # write_file(films_unique(data),"unique_sorted_films.csv")
    # write_file(data, "sorted_films.csv")
    
    with open(file) as f:
        lines = f.readlines()
        films = parse_file(lines)
    menu(films)
    
if __name__ == "__main__":
    main()