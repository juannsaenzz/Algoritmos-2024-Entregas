
#! EJERCICIO 14

#! Implementar sobre un grafo no dirigido los algoritmos necesario para dar solución a las siguientes tareas:

#! a. cada vértice representar un ambiente de una casa: cocina, comedor, cochera, quincho, baño 1, baño 2, habitación 1, habitación 2, sala de estar, terraza, patio;

#! b. cargar al menos tres aristas a cada vértice, y a dos de estas cárguele cinco, el peso de la arista es la distancia entre los ambientes, se debe cargar en metros;

#! c. obtener el árbol de expansión mínima y determine cuantos metros de cables se necesitan para conectar todos los ambientes;

#! d. determinar cuál es el camino más corto desde la habitación 1 hasta la sala de estar para determinar cuántos metros de cable de red se necesitan para conectar el router con el Smart Tv.

from grafo import Graph

# Inicialización del grafo no dirigido
casa = Graph(dirigido=False)

# a. Agregar cada ambiente como vértice
ambientes = ["cocina", "comedor", "cochera", "quincho", "baño 1", "baño 2",
             "habitación 1", "habitación 2", "sala de estar", "terraza", "patio"]

for ambiente in ambientes:
    casa.insert_vertice(ambiente)

# b. Cargar al menos tres aristas a cada vértice y cinco en dos de ellas
# Las distancias se asignan de manera arbitraria para ejemplificar el ejercicio
casa.insert_arista("cocina", "comedor", 5)
casa.insert_arista("cocina", "sala de estar", 8)
casa.insert_arista("cocina", "baño 1", 10)
casa.insert_arista("comedor", "habitación 1", 7)
casa.insert_arista("comedor", "baño 2", 6)
casa.insert_arista("comedor", "terraza", 9)
casa.insert_arista("cochera", "quincho", 4)
casa.insert_arista("cochera", "patio", 6)
casa.insert_arista("cochera", "terraza", 7)
casa.insert_arista("quincho", "patio", 5)
casa.insert_arista("quincho", "habitación 2", 11)
casa.insert_arista("baño 1", "sala de estar", 3)
casa.insert_arista("baño 1", "habitación 1", 8)
casa.insert_arista("baño 2", "habitación 2", 6)
casa.insert_arista("habitación 1", "habitación 2", 4)
casa.insert_arista("habitación 2", "terraza", 9)
casa.insert_arista("sala de estar", "terraza", 12)
casa.insert_arista("sala de estar", "patio", 10)
casa.insert_arista("patio", "terraza", 7)

# c. Obtener el árbol de expansión mínima y calcular el cable total
arbol_minimo = casa.kruskal("cocina")  # Usamos el algoritmo de Kruskal
print("Árbol de expansión mínima para conectar todos los ambientes:")
print(arbol_minimo)

# Calcular la longitud total de cable para el árbol de expansión mínima
longitud_cable_total = sum(int(arista.split('-')[-1]) for arista in arbol_minimo)
print(f"Total de metros de cable necesarios para el árbol de expansión mínima: {longitud_cable_total} metros")

# d. Encontrar el camino más corto entre "habitación 1" y "sala de estar"
camino_mas_corto = casa.dijkstra("habitación 1")

# Inicializar variables para la ruta y la distancia total
distancia_total = 0
ruta = []
nodo_actual = camino_mas_corto.pop()  # Iniciar con el primer nodo de la pila

# Recorrer la pila y construir la ruta completa hasta "sala de estar"
while nodo_actual[1][0] != "sala de estar":
    destino = nodo_actual[1][0]  # Primer elemento de la lista como destino
    distancia = nodo_actual[1][1]  # Segundo elemento como distancia
    
    # Asegurarnos de que `distancia` es un número, extrayendo solo si es necesario
    if isinstance(distancia, dict):
        distancia = int(distancia.get("distancia", 0))
    
    ruta.append(destino)
    distancia_total += distancia  # Sumar la distancia
    if camino_mas_corto.size() > 0:
        nodo_actual = camino_mas_corto.pop()  # Avanzar al siguiente nodo en la pila
    else:
        break  # Terminar si no quedan más nodos

# Añadir el último nodo ("sala de estar") a la ruta
ruta.append("sala de estar")
if isinstance(nodo_actual[1][1], int):
    distancia_total += nodo_actual[1][1]

# Imprimir la ruta y la distancia total
print("Ruta más corta de habitación 1 a sala de estar:", " -> ".join(ruta))
print(f"Metros de cable de red necesarios: {distancia_total} metros")