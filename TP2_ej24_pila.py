
#! Dada una pila de personajes de Marvel Cinematic Universe (MCU), de los cuales se dispone de su nombre y
#! la cantidad de películas de la saga en la que participó, implementar las funciones necesarias para resolver
#! las siguientes actividades:

#! A. determinar en qué posición se encuentran Rocket Raccoon y Groot, tomando como posición uno la cima
#! de la pila;

#! B. determinar los personajes que participaron en más de 5 películas de la saga, además indicar la
#! cantidad de películas en la que aparece;

#! C. determinar en cuantas películas participo la Viuda Negra (Black Widow);

#! D. mostrar todos los personajes cuyos nombre empiezan con C, D y G.

from pila import Stack

#! Primero defino las funciones necesarias

#! A
def posicion(pila):
    pos = 1
    #! Crea una lista para almacenar la posicion de ambos
    resultados = []
    while pila.size() > 0:
        personaje, peliculas = pila.pop()
        #! Determina en que posicion se encuentran Rocket Raccoon y Groot
        if personaje == 'Rocket Raccoon':
            resultados.append(f'Rocket Raccoon se encuentra en la posicion {pos}')
        elif personaje == 'Groot':
            resultados.append(f'Groot se encuentra en la posicion {pos}')
        pos += 1
    return resultados

#! B
def mas_de_5(pila):
    #! Crea una lista para almacenar los datos de los personajes
    personajes_mas_5 = []
    while pila.size() > 0:
        personaje, peliculas = pila.pop()
        #! Determina si el personaje se encuentra en mas de 5 peliculas
        if peliculas > 5:
            #! Almacena sus datos en la lista
            personajes_mas_5.append((personaje, peliculas))
    return personajes_mas_5

#! C
def participacion(pila):
    participa = []
    while pila.size() > 0:
        personaje, peliculas = pila.pop()
        if personaje == 'Black Widow':
            participa.append(f'Black Widow participo en {peliculas} peliculas')
    return participa
        
#! D
def personajes_iniciales(pila, iniciales):
    #! Crea una lista para almacenar los datos de los personajes
    personajes = []
    while pila.size() > 0:
        personaje, peliculas = pila.pop()
        if personaje[0] in iniciales:
            personajes.append(personaje)
    return personajes

#! Crea una pila para los personajes y una copia por cada funcion donde se utiliza, para no perder los datos
pila_MCU = Stack()
pila_MCU_copia_1 = Stack()
pila_MCU_copia_2 = Stack()
pila_MCU_copia_3 = Stack()

#! Crea un diccionario con los personajes y la cantidad de peliculas
personajes = [
    ('Spider-Man', 5), ('Iron Man', 8), ('Groot', 4), ('Capitana Marvel', 5),
    ('Thor', 9), ('Hulk', 6), ('Rocket Raccoon', 4), ('Black Widow', 6), ('Capitán América', 7),
    ('Doctor Strange', 5), ('Black Panther', 3), ('Ant-Man', 5), ('Locky', 5)
]

#! Recorre el diccionario y agrega cada elemento a la pila y sus tres copias
for personaje in personajes:
    pila_MCU.push(personaje)
    pila_MCU_copia_1.push(personaje)
    pila_MCU_copia_2.push(personaje)
    pila_MCU_copia_3.push(personaje)

#! A             
rocket_groot = (posicion(pila_MCU))
#! Recorre la lista para mostrar la posicion de ambos
if rocket_groot != []:
    for i in range (len(rocket_groot)):
        print(rocket_groot[i])
else:
    print('No se encontraron los personajes')

print()

#! B
personajes_mas5 = mas_de_5(pila_MCU_copia_1)
print('Personajes que participaron en mas de 5 peliculas:')
#! Recorre la lista para mostrar los personajes que participaron en mas de 5 peliculas
if personajes_mas5 != []:
    for personaje, peliculas in personajes_mas5:
        print(f'{personaje} participo en {peliculas} peliculas')
else:
    print('No se encontraron personajes que hayan participado en mas de 5 peliculas')

print()

#! C
participa = participacion(pila_MCU_copia_2)
if participa != []:
    for i in range(len(participa)):
        print(participa[i])
else:
    print('No se encontro a Black Widow')

print()

#! D
#! Crea una lista con las inciales
iniciales = ['C', 'D', 'G']
print('Personajes cuyos nombres empiezan con C, D y G:')
personajes_cdg = personajes_iniciales(pila_MCU_copia_3, iniciales)
#! Recorre la lista para mostrar los personajes cuyas iniciales empiezan con c, d o g
if personajes_cdg != []:
    for personaje in personajes_cdg:
        print(personaje)
else:
    print('No se encontraron personajes cuyas iniciales empiecen con C, D y G')