'''
Pablo Chantada Saborido | pablo.chantada@udc.es
Pablo Verdes Sánchez | p.verdess@udc.es
'''



def preorder_indent_BST(T, p, d):
    """Print preorder representation of a binary subtree of T rooted at p at depth d.
        To print aTree completely call preorder_indent_BST(aTree, aTree.root(), 0)"""
    if p is not None:
        # use depth for indentation
        print(2*d*' ' + "(" + str(p.key()) + "," +  str(p.value()) + ")") 
        preorder_indent_BST(T, T.left(p), d+1) # left child depth is d+1
        preorder_indent_BST(T, T.right(p), d+1) # right child depth is d+1
        


def higher_profit(course_a, course_b):
    benefit_a = course_a.price * course_a.students * course_a.duration
    benefit_b = course_b.price * course_b.students * course_b.duration
    if benefit_a >= benefit_b:
        course_a.students += course_b.students  # Sumamos los estudiantes del curso menos rentable
        return course_a
    else:
        course_b.students += course_a.students
        return course_b

    
# Union
def oferta_agregada(treeA, treeB):
    combined_offers = []
    visited_b = set()

    for i in treeA:
        matched = False
        for j in treeB:
            node_a = treeA[i]
            node_b = treeB[j]
            if node_a.name == node_b.name:
                visited_b.add(node_b)
                if (node_a.level, node_a.language) == (node_b.level, node_b.language):
                    combined_offers.append(higher_profit(node_a, node_b))
                    matched = True
                    break
                else:
                    node_a.name += " (Academia A)"
                    node_b.name += " (Academia B)"
                    combined_offers.append(node_a)
                    combined_offers.append(node_b)
                    matched = True
        if not matched:
            combined_offers.append(node_a)
    
    # Agregar los cursos en B que no fueron visitados
    for j in treeB:
        node_b = treeB[j]
        if node_b not in visited_b:
            combined_offers.append(node_b)

    return combined_offers

            
# Interseccion
def oferta_comun(treeA, treeB):
    common_courses = []
    for i in treeA:
        for j in treeB:
            node_a = treeA[i]
            node_b = treeB[j]
            if (node_a.name, node_a.level, node_a.language) == (node_b.name, node_b.level, node_b.language):
                common_courses.append(higher_profit(node_a, node_b))
                break

    return common_courses


# Añadir un input
def visualize(data, input):
    print(f"\nShowing Oferta Agregada:  \n") if input == "2" else print(f"\nShowing Oferta Comun:  \n")
    for i in range(len(data)):
        print(data[i])

if __name__ == "__main__":
    from menu import Menu
    Menu.menu("ejA.txt", "ejB.txt")