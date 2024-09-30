
#! EJERCICIO 15

#! Se cuenta con una lista de entrenadores Pokémon. De cada uno de estos se conoce:
#! nombre, cantidad de torneos ganados, cantidad de batallas perdidas y cantidad de batallas
#! ganadas. Y además la lista de sus Pokémons, de los cuales se sabe: nombre, nivel,
#! tipo y subtipo. Se pide resolver las siguientes actividades utilizando lista de
#! lista implementando las funciones necesarias:

#! a. obtener la cantidad de Pokémons de un determinado entrenador;
#! b. listar los entrenadores que hayan ganado más de tres torneos;
#! c. el Pokémon de mayor nivel del entrenador con mayor cantidad de torneos ganados;
#! d. mostrar todos los datos de un entrenador y sus Pokémos;
#! e. mostrar los entrenadores cuyo porcentaje de batallas ganados sea mayor al 79 %;
#! f. los entrenadores que tengan Pokémons de tipo fuego y planta o agua/volador
#! (tipo y subtipo);
#! g. el promedio de nivel de los Pokémons de un determinado entrenador;
#! h. determinar cuántos entrenadores tienen a un determinado Pokémon;
#! i. mostrar los entrenadores que tienen Pokémons repetidos;
#! j. determinar los entrenadores que tengan uno de los siguientes Pokémons: Tyrantrum,
#! Terrakion o Wingull;
#! k. determinar si un entrenador “X” tiene al Pokémon “Y”, tanto el nombre del entrenador
#! como del Pokémon deben ser ingresados; además si el entrenador tiene al Pokémon se
#! deberán mostrar los datos de ambos;

from lista import by_name, show_list, search, show_list_list, by_temp, remove

def cantidad_pokemones_entrenador(entrenador, lista_entrenadores):
    for entrenador_actual in lista_entrenadores:
        if entrenador_actual['nombre'] == entrenador:
            return len(entrenador_actual['sublist'])
    return 0

def entrenadores_3torneos(lista_entrenadores):
    entrenadores_ganadores = []
    for entrenador in lista_entrenadores:
        if entrenador['torneos_ganados'] > 3:
            entrenadores_ganadores.append(entrenador['nombre'])
    return entrenadores_ganadores

def mas_nivel_mas_torneos(lista_entrenadores):
    entrenador_mas_torneos = max(lista_entrenadores, key=lambda x: x['torneos_ganados'])

    pokemones_entrenador = entrenador_mas_torneos['sublist']

    pokemon_mayor_nivel = max(pokemones_entrenador, key=lambda x: x['nivel'])
    
    return pokemon_mayor_nivel

def show_entrenador_pokemons(entrenador_buscado, lista_entrenadores):
    for entrenador in lista_entrenadores:
        if entrenador['nombre'] == entrenador_buscado:
            print(f"Nombre del Entrenador: {entrenador['nombre']}")
            print(f"Torneos Ganados: {entrenador['torneos_ganados']}")
            print("Pokemons asociados:")
            for pokemon in entrenador['sublist']:
                print(f"  Nombre: {pokemon['nombre']}")
                print(f"  Nivel: {pokemon['nivel']}")
                print(f"  Tipo: {pokemon['tipo']}")
                print(f"  Subtipo: {pokemon['subtipo']}")
            return
    print(f"No se encontro al entrenador '{entrenador_buscado}' en la lista")

def porcentaje(entrenador):
    total_batallas = entrenador['batallas_perdidas'] + entrenador['batallas_ganadas']
    if total_batallas == 0:
        return 0
    return (entrenador['batallas_ganadas'] / total_batallas) * 100

def entrenadores_porcentaje_alto(lista_entrenadores, porcentaje_minimo):
    entrenadores_altos = []
    for entrenador in lista_entrenadores:
        porcen= porcentaje(entrenador)
        if porcen > porcentaje_minimo:
            entrenadores_altos.append(entrenador)
    return entrenadores_altos

def entrenadores_tipos_especificos(lista_entrenadores, tipo1, tipo2, subtipo1, subtipo2):
    entrenadores_tipos = []
    for entrenador in lista_entrenadores:
        for pokemon in entrenador['sublist']:
            if (pokemon['tipo'] == tipo1 and pokemon['subtipo'] == subtipo1) or (pokemon['tipo'] == tipo2 and pokemon['subtipo'] == subtipo2):
                entrenadores_tipos.append(entrenador)
                break
    return entrenadores_tipos

def promedio_nivel(entrenador, lista_entrenadores):
    for entrenador_actual in lista_entrenadores:
        if entrenador_actual['nombre'] == entrenador:
            pokemones_entrenador = entrenador_actual['sublist']
            if len(pokemones_entrenador) == 0:
                return 0
            nivel_total = sum(pokemon['nivel'] for pokemon in pokemones_entrenador)
            return nivel_total / len(pokemones_entrenador)
    return None

