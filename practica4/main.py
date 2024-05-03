'''
Pablo Chantada Saborido | pablo.chantada@udc.es
Pablo Verdes Sánchez | p.verdess@udc.es
'''

from course import Curso


def higher_profit(course_a, course_b):
    '''
    Calcula qué curso de dos tiene un mayor beneficio y devuelve una nueva instancia de Curso
    con la suma de estudiantes de ambos.

    Se genera una nueva instacia para evitar modificar el arbol original.

    Parameters 
    ----------
    - course_a (Curso): Primer curso para comparar.
    - course_b (Curso): Segundo curso para comparar.

    Returns 
    -------
    - Curso: Nueva instancia de Curso con el mayor beneficio y la suma de estudiantes de ambos cursos.
    '''

    # Mayor beneficio (precio por hora y estudiante)
    benefit_a = course_a.price * course_a.students * course_a.duration
    benefit_b = course_b.price * course_b.students * course_b.duration

    if benefit_a >= benefit_b:
        # Hacemos deepcopy del curso para no modificar el original
        new_course = Curso(course_a.name, course_a.duration, course_a.students + course_b.students,
                           course_a.level, course_a.language, course_a.price)
    else:
        new_course = Curso(course_b.name, course_b.duration, course_b.students + course_a.students,
                           course_b.level, course_b.language, course_b.price)

    return new_course


def oferta_agregada(treeA, treeB):
    """
    Combina las ofertas de dos árboles según: nombre, nivel e idioma.
    En caso de coincidencia por nombre pero discrepancia por nivel o idioma, se modifican
    los nombres de los cursos y ambos se agregan a la lista resultante; indicando de que
    compañia vienen.

    Parameters 
    ----------
    - treeA (AVL): Primer árbol de cursos.
    - treeB (AVL): Segundo árbol de cursos.

    Returns 
    -------
    - combined_offers (list): Lista de cursos combinados.
    """

    combined_offers = []
    # Guardamos los ya visitados para acelerar la ejecución
    visited_b = set()
    for i in treeA:
        matched = False
        for j in treeB:
            # Cojemos los nodos de cada arbol
            node_a = treeA[i]
            node_b = treeB[j]
            if node_a.name == node_b.name:
                visited_b.add(node_b)
                # Son iguales
                if (node_a.level, node_a.language) == (node_b.level, node_b.language):
                    combined_offers.append(higher_profit(node_a, node_b))
                    matched = True
                    break
                # Solo comparten nombre
                else:
                    node_a.company = "Academia A"
                    node_b.company = "Academia B"
                    combined_offers.append(node_a)
                    combined_offers.append(node_b)
                    matched = True
        # Si no esta en B, lo añadimos. Es la operación de union
        if not matched:
            combined_offers.append(node_a)

    # Agregamos los cursos restantes de B
    for j in treeB:
        # Cojemos el nodo
        node_b = treeB[j]
        if node_b not in visited_b:
            combined_offers.append(node_b)

    return combined_offers


def oferta_comun(treeA, treeB):
    """
    Encuentra cursos comunes en dos árboles y devuelve una lista de los cursos con mayor beneficio.

    Parameters:
    - treeA (AVL): Primer árbol de cursos.
    - treeB (AVL): Segundo árbol de cursos.

    Returns:
    - common_courses(list): Lista de cursos comunes con el mayor beneficio de cada par.
    """
    common_courses = []
    for i in treeA:
        for j in treeB:
            # Cojemos los nodos de cada arbol
            node_a = treeA[i]
            node_b = treeB[j]
            # Si son iguales, cojemos el de mayor beneficio
            if (node_a.name, node_a.level, node_a.language) == (node_b.name, node_b.level, node_b.language):
                common_courses.append(higher_profit(node_a, node_b))
                break

    return common_courses


# Añadir un input
def visualize(data, input):
    '''    
    Visualiza la lista de cursos de acuerdo al tipo de oferta indicado.

    Parameters 
    ----------
    - data (list): Lista de cursos a visualizar.
    - input (int): Identificador del tipo de oferta (2 para agregada, 3 para común).
    '''
    print(f"\nShowing Oferta Agregada:\n") if input == 2 else print(
        f"\nShowing Oferta Comun:\n")
    # Imprimimos los cursos del arbol
    for i in range(len(data)):
        print(data[i])


if __name__ == "__main__":
    from menu import MenuManager
    # Iniciamos el menu
    MenuManager.menu()
