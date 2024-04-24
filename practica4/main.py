'''
Pablo Chantada Saborido | pablo.chantada@udc.es
Pablo Verdes Sánchez | p.verdess@udc.es
'''

from stats import Statistics
from esentials.avl_tree import AVL

def preorder_indent_BST(T, p, d):
    """Print preorder representation of a binary subtree of T rooted at p at depth d.
        To print aTree completely call preorder_indent_BST(aTree, aTree.root(), 0)"""
    if p is not None:
        # use depth for indentation
        print(2*d*' ' + "(" + str(p.key()) + "," +  str(p.value()) + ")") 
        preorder_indent_BST(T, T.left(p), d+1) # left child depth is d+1
        preorder_indent_BST(T, T.right(p), d+1) # right child depth is d+1
        
def parse_file(lines):
    '''
    Añade los datos de un archivo a una SortedPositionalList
    
    Parameters
    ----------
    lines(file): archivo a dividir
    '''

    lines = [pass if x[1] == '#' else x.strip("\n").split(",") for x in lines]
    tree = AVL()
    cnt = 0
    for line in lines:
        # Line = nombre, duración(horas), número de estudiantes, nivel, idioma y precio
        tree[cnt] = line
        cnt += 1
    # IZQ < PADRE; DER > PADRE
    print("Tree: "); preorder_indent_BST(tree,tree.root(),0)
    
    
def visualize_ofetas():
    pass
def more_benefit(objA, objB):
    benefitA = objA["precio"] * (objA["hora"] / objA["estudiante"])
    benefitB = objB["precio"] * (objB["hora"] / objB["estudiante"])
    return objA if objA > objB else objB
 
def oferta_agregada(treeA: AVL, treeB: AVL):
    '''
    Cada academia
    Visualizar
    
    - Iguales (nombre, nivel, idioma) -> seleccionar mayor beneficio (precio x hora/estudiante)
    - Nombres iguales -> añadir nombre de compañia
    '''
    # Lista de tuplas con los indices de ambos arboles
    in_both = []
    # Recorremos ambos arboles, comprobamos los atributos, añadimos los nodos que sean iguales
    # Doble bucle para recorrer el A y mirar todos los elementos de B
    for i in treeA:
        current_node_b = treeA[i]
        for j in treeB:
            current_node_b = treeB[j]
            pass
    
    visualize_ofetas(in_both)            
            
            
            
def oferta_comun():
    '''
    Ambas academias
    Visualizar
    
    - Iguales (nombre, nivel, idioma) -> seleccionar mayor beneficio (precio x hora/estudiante)
    - Nombres iguales -> añadir nombre de compañia     
    '''
    pass


file = "ejA.txt"
with open(file) as f:
    lines = f.readlines()
    films = parse_file(lines)

file = "ejB.txt"
with open(file) as f:
    lines = f.readlines()
    films = parse_file(lines)