
#! Implementar un algoritmo que permita generar un árbol con los datos de la siguiente tabla y
#! resuelva las siguientes consultas:

#! a. listado inorden de las criaturas y quienes la derrotaron;

#! b. se debe permitir cargar una breve descripción sobre cada criatura;

#! c. mostrar toda la información de la criatura Talos;

#! d. determinar los 3 héroes o dioses que derrotaron mayor cantidad de criaturas;

#! e. listar las criaturas derrotadas por Heracles;

#! f. listar las criaturas que no han sido derrotadas;

#! g. además cada nodo debe tener un campo “capturada” que almacenará el nombre del héroe
#! o dios que la capturo;

#! h. modifique los nodos de las criaturas Cerbero, Toro de Creta, Cierva Cerinea y Jabalí de
#! Erimanto indicando que Heracles las atrapó;

#! i. se debe permitir búsquedas por coincidencia;

#! j. eliminar al Basilisco y a las Sirenas;

#! k. modificar el nodo que contiene a las Aves del Estínfalo, agregando que Heracles
#! derroto a varias;

#! l. modifique el nombre de la criatura Ladón por Dragón Ladón;

#! m. realizar un listado por nivel del árbol;

#! n. muestre las criaturas capturadas por Heracles.

from arbol_avl import BinaryTree

# Crear una instancia de tu árbol AVL.
tree = BinaryTree()

# Definir las criaturas y sus respectivos derrotadores.
# En la lista, cada criatura está representada por una tupla (nombre, derrotador).
# Si una criatura no tiene derrotador, el valor es None.
creatures_info = [
    ("Ceto", None),
    ("Tifón", "Zeus"),
    ("Equidna", "Argos Panoptes"),
    ("Dino", None),
    ("Pefredo", None),
    ("Enio", None),
    ("Escila", None),
    ("Caribdis", None),
    ("Euríale", None),
    ("Esteno", None),
    ("Medusa", "Perseo"),
    ("Ladón", "Heracles"),
    ("Águila del Cáucaso", None),
    ("Quimera", "Belerofonte"),
    ("Hidra de Lerna", "Heracles"),
    ("León de Nemea", "Heracles"),
    ("Esfinge", "Edipo"),
    ("Dragón de la Cólquida", None),
    ("Cerbero", None),
    ("Cerda de Cromión", "Teseo"),
    ("Ortros", "Heracles"),
    ("Toro de Creta", "Teseo"),
    ("Jabalí de Calidón", "Atalanta"),
    ("Carcinos", None),
    ("Gerión", "Heracles"),
    ("Cloto", None),
    ("Láquesis", None),
    ("Átropos", None),
    ("Minotauro de Creta", "Teseo"),
    ("Harpías", None),
    ("Argos Panoptes", "Hermes"),
    ("Aves del Estínfalo", None),
    ("Talos", "Medea"),
    ("Sirenas", None),
    ("Pitón", "Apolo"),
    ("Cierva de Cerinea", None),
    ("Basilisco", None),
    ("Jabalí de Erimanto", None),
]

# Insertar las criaturas en el árbol AVL.
# Cada nodo contiene el nombre de la criatura y un diccionario con el derrotador y si fue capturada.
for creature, defeated_by in creatures_info:
    tree.insert_node(creature, {'defeated_by': defeated_by, 'capturada': None})

# a. Realizar un recorrido inorden del árbol e imprimir las criaturas con sus derrotadores.
def inorden_with_defeated(tree):
    def __inorden(root):
        if root is not None:
            __inorden(root.left)  # Recorrer el subárbol izquierdo.
            # Obtener el derrotador de la criatura (o "Desconocido" si no tiene).
            defeated_by = root.other_value.get('defeated_by', 'Desconocido')
            print(f"Criatura: {root.value}, Derrotado por: {defeated_by}")
            __inorden(root.right)  # Recorrer el subárbol derecho.

    # Ejecutar el recorrido si el árbol no está vacío.
    if tree.root is not None:
        __inorden(tree.root)

# Llamada para mostrar el recorrido inorden del árbol.
inorden_with_defeated(tree)
print()

# b. Añadir o modificar el derrotador de una criatura.
def agregar_derrotador(tree, creature, defeated_by):
    node = tree.search(creature)  # Buscar la criatura en el árbol.
    if node:
        node.other_value['defeated_by'] = defeated_by  # Actualizar el derrotador.
        print(f"Derrotador añadido a {creature}.")
    else:
        print(f"Criatura {creature} no encontrada.")

# Ejemplo: Añadir derrotador a 'Ceto'.
agregar_derrotador(tree, "Ceto", "Poseidón")

# c. Mostrar toda la información de una criatura específica.
def mostrar_info_criatura(tree, criatura):
    node = tree.search(criatura)  # Buscar la criatura.
    if node:
        # Imprimir la información disponible sobre la criatura.
        print(f"Criatura: {node.value}")
        print(f"Derrotado por: {node.other_value.get('defeated_by', 'Desconocido')}")
        print(f"Capturada por: {node.other_value.get('capturada', 'No capturada')}")
    else:
        print(f"Criatura {criatura} no encontrada.")

# Llamada para mostrar la información de 'Talos'.
mostrar_info_criatura(tree, "Talos")
print()