def cant_entrenadores_pokemon(nombre_pokemon, lista_entrenadores):
    cont = 0
    for entrenador in lista_entrenadores:
        for pokemon in entrenador['sublist']:
            if pokemon['nombre'] == nombre_pokemon:
                cont += 1
                break
    return cont

def entrenadores_pokemons_repetidos(lista_entrenadores):
    entrenadores_repetidos = []
    for entrenador in lista_entrenadores:
        pokemones_entrenador = []
        for pokemon in entrenador['sublist']:
            if pokemon['nombre'] in pokemones_entrenador:
                entrenadores_repetidos.append({
                    'nombre': entrenador['nombre'],
                    'pokemones_repetidos': pokemon['nombre']
                })
                break
            else:
                pokemones_entrenador.append(pokemon['nombre'])
    return entrenadores_repetidos

def entrenadores_pokemones_especificos(pokemones_buscados, lista_entrenadores):
    entrenadores_coincidentes = []
    for entrenador in lista_entrenadores:
        for pokemon in entrenador['sublist']:
            if pokemon['nombre'] in pokemones_buscados and entrenador['nombre'] not in entrenadores_coincidentes:
                entrenadores_coincidentes.append(entrenador['nombre'])
                break
    return entrenadores_coincidentes

def encontrar_entrenador_pokemon(entrenador_buscado, pokemon_buscado, lista_entrenadores):
    for entrenador in lista_entrenadores:
        if entrenador['nombre'] == entrenador_buscado:
            for pokemon in entrenador['sublist']:
                if pokemon['nombre'] == pokemon_buscado:
                    print("Datos del Entrenador:")
                    print(f"Nombre: {entrenador['nombre']}")
                    print(f"Torneos Ganados: {entrenador['torneos_ganados']}")
                    print("Datos del Pokémon:")
                    print(f"Nombre: {pokemon['nombre']}")
                    print(f"Nivel: {pokemon['nivel']}")
                    print(f"Tipo: {pokemon['tipo']}")
                    print(f"Subtipo: {pokemon['subtipo']}")
                    return
            print(f"El entrenador '{entrenador_buscado}' no tiene al Pokemon '{pokemon_buscado}' en su equipo")
            return
    print(f"No se encontro al entrenador '{entrenador_buscado}' en la lista de entrenadores")

lista_entrenadores = []

entrenadores = [
{
'nombre': "Ash Ketchum",
'torneos_ganados': 7,
'batallas_perdidas': 50,
'batallas_ganadas': 120
},
{
'nombre': "Goh",
'torneos_ganados': 2,
'batallas_perdidas': 10,
'batallas_ganadas': 40
},
{
'nombre': "Leon",
'torneos_ganados': 10,
'batallas_perdidas': 5,
'batallas_ganadas': 100
},
{
'nombre': "Chloe",
'torneos_ganados': 1,
'batallas_perdidas': 8,
'batallas_ganadas': 30
},
{
'nombre': "Raihan",
'torneos_ganados': 4,
'batallas_perdidas': 15,
'batallas_ganadas': 60
}
]
pokemones = [
    {
        'nombre': "Pikachu",
        'nivel': 35,
        'tipo': "Eléctrico",
        'subtipo': None,
        'entrenador': "Leon"
    },
    {
        'nombre': "Charizard",
        'nivel': 40,
        'tipo': "Fuego",
        'subtipo': "Volador",
        'entrenador': "Raihan"
    },
    {
        'nombre': "Bulbasaur",
        'nivel': 30,
        'tipo': "Planta",
        'subtipo': "Veneno",
        'entrenador': "Goh"
    },
    {
        'nombre': "Pikachu",
        'nivel': 35,
        'tipo': "Eléctrico",
        'subtipo': None,
        'entrenador': "Leon"
    },
    {
        'nombre': "Starmie",
        'nivel': 30,
        'tipo': "Agua",
        'subtipo': "Psíquico",
        'entrenador': "Chloe"
    },
    {
        'nombre': "Psyduck",
        'nivel': 25,
        'tipo': "Agua",
        'subtipo': None,
        'entrenador': "Goh"
    },
    {
        'nombre': "Psyduck",
        'nivel': 25,
        'tipo': "Agua",
        'subtipo': None,
        'entrenador': "Chloe"
    },
    {
        'nombre': "Gyarados",
        'nivel': 35,
        'tipo': "Agua",
        'subtipo': "Volador",
        'entrenador': "Ash Ketchum"
    },
    {
        'nombre': "Onix",
        'nivel': 38,
        'tipo': "Roca",
        'subtipo': "Tierra",
        'entrenador': "Leon"
    },
    {
        'nombre': "Geodude",
        'nivel': 28,
        'tipo': "Roca",
        'subtipo': "Tierra",
        'entrenador': "Chloe"
    },
    {
        'nombre': "Vulpix",
        'nivel': 20,
        'tipo': "Fuego",
        'subtipo': None,
        'entrenador': "Ash Ketchum"
    },
    {
        'nombre': "Blastoise",
        'nivel': 50,
        'tipo': "Agua",
        'subtipo': None,
        'entrenador': "Raihan"
    },
    {
        'nombre': "Tyrantrum",
        'nivel': 60,
        'tipo': "Agua",
        'subtipo': "Tierra",
        'entrenador': "Raihan"
    },
    {
        'nombre': "Umbreon",
        'nivel': 45,
        'tipo': "Siniestro",
        'subtipo': None,
        'entrenador': "Chloe"
    },
    {
        'nombre': "Nidoking",
        'nivel': 40,
        'tipo': "Veneno",
        'subtipo': "Tierra",
        'entrenador': "Goh"
    }]

