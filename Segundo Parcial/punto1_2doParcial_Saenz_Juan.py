from arbol_avl import BinaryTree

#Dicicionario con algunos Pokemons
pokemons = [
    {"nombre": "Bulbasaur", "numero": 1, "tipos": ["planta", "veneno"]},
    {"nombre": "Ivysaur", "numero": 2, "tipos": ["planta", "veneno"]},
    {"nombre": "Charmander", "numero": 4, "tipos": ["fuego"]},
    {"nombre": "Charmeleon", "numero": 5, "tipos": ["fuego"]},
    {"nombre": "Squirtle", "numero": 7, "tipos": ["agua"]},
    {"nombre": "Wartortle", "numero": 8, "tipos": ["agua"]},
    {"nombre": "Pikachu", "numero": 25, "tipos": ["electrico"]},
    {"nombre": "Jolteon", "numero": 135, "tipos": ["electrico"]},
    {"nombre": "Magnemite", "numero": 81, "tipos": ["electrico", "acero"]},
    {"nombre": "Magneton", "numero": 82, "tipos": ["electrico", "acero"]},
    {"nombre": "Lycanroc", "numero": 745, "tipos": ["roca"]},
    {"nombre": "Tyrantrum", "numero": 697, "tipos": ["roca", "dragon"]},
    {"nombre": "Electivire", "numero": 466, "tipos": ["electrico"]},
]

# a) Crear los tres arboles AVL para nombre, numero y tipo

# Crear las instancias de los arboles
tree_name = BinaryTree()    # Arbol AVL indexado por nombre
tree_number = BinaryTree()  # Arbol AVL indexado por número
tree_type = BinaryTree()    # Arbol AVL indexado por tipo

# Funcion para insertar los datos en los tres arboles
def insert_pokemon(pokemon):
    # Insertar en el arbol por nombre
    tree_name.insert_node(pokemon["nombre"].lower(), pokemon)  # Convertir a minusculas para evitar problemas con mayusculas
    
    # Insertar en el arbol por numero
    tree_number.insert_node(pokemon["numero"], pokemon)
    
    # Insertar en el arbol por tipo
    for tipo in pokemon["tipos"]:
        tipo_node = tree_type.search(tipo)
        if tipo_node is None:
            # Crear nodo de tipo con lista de Pokemon
            tree_type.insert_node(tipo, {"pokemons": [pokemon]})
        else:
            # Agregar el Pokemon a la lista del tipo existente
            tipo_node.other_value["pokemons"].append(pokemon)

# Insertar cada Pokemon en los arboles
for pokemon in pokemons:
    insert_pokemon(pokemon)

# b) Mostrar datos de un Pokemon a partir de su numero y nombre (busqueda por proximidad en numero y nombre)
def show_pokemon_by_number_and_name(number, name_prefix):
    print("b) Mostrar datos de un Pokemon por numero y nombre (busqueda por proximidad)")
    pokemon_by_number = tree_number.search(number)
    if pokemon_by_number:
        print(f"Datos del Pokemon con numero {number}: {pokemon_by_number.other_value}")

    print(f"Pokemons cuyo nombre contiene '{name_prefix}':")
    tree_name.proximity_search(name_prefix.lower())  # La busqueda no distingue entre mayusculas y minusculas para evitar posibles erorres

# Prueba de b)
show_pokemon_by_number_and_name(4, "bul")

# c) Mostrar nombres de Pokemon de un tipo especifico (agua, fuego, planta, eléctrico)
def show_pokemon_by_type(pokemon_type):
    print()
    print(f"c) Mostrar nombres de todos los Pokemon de tipo {pokemon_type}")
    type_node = tree_type.search(pokemon_type)
    if type_node:
        print(f"Pokemons de tipo {pokemon_type}:")
        for pokemon in type_node.other_value["pokemons"]:
            print(pokemon["nombre"])

# Prueba de c)
show_pokemon_by_type("fuego")
show_pokemon_by_type("agua")
show_pokemon_by_type("planta")
show_pokemon_by_type("eléctrico")

# d) Listado en orden ascendente por numero y nombre, y listado por nivel por nombre
def show_pokemon_sorted_and_by_level():
    print()
    print("d) Listado en orden ascendente por numero y nombre, y por nivel por nombre")
    
    # Listar en orden por numero y nombre
    print("Poké-emons en orden ascendente por numero y nombre:")
    def inorden_with_names(root):
        if root is not None:
            inorden_with_names(root.left)
            print(f"{root.value} - {root.other_value['nombre']}")
            inorden_with_names(root.right)
    
    inorden_with_names(tree_number.root)

    print("Pokemons en orden ascendente por nombre:")
    tree_name.inorden()

    print("Pokemons por nivel por nombre:")
    tree_name.by_level()

# Prueba de d)
show_pokemon_sorted_and_by_level()

# e) Mostrar datos de Pokemon especificos (Jolteon, Lycanroc, Tyrantrum)
def show_specific_pokemon(names):
    print()
    print("e) Mostrar datos de Pokemon especificos: Jolteon, Lycanroc, Tyrantrum")
    for name in names:
        pokemon_node = tree_name.search(name.lower())  # Busqueda sin distinguir entre mayusculas y minusculas
        if pokemon_node:
            print(f"Datos de {name}: {pokemon_node.other_value}")

# Prueba de e)
show_specific_pokemon(["Jolteon", "Lycanroc", "Tyrantrum"])

# f) Determinar cuantos Pokemon hay de tipo electrico y acero
def count_pokemon_by_types(types):
    print()
    print("f) Determinar la cantidad de Pokemon de tipo electrico y acero")
    for pokemon_type in types:
        type_node = tree_type.search(pokemon_type)
        count = len(type_node.other_value["pokemons"]) if type_node else 0
        print(f"Cantidad de Pokemons de tipo {pokemon_type}: {count}")

# Prueba de f)
count_pokemon_by_types(["electrico", "acero"])
