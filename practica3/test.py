class MenuManager():
    def main_menu():
        print("\nSeleccione una de las siguientes opciones (para parar la ejeución pulse CTRL + C):\n")
        user_input = ""
        while user_input != "9":
            show_main_menu_options()
            user_input = input("\n______________________\nEscriba aqui la selección: ")
            execute_main_options(user_input)

    def show_main_menu_options():
        print("""
        1 - Gestión de películas
        2 - Estadísticas
        9 - Salir
        """)

    def execute_main_options(option):
        if option == "1":
            films_management_menu()
        elif option == "2":
            statistics_menu()
        elif option == "9":
            print("Saliendo del programa...")
        else:
            print("Opción no válida, intente de nuevo.")

    def films_management_menu():
        user_input = ""
        while user_input != "0":
            show_films_menu_options()
            user_input = input("\nEscriba su selección para la gestión de películas: ")
            execute_films_options(user_input)

    def show_films_menu_options():
        print("""
        0 - Volver al menú principal
        1 - Añadir película
        2 - Eliminar película
        """)

    def execute_films_options(option):
        if option == "0":
            return  # Simply return to exit this menu
        elif option == "1":
            add_film()
        elif option == "2":
            delete_film()
        else:
            print("Opción no válida, intente de nuevo.")

    def statistics_menu():
        user_input = ""
        while user_input != "0":
            show_statistics_menu_options()
            user_input = input("\nEscriba su selección para estadísticas: ")
            execute_statistics_options(user_input)

    def show_statistics_menu_options():
        print("""
        0 - Volver al menú principal
        1 - Mostrar películas por director
        2 - Mostrar todas las películas
        """)

    def execute_statistics_options(option):
        if option == "0":
            return  # Simply return to exit this menu
        elif option == "1":
            show_films_by_director()
        elif option == "2":
            show_all_films()
        else:
            print("Opción no válida, intente de nuevo.")