for entrenador in entrenadores:
    entrenador.update({'sublist': []})
    lista_entrenadores.append(entrenador)

lista_entrenadores.sort(key=by_name)

for pokemon in pokemones:
    pos = search(lista_entrenadores, 'nombre', pokemon['entrenador'])
    if pos is not None:
        lista_entrenadores[pos]['sublist'].append(pokemon)
    else:
        print('El entrenador no esta en la lista')

# show_list_list('Lista de Entrenadores', 'Lista de Pokemones', lista_entrenadores)
#! A
print('Buscador de entrenador (cantidad de pokemons)')
entrenador_buscado = "Goh"
pok_entrenador = cantidad_pokemones_entrenador(entrenador_buscado, lista_entrenadores)
print(f'El entrenador buscado ({entrenador_buscado}) tiene {pok_entrenador} pokemons')

#! B
print()
print('Entrenadores que ganaron mas de tres torneos:')
entrenadores_gan3 = entrenadores_3torneos(lista_entrenadores)
for entrenador in entrenadores_gan3:
    print(entrenador)

#! C
print()
pokemon_nivel_torneos = mas_nivel_mas_torneos(lista_entrenadores)
print(f"El Pokemon de mayor nivel del entrenador con mayor cantidad de torneos ganados es: {pokemon_nivel_torneos['nombre']}")

#! D
print()
print('Buscador de entrenador (datos del entrenador y sus pokemons)')
entrenador_buscado = "Raihan"
show_entrenador_pokemons(entrenador_buscado, lista_entrenadores)

#! E
print()
porcentaje_minimo = 79
entrenadores_alto_portcentaje = entrenadores_porcentaje_alto(lista_entrenadores, porcentaje_minimo)
print(f"Entrenadores con porcentaje de batallas ganadas mayor al {porcentaje_minimo}%:")
for entrenador in entrenadores_alto_portcentaje:
    print(entrenador['nombre'])

#! F
print()
tipo1 = "Fuego"
subtipo1 = "Planta"
tipo2 = "Agua"
subtipo2 = "Volador"
entrenadores_tipos = entrenadores_tipos_especificos(lista_entrenadores, tipo1, tipo2, subtipo1, subtipo2)
if entrenadores_tipos:
    print('Entrenadores con algun pokemon de tipo fuego y planta o agua y volador:')
    for entrenador in entrenadores_tipos:
        print(entrenador['nombre'])
else:
    print('No se encontraron entrenadores con algun pokemon de tipo fuego y planta o agua y volador')

#! G
print()
entrenador_buscado = "Ash Ketchum"
promedio_entrenador = promedio_nivel(entrenador_buscado, lista_entrenadores)
if promedio_entrenador is not None:
    print(f"El promedio de nivel de los pokemons de {entrenador_buscado} es: {promedio_entrenador}")
else:
    print(f"No se encontro al entrenador '{entrenador_buscado}' en la lista")

#! H
print()
pokemon_buscado = "Psyduck"
cantidad_entrenadores = cant_entrenadores_pokemon(pokemon_buscado, lista_entrenadores)
print(f'{pokemon_buscado} esta en el equipo de {cantidad_entrenadores} entrenador/es')

#! I
print()
print('Entrenadores con Pokemon repetidos en su equipo:')
entrenadores_repetidos = entrenadores_pokemons_repetidos(lista_entrenadores)
if entrenadores_repetidos:
    for entrenador in entrenadores_repetidos:
        print(entrenador['nombre'])
else:
    print('No hay entrenadores con Pokemon repetidos en su equipo')

#! J
print()
print("Entrenador/es que tienen a alguno de los Pokemons 'Tyrantrum', 'Terrakion' o 'Wingull':")
pokemones_buscados = ["Tyrantrum", "Terrakion", "Wingull"]
entrenadores_coincidentes = entrenadores_pokemones_especificos(pokemones_buscados, lista_entrenadores)
if entrenadores_coincidentes:
    for entrenador in entrenadores_coincidentes:
        print(entrenador)
else:
    print('No hay entrenadores con los Pokemons buscados en su equipo')

#! K
print()
entrenador_buscado = input('Ingrese el nombre del entrenador: ')
pokemon_buscado = input('Ingrese el nombre del Pokemon: ')
encontrar_entrenador_pokemon(entrenador_buscado, pokemon_buscado, lista_entrenadores)