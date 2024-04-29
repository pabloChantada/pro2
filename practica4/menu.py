from esentials.avl_tree import AVL
from main import oferta_agregada, oferta_comun, visualize
from stats import Statistics
from course import Curso

class Menu:
    def parse_file(lines):
        '''
        Añade los datos de un archivo a una SortedPositionalList
        
        Parameters
        ----------
        lines(file): archivo a dividir
        '''

        lines = [x.strip("\n").split(",") for x in lines]
        tree = AVL()
        cnt = 0
        for line in lines:
                # Line = nombre, duración(horas), número de estudiantes, nivel, idioma y precio
                tree[cnt] = Curso(line[0], int(line[1]), int(line[2]), line[3], line[4], float(line[5]))
                cnt += 1
        # IZQ < PADRE; DER > PADRE
        return tree
    
    def show_menu_options():
        '''
        Se muestran al usuario las opciones posibles
        '''
        
        print("1. Cargar cursos")
        print("2. Oferta Agregada")
        print("3. Oferta Comun")
        print("4. Estadisticas")
        print("5. Parar la ejecucion")

    def execute_options(user_input, fileA, fileB):
        global treeA, treeB
        match user_input:
            # Leer archivo
            case "1":
                try:
                    with open(fileA) as f:
                        lines = f.readlines()
                        treeA = Menu.parse_file(lines)
                    with open(fileB) as f:
                        lines = f.readlines()
                        treeB = Menu.parse_file(lines)
                    print("File Loaded.")
                except FileNotFoundError as e:
                    print(f"Introduzca correctamente el nombre del archivo: {e}\n\n")             
                return treeA, treeB
            # Oferta agregada
            case "2":
                try:
                    print()
                    visualize(oferta_agregada(treeA, treeB), user_input)
                    print()
                except FileNotFoundError as e:
                    print(f"Debe guardar primero el archivo: {e}\n") 
            # Oferta comun
            case "3":
                try:
                    print()
                    visualize(oferta_comun(treeA, treeB), user_input)
                    print()
                except FileNotFoundError as e:
                    print(f"Debe guardar primero el archivo: {e}\n") 
            # Stats
            case "4": 
                try: 
                    print("Tree A stats:\n")
                    Statistics.mean_language(treeA)
                    Statistics.mean_level(treeA)
                    Statistics.total_income(treeA)
                    print()
                    print("Tree B stats:\n")
                    Statistics.mean_language(treeB)
                    Statistics.mean_level(treeB)
                    Statistics.total_income(treeB)
                    print()
                    
                except FileNotFoundError as e:
                    print(f"Debe guardar primero el archivo: {e}\n")
            case "5":
                print("Parando la ejecución...")
                return
            case _:
                print("Opción incorrecta, vuelva a seleccionar o detenga la ejecución con 9\n")

    def menu(fileA, fileB):
        '''
        Muestra un menu por pantalla con 9 opciones
        '''
        print("\nSeleccione una de las siguientes opciones (para parar la ejeución pulse CTRL + C):\n")
        # Creamos un placeholder del user_input como un string vacio
        user_input = ""
        # Repetimos mientras no se seleccione cerrar el progama
        while user_input != "5":
            # Mostramos las opciones
            Menu.show_menu_options()
            user_input = str(input("\n______________________\nEscriba aqui la selección: "))
            # Ejecutamos la opcion seleccionada
            Menu.execute_options(user_input, fileA, fileB)   