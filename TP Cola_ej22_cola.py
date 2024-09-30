
#! EJERCICIO 22

#! Se tienen una cola con personajes de Marvel Cinematic Universe (MCU), de los cuales se cono-
#! ce el nombre del personaje, el nombre del superhéroe y su género (Masculino M y Femenino
#! F) –por ejemplo {Tony Stark, Iron Man, M}, {Steve Rogers, Capitán América, M}, {Natasha Ro-
#! manoff, Black Widow, F}, etc., desarrollar un algoritmo que resuelva las siguientes actividades:

#! a. determinar el nombre del personaje de la superhéroe Capitana Marvel;
#! b. mostrar los nombre de los superhéroes femeninos;
#! c. mostrar los nombres de los personajes masculinos;
#! d. determinar el nombre del superhéroe del personaje Scott Lang;
#! e. mostrar todos datos de los superhéroes o personaje cuyos nombres comienzan
#! con la letra S;
#! f. determinar si el personaje Carol Danvers se encuentra en la cola e indicar su nombre
#! de superhéroes.

from queue import Queue

# Definir la cola de personajes de MCU
cola_mcu = Queue()

# Agregar personajes a la cola de MCU (nombre del personaje, nombre del superhéroe, género)
cola_mcu.put(("Tony Stark", "Iron Man", "M"))
cola_mcu.put(("Steve Rogers", "Capitán América", "M"))
cola_mcu.put(("Natasha Romanoff", "Black Widow", "F"))
cola_mcu.put(("Carol Danvers", "Capitana Marvel", "F"))
cola_mcu.put(("Scott Lang", "Ant-Man", "M"))
cola_mcu.put(("Wanda Maximoff", "Scarlet Witch", "F"))
cola_mcu.put(("Peter Parker", "Spider-Man", "M"))
cola_mcu.put(("Stephen Strange", "Doctor Strange", "M"))
cola_mcu.put(("Bruce Banner", "Hulk", "M"))

# a. Determinar el nombre del personaje de la superhéroe Capitana Marvel
def nombre_personaje_capitana_marvel(cola):
    # Convertimos la cola en una lista para poder iterar sobre ella
    cola_lista = list(cola.queue)
    # Recorremos cada elemento de la cola
    for nombre_personaje, nombre_superheroe, genero in cola_lista:
        # Si el superhéroe es Capitana Marvel, devolvemos el nombre del personaje
        if nombre_superheroe == "Capitana Marvel":
            return nombre_personaje
    return "No se encontró a la Capitana Marvel en la cola"

# b. Mostrar los nombres de los superhéroes femeninos
def superheroes_femeninos(cola):
    # Convertimos la cola en una lista para poder iterar sobre ella
    cola_lista = list(cola.queue)
    superheroes = []
    # Recorremos cada elemento de la cola
    for nombre_personaje, nombre_superheroe, genero in cola_lista:
        # Si el género es femenino (F), añadimos el nombre del superhéroe a la lista
        if genero == "F":
            superheroes.append(nombre_superheroe)
    return superheroes

# c. Mostrar los nombres de los personajes masculinos
def personajes_masculinos(cola):
    # Convertimos la cola en una lista para poder iterar sobre ella
    cola_lista = list(cola.queue)
    personajes = []
    # Recorremos cada elemento de la cola
    for nombre_personaje, _, genero in cola_lista:
        # Si el género es masculino (M), añadimos el nombre del personaje a la lista
        if genero == "M":
            personajes.append(nombre_personaje)
    return personajes

# d. Determinar el nombre del superhéroe del personaje Scott Lang
def superheroe_de_personaje(cola, nombre_personaje):
    # Convertimos la cola en una lista para poder iterar sobre ella
    cola_lista = list(cola.queue)
    # Recorremos cada elemento de la cola
    for nombre_p, nombre_superheroe, _ in cola_lista:
        # Si encontramos el personaje, devolvemos el nombre del superhéroe
        if nombre_p == nombre_personaje:
            return nombre_superheroe
    return None

# e. Mostrar todos los datos de los superhéroes o personajes cuyos nombres comienzan con la letra S
def superheroes_con_letra(cola, letra):
    cola_lista = list(cola.queue)
    superheroes = []
    for nombre_personaje, nombre_superheroe, genero in cola_lista:
        # Verificamos si EITHER el nombre del personaje O el nombre del superhéroe comienza con la letra
        if nombre_personaje.startswith(letra) or nombre_superheroe.startswith(letra):
            superheroes.append((nombre_personaje, nombre_superheroe, genero))
    return superheroes

# f. Determinar si el personaje Carol Danvers se encuentra en la cola e indicar su nombre de superhéroes
def buscar_carol_danvers(cola):
    # Convertimos la cola en una lista para poder iterar sobre ella
    cola_lista = list(cola.queue)
    # Recorremos cada elemento de la cola
    for nombre_personaje, nombre_superheroe, _ in cola_lista:
        # Si el personaje es Carol Danvers, devolvemos su nombre de superhéroe
        if nombre_personaje == "Carol Danvers":
            return nombre_superheroe
    return "No se encontró a Carol Danvers en la cola"

# Ejecutar las funciones y mostrar los resultados
print("a. Nombre del personaje de la superhéroe Capitana Marvel:", nombre_personaje_capitana_marvel(cola_mcu))
print("b. Nombres de los superhéroes femeninos:", superheroes_femeninos(cola_mcu))
print("c. Nombres de los personajes masculinos:", personajes_masculinos(cola_mcu))
print("d. Nombre del superhéroe del personaje Scott Lang:", superheroe_de_personaje(cola_mcu, "Scott Lang"))
print("e. Datos de los superhéroes cuyos nombres comienzan con la letra S:", superheroes_con_letra(cola_mcu, "S"))
print("f. Buscar a Carol Danvers en la cola:", buscar_carol_danvers(cola_mcu))

