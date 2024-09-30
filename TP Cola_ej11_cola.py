
#! EJERCICIO 11

#! Dada una cola con personajes de la saga Star Wars, de los cuales se conoce su nombre y planeta
#! de origen. Desarrollar las funciones necesarias para resolver las siguientes actividades:

#! a. mostrar los personajes del planeta Alderaan, Endor y Tatooine
#! b. indicar el plantea natal de Luke Skywalker y Han Solo
#! c. insertar un nuevo personaje antes del maestro Yoda
#! d. eliminar el personaje ubicado después de Jar Jar Binks

from pila import Stack
from cola import Queue

# Función para mostrar personajes de un planeta específico
def mostrar_personajes_por_planeta(cola, planeta):
    pila_aux = Stack()  # Pila auxiliar para mantener el orden
    encontrados = []  # Lista para almacenar los personajes encontrados
    
    # Recorremos la cola buscando personajes del planeta solicitado
    while cola.size() > 0:
        personaje = cola.attention()  # Se atiende (extrae) el primer personaje de la cola
        if personaje["planeta"] == planeta:
            encontrados.append(personaje["nombre"])  # Si coincide el planeta, lo guardamos
        pila_aux.push(personaje)  # Guardamos el personaje en la pila auxiliar para no perderlo
    
    # Restauramos la cola original
    while pila_aux.size() > 0:
        cola.arrive(pila_aux.pop())  # Devolvemos los personajes de la pila auxiliar a la cola
    
    # Mostramos el resultado
    if encontrados:
        print(f"Personajes encontrados en el planeta {planeta}:")
        for personaje in encontrados:
            print(personaje)  # Imprimimos cada personaje encontrado
    else:
        print(f"No se encontraron personajes en el planeta {planeta}")

# Función para encontrar el planeta natal de un personaje específico
def encontrar_planeta_natal(cola, personaje):
    pila_aux = Stack()  # Pila auxiliar para mantener el orden
    encontrado = False  # Bandera para verificar si encontramos el personaje
    
    # Recorremos la cola buscando el personaje
    while cola.size() > 0:
        p = cola.attention()  # Se atiende el primer personaje de la cola
        if p["nombre"] == personaje:
            # Si coincide el nombre del personaje, mostramos el planeta natal
            print(f"El planeta natal de {personaje} es {p['planeta']}")
            encontrado = True  # Indicamos que fue encontrado
        pila_aux.push(p)  # Guardamos el personaje en la pila auxiliar para no perderlo
    
    # Restauramos la cola original
    while pila_aux.size() > 0:
        cola.arrive(pila_aux.pop())  # Devolvemos los personajes de la pila auxiliar a la cola
    
    if not encontrado:
        print(f"No se encontró el personaje {personaje}")  # Si no se encontró, mostramos un mensaje

# Función para insertar un nuevo personaje antes del maestro Yoda
def insertar_antes_de_maestro_yoda(cola, nuevo_personaje):
    pila_aux = Stack()  # Pila auxiliar para mantener el orden
    
    # Recorremos la cola buscando al maestro Yoda
    while cola.size() > 0:
        personaje = cola.attention()  # Se atiende el primer personaje de la cola
        if personaje["nombre"] == "Yoda":
            break  # Si encontramos a Yoda, salimos del bucle
        pila_aux.push(personaje)  # Guardamos el personaje en la pila auxiliar para no perderlo
    
    # Insertamos el nuevo personaje antes de Yoda
    cola.arrive(nuevo_personaje)
    
    # Restauramos la cola original
    while pila_aux.size() > 0:
        cola.arrive(pila_aux.pop())  # Devolvemos los personajes de la pila auxiliar a la cola

# Función para eliminar el personaje que está inmediatamente después de Jar Jar Binks
def eliminar_despues_de_jar_jar(cola):
    pila_aux = Stack()  # Pila auxiliar para mantener el orden
    encontrado = False  # Bandera para verificar si encontramos a Jar Jar Binks
    eliminado = False  # Bandera para verificar si ya eliminamos al siguiente personaje
    
    # Recorremos la cola buscando a Jar Jar Binks
    while cola.size() > 0:
        personaje = cola.attention()  # Se atiende el primer personaje de la cola
        if encontrado and not eliminado:
            # Si ya encontramos a Jar Jar Binks, eliminamos el siguiente personaje
            eliminado = True  # Indicamos que ya eliminamos el personaje
        else:
            pila_aux.push(personaje)  # Guardamos el personaje en la pila auxiliar si no se elimina
        
        if personaje["nombre"] == "Jar Jar Binks":
            encontrado = True  # Indicamos que encontramos a Jar Jar Binks
    
    # Restauramos la cola original
    while pila_aux.size() > 0:
        cola.arrive(pila_aux.pop())  # Devolvemos los personajes de la pila auxiliar a la cola
    
    if not encontrado:
        print("Jar Jar Binks no encontrado en la cola")  # Si no encontramos a Jar Jar, mostramos un mensaje
    elif eliminado:
        print("Personaje después de Jar Jar Binks eliminado")  # Si eliminamos, mostramos un mensaje

# Inicialización de la cola con personajes de Star Wars
cola_star_wars = Queue()

# Agregamos personajes a la cola_star_wars con su nombre y planeta
cola_star_wars.arrive({"nombre": "Luke Skywalker", "planeta": "Tatooine"})
cola_star_wars.arrive({"nombre": "Han Solo", "planeta": "Corellia"})
cola_star_wars.arrive({"nombre": "Leia Organa", "planeta": "Alderaan"})
cola_star_wars.arrive({"nombre": "Yoda", "planeta": "Dagobah"})
cola_star_wars.arrive({"nombre": "Jar Jar Binks", "planeta": "Naboo"})
cola_star_wars.arrive({"nombre": "Ewok", "planeta": "Endor"})

# Llamamos a las funciones para realizar las operaciones solicitadas
mostrar_personajes_por_planeta(cola_star_wars, "Alderaan")  # Muestra personajes de Alderaan
mostrar_personajes_por_planeta(cola_star_wars, "Endor")  # Muestra personajes de Endor
mostrar_personajes_por_planeta(cola_star_wars, "Tatooine")  # Muestra personajes de Tatooine

encontrar_planeta_natal(cola_star_wars, "Luke Skywalker")  # Encuentra planeta natal de Luke Skywalker
encontrar_planeta_natal(cola_star_wars, "Han Solo")  # Encuentra planeta natal de Han Solo

insertar_antes_de_maestro_yoda(cola_star_wars, {"nombre": "Nuevo Personaje", "planeta": "Planeta Nuevo"})  # Inserta un personaje antes de Yoda

eliminar_despues_de_jar_jar(cola_star_wars)  # Elimina el personaje después de Jar Jar Binks
