
#! Escribir un algoritmo que permita utilizar tres tablas hash para guardar los
#! datos de Pokémons, que contemple las siguientes actividades: 

#! a. en la primera tabla hash la función hash debe ser sobre el tipo de Pokémon,
#! en la segunda tabla la función hash deberá utilizar el ultimo dígito del número del
#! Pokémon como clave y la tercera sera en base  a su nivel repartiéndolos en 10
#! posiciones dentro de la tabla; 
#! b. debe utilizar tablas hash abiertas con listas como estructura secundaria;
#! c. si el Pokémon es de más de un tipo deberá cargarlo en cada uno de las tabla que
#! indiquen estos tipos;
#! d. deberá permitir cargar Pokémons de los cuales se dispone de su número, nombre,
#! tipo/s, nivel.
#! e. mostrar todos los Pokémons cuyos numeros terminan en 3, 7 y 9;
#! f. mostrar todos los Pokémons cuyos niveles son multiplos de 2, 5 y 10;
#! g. mostrar todos los Pokémons de los siguientes tipo: Acero, Fuego, Electrifico, Hielo

from random import randint, choice

def hash_tipo(pokemon):
    tipos = [pokemon['tipo']]
    if pokemon['subtipo']:
        tipos.append(pokemon['subtipo'])
    return tuple(sorted(tipos))

def hash_numero(pokemon):
    return str(pokemon['numero'])[-1]

def hash_nivel(pokemon):
    return pokemon['nivel'] // 10

tipos = ['Planta', 'Fuego', 'Agua', 'Eléctrico', 'Tierra', 'Volador', 'Veneno', 'Normal', 'Lucha', 'Psíquico', 'Siniestro', 'Hada']

tabla_tipo = {}
tabla_numero = {}
tabla_nivel = {}

def agregar_pokemon(pokemon):
    tipo = pokemon['tipo']
    subtipo = pokemon['subtipo']
    numero = str(pokemon['numero'])
    nivel = pokemon['nivel']
    
    tipos = [tipo]
    if subtipo:
        tipos.append(subtipo)
    
    for t in tipos:
        if t not in tabla_tipo:
            tabla_tipo[t] = []
        tabla_tipo[t].append(pokemon)
    
    digito = numero[-1]
    if digito not in tabla_numero:
        tabla_numero[digito] = []
    tabla_numero[digito].append(pokemon)
    
    nivel_hash = hash_nivel(pokemon)
    if nivel_hash not in tabla_nivel:
        tabla_nivel[nivel_hash] = []
    tabla_nivel[nivel_hash].append(pokemon)

def show_ultimos_numeros(ult_digitos):
    for digito in ult_digitos:
        if digito in tabla_numero:
            print(f"Pokemons cuyos numeros terminan en '{digito}':")
            for index, pokemon in enumerate(tabla_numero[digito]):
                print(f"{index + 1}. {pokemon}")
            print()

def show_niveles_multiplos(multiplos):
    for multiplo_str in multiplos:
        multiplo = int(multiplo_str)
        print(f"Pokemons cuyos niveles son múltiplos de '{multiplo}':")
        for nivel_hash, pokemons in tabla_nivel.items():
            if nivel_hash % multiplo == 0:
                for index, pokemon in enumerate(pokemons):
                    print(f"{index + 1}. {pokemon}")
        print()
    
def show_tipos(tipos_show):
    for tipo in tipos_show:
        if tipo in tabla_tipo:
            print(f"Pokemons cuyo tipo es '{tipo}':")
            for index, pokemon in enumerate(tabla_tipo[tipo]):
                print(f"{index + 1}. {pokemon}")
            print()

pokemons = [
    {
        "numero": 4423,
        "nombre": "Pikachu",
        "nivel": 35,
        "tipo": "Electrifico",
        "subtipo": None
    },
    {
        "numero": 45656,
        "nombre": "Charizard",
        "nivel": 40,
        "tipo": "Fuego",
        "subtipo": "Volador"
    },
    {
        "numero": 46576,
        "nombre": "Bulbasaur",
        "nivel": 30,
        "tipo": "Planta",
        "subtipo": "Veneno"
    },
    {
        "numero": 547,
        "nombre": "Starmie",
        "nivel": 30,
        "tipo": "Agua",
        "subtipo": "Psíquico"
    },
    {
        "numero":292847,
        "nombre": "Psyduck",
        "nivel": 25,
        "tipo": "Agua",
        "subtipo": None
    },
    {
        "numero": 5770,
        "nombre": "Gyarados",
        "nivel": 35,
        "tipo": "Agua",
        "subtipo": "Volador"
    },
    {
        "numero": 4365,
        "nombre": "Onix",
        "nivel": 38,
        "tipo": "Roca",
        "subtipo": "Tierra"
    },
    {
        "numero": 4657,
        "nombre": "Geodude",
        "nivel": 28,
        "tipo": "Roca",
        "subtipo": "Tierra"
    },
    {
        "numero": 2643,
        "nombre": "Vulpix",
        "nivel": 20,
        "tipo": "Fuego",
        "subtipo": None
    },
    {
        "numero": 922,
        "nombre": "Blastoise",
        "nivel": 50,
        "tipo": "Agua",
        "subtipo": None
    },
    {
        "numero": 4436,
        "nombre": "Umbreon",
        "nivel": 45,
        "tipo": "Siniestro",
        "subtipo": None
    },
    {
        "numero": 435,
        "nombre": "Nidoking",
        "nivel": 40,
        "tipo": "Veneno",
        "subtipo": "Tierra"
    }
]

for pokemon in pokemons:
    agregar_pokemon(pokemon)

#! E
ult_digitos = ['3', '7', '9']
show_ultimos_numeros(ult_digitos)

#! F
print()
multiplos = ['2', '5', '10']
show_niveles_multiplos(multiplos)

#! G
tipos_show = ['Acero', 'Fuego', 'Electrifico', 'Hielo']
show_tipos(tipos_show)