# d. Determinar los 3 héroes o dioses que derrotaron la mayor cantidad de criaturas.
def heroes_top_derrotas(tree):
    derrotadores = {}  # Diccionario para almacenar el número de derrotas por héroe.

    def __contar_derrotadores(root):
        if root is not None:
            defeated_by = root.other_value.get('defeated_by')
            if defeated_by:
                # Incrementar el conteo de derrotas para el héroe/dios.
                derrotadores[defeated_by] = derrotadores.get(defeated_by, 0) + 1
            __contar_derrotadores(root.left)
            __contar_derrotadores(root.right)

    # Ejecutar el conteo si el árbol no está vacío.
    if tree.root is not None:
        __contar_derrotadores(tree.root)
    
    # Ordenar los héroes por número de derrotas y obtener los 3 primeros.
    top_heroes = sorted(derrotadores.items(), key=lambda x: x[1], reverse=True)[:3]
    for heroe, count in top_heroes:
        print(f"{heroe}: {count} criaturas derrotadas")

# Llamada para mostrar los 3 héroes o dioses con más derrotas.
heroes_top_derrotas(tree)
print()

# e. Listar todas las criaturas derrotadas por un héroe específico.
def listar_criaturas_derrotadas_por(tree, heroe):
    def __listar_criaturas_derrotadas(root):
        if root is not None:
            defeated_by = root.other_value.get('defeated_by')
            if defeated_by == heroe:
                print(f"Criatura: {root.value}")
            __listar_criaturas_derrotadas(root.left)
            __listar_criaturas_derrotadas(root.right)

    print(f"Criaturas derrotadas por {heroe}:")
    if tree.root is not None:
        __listar_criaturas_derrotadas(tree.root)

# Llamada para listar las criaturas derrotadas por Heracles.
listar_criaturas_derrotadas_por(tree, "Heracles")
print()

# f. Listar todas las criaturas que no han sido derrotadas.
def listar_criaturas_no_derrotadas(tree):
    def __listar_no_derrotadas(root):
        if root is not None:
            if not root.other_value.get('defeated_by'):
                print(f"Criatura: {root.value}")
            __listar_no_derrotadas(root.left)
            __listar_no_derrotadas(root.right)

    print("Criaturas que no han sido derrotadas:")
    if tree.root is not None:
        __listar_no_derrotadas(tree.root)

# Llamada para listar las criaturas que no han sido derrotadas.
listar_criaturas_no_derrotadas(tree)
print()

# g. Añadir o modificar el campo "capturada" de una criatura.
def capturar_criatura(tree, criatura, captor):
    node = tree.search(criatura)  # Buscar la criatura.
    if node:
        # Asignar el captor de la criatura.
        node.other_value['capturada'] = captor
        print(f"{criatura} ha sido capturada por {captor}.")
    else:
        print(f"Criatura {criatura} no encontrada.")

# Ejemplo de captura: capturar a 'Talos' por Medea.
capturar_criatura(tree, "Talos", "Medea")
print()

# h. Marcar ciertas criaturas como capturadas por Heracles.
def modificar_captura_por_heracles(tree):
    criaturas_a_atrapar = ["Cerbero", "Toro de Creta", "Cierva de Cerinea", "Jabalí de Erimanto"]
    for criatura in criaturas_a_atrapar:
        capturar_criatura(tree, criatura, "Heracles")

# Llamada para modificar las capturas hechas por Heracles.
modificar_captura_por_heracles(tree)
print()

# i. Permitir búsquedas de criaturas por coincidencia parcial del nombre.
def buscar_por_coincidencia(tree, partial_name):
    def __buscar_coincidencias(root, partial_name):
        if root is not None:
            if partial_name.lower() in root.value.lower():
                print(f"Criatura: {root.value}")
            __buscar_coincidencias(root.left, partial_name)
            __buscar_coincidencias(root.right, partial_name)

    print(f"Criaturas que coinciden con '{partial_name}':")
    if tree.root is not None:
        __buscar_coincidencias(tree.root, partial_name)

# Ejemplo de búsqueda de coincidencias parciales: criaturas que contienen "Cer".
buscar_por_coincidencia(tree, "Cer")
print()

# j. Eliminar al Basilisco y a las Sirenas del árbol.
tree.delete_node("Basilisco")
tree.delete_node("Sirenas")

# k. Modificar la información de las Aves del Estínfalo, indicando que Heracles las derrotó.
def modificar_aves_del_estinfalo(tree):
    node = tree.search("Aves del Estínfalo")
    if node:
        node.other_value['defeated_by'] = "Heracles"  # Actualizar el derrotador.

# Llamada para modificar las Aves del Estínfalo.
modificar_aves_del_estinfalo(tree)
print()

# l. Modificar el nombre de la criatura 'Ladón' a 'Dragón Ladón'.
def modificar_nombre_criatura(tree, old_name, new_name):
    node = tree.search(old_name)  # Buscar la criatura por su nombre antiguo.
    if node:
        node.value = new_name  # Cambiar el nombre de la criatura.
        print(f"Criatura {old_name} ha sido renombrada a {new_name}.")
    else:
        print(f"Criatura {old_name} no encontrada.")

# Llamada para modificar el nombre de 'Ladón' a 'Dragón Ladón'.
modificar_nombre_criatura(tree, "Ladón", "Dragón Ladón")
print()

# m. Realizar un listado del árbol por niveles.
tree.by_level()
print()

# n. Listar todas las criaturas capturadas por un héroe específico (Heracles).
def listar_criaturas_capturadas_por(tree, captor):
    def __listar_capturadas(root):
        if root is not None:
            if root.other_value.get('capturada') == captor:
                print(f"Criatura: {root.value}")
            __listar_capturadas(root.left)
            __listar_capturadas(root.right)

    print(f"Criaturas capturadas por {captor}:")
    if tree.root is not None:
        __listar_capturadas(tree.root)

# Llamada para listar las criaturas capturadas por Heracles.
listar_criaturas_capturadas_por(tree, "Heracles")
print()
