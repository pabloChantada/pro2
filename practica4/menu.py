'''
Pablo Chantada Saborido | pablo.chantada@udc.es
Pablo Verdes Sánchez | p.verdess@udc.es
'''

from esentials.avl_tree import AVL
from main import oferta_agregada, oferta_comun, visualize
from stats import Statistics
from course import Curso


class MenuManager:
    '''
    Clase para diseñar un menu por consola.
    '''

    def __init__(self):
        '''
        Inicializa un nuevo objeto MenuManager con árboles vacíos para almacenar cursos.
        '''
        self.treeA = None
        self.treeB = None

    @staticmethod
    def parse_file(lines):
        '''
        Procesa y añade los datos de un archivo a un árbol AVL.

        Parameters 
        ----------
        - lines (lista de str): Archivo a parsear, donde cada linea es un curso.

        Returns 
        -------
        - AVL: Un árbol AVL con los datos de los cursos del archivo.
        '''
        # Eliminamos saltos de linea y dividimos por comas
        lines = [x.strip("\n").split(",") for x in lines]
        tree = AVL()
        # Usamos enumerate para acceder al arbol directamente para cada linea
        for cnt, line in enumerate(lines):
            tree[cnt] = Curso(line[0], int(line[1]), int(
                line[2]), line[3], line[4], float(line[5]))
        return tree

    @staticmethod
    def show_menu_options():
        '''
        Imprime las opciones del menú disponibles para el usuario.
        '''
        print("\n1: Cargar archivos\n2: Oferta Agregada\n3: Oferta Comun\n4: Estadisticas\n5: Salir")

    def load_files(self):
        '''
        Carga los datos desde archivos especificados por el usuario y los almacena en árboles AVL.
        '''
        while True:
            fileA = input("Nombre del archivo A: ")
            fileB = input("Nombre del archivo B: ")
            try:
                with open(fileA) as f:
                    lines = f.readlines()
                    self.treeA = MenuManager.parse_file(lines)
                with open(fileB) as f:
                    lines = f.readlines()
                    self.treeB = MenuManager.parse_file(lines)
                print("Archivo Cargado.")
                break
            except FileNotFoundError:
                print(
                    "Error al cargar el archivo. Asegurese de que la ruta sea correcta.")

    def oferta_agregada(self):
        '''
        Ejecuta y visualiza la oferta agregada basada en los árboles cargados.
        '''
        print()
        visualize(oferta_agregada(self.treeA, self.treeB), 2)
        print()

    def oferta_comun(self):
        '''
        Ejecuta y visualiza la oferta comun basada en los árboles cargados.
        '''
        print()
        visualize(oferta_comun(self.treeA, self.treeB), 3)
        print()

    def calculate_stats(self):
        '''
        Calcula y muestra las estadísticas de los cursos almacenados en los árboles AVL.
        '''
        # Los arboles han sido cargados
        if self.treeA and self.treeB:
            print("\nTree A stats:\n______________________\n")
            # Número medio de alumnos por idioma.
            Statistics.mean_language(self.treeA)
            # Número medio de alumnos por nivel.
            Statistics.mean_level(self.treeA)
            Statistics.total_income(self.treeA)   # Ingresos totales posibles.
            print()
            print("\nTree B stats:\n______________________\n")
            # Número medio de alumnos por idioma.
            Statistics.mean_language(self.treeB)
            # Número medio de alumnos por nivel.
            Statistics.mean_level(self.treeB)
            Statistics.total_income(self.treeB)   # Ingresos totales posibles.
            print()
        else:
            print("Debe cargar los archivos primero.\n")

    def execute_options(self, user_input):
        '''
        Ejecuta una opción del menú basada en la entrada del usuario.

        Parameters 
        ----------
        - user_input (int): El número de la opción seleccionada por el usuario.
        '''
        match user_input:
            case "1":
                self.load_files()
            case "2":
                self.oferta_agregada()
            case "3":
                self.oferta_comun()
            case "4":
                self.calculate_stats()
            case "5":
                print("Parando la ejecución...")
                return
            case _:
                print(
                    "Opción incorrecta, vuelva a seleccionar o detenga la ejecución con 5\n")

    @staticmethod
    def menu():
        '''
        Inicia el menú principal del programa, permitiendo al usuario elegir entre varias opciones.
        '''
        print("\nSeleccione una de las siguientes opciones (para parar la ejecución pulse CTRL + C):\n")
        manager = MenuManager()
        # Placeholder de la eleccion del usuario
        user_input = ""
        # Mientras no se quiera parar repetimos
        while user_input != "5":
            manager.show_menu_options()
            user_input = str(
                input("\n______________________\nEscriba aquí la selección: "))
            manager.execute_options(user_input)
