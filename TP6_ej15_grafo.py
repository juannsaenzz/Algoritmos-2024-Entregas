
#! EJERCICIO 15

#! Se requiere implementar un grafo para almacenar las siete maravillas arquitectónicas modernas y naturales del mundo, para lo cual se deben tener en cuenta las siguientes actividades:
#! a. de cada una de las maravillas se conoce su nombre, país de ubicación (puede ser más de uno en las naturales) y tipo (natural o arquitectónica);

#! b. cada una debe estar relacionada con las otras seis de su tipo, para lo que se debe almacenar la distancia que las separa;

#! c. hallar el árbol de expansión mínimo de cada tipo de las maravillas;

#! d. determinar si existen países que dispongan de maravillas arquitectónicas y naturales;

#! e. determinar si algún país tiene más de una maravilla del mismo tipo;

#! f. deberá utilizar un grafo no dirigido.

# Importamos las clases necesarias
from grafo import Graph

# Creamos el grafo no dirigido
maravillas_grafo = Graph(dirigido=False)

# Datos de las maravillas
maravillas_info = {
    'Gran Muralla China': {'tipo': 'arquitectónica', 'países': ['China']},
    'Petra': {'tipo': 'arquitectónica', 'países': ['Jordania']},
    'Cristo Redentor': {'tipo': 'arquitectónica', 'países': ['Brasil']},
    'Machu Picchu': {'tipo': 'arquitectónica', 'países': ['Perú']},
    'Chichén Itzá': {'tipo': 'arquitectónica', 'países': ['México']},
    'Coliseo': {'tipo': 'arquitectónica', 'países': ['Italia']},
    'Taj Mahal': {'tipo': 'arquitectónica', 'países': ['India']},
    'Amazonas': {'tipo': 'natural', 'países': ['Brasil', 'Colombia', 'Perú']},
    'Bahía de Ha-Long': {'tipo': 'natural', 'países': ['Vietnam']},
    'Cataratas del Iguazú': {'tipo': 'natural', 'países': ['Argentina', 'Brasil']},
    'Isla Jeju': {'tipo': 'natural', 'países': ['Corea del Sur']},
    'Komodo': {'tipo': 'natural', 'países': ['Indonesia']},
    'Montaña de la Mesa': {'tipo': 'natural', 'países': ['Sudáfrica']},
    'Río subterráneo de Puerto Princesa': {'tipo': 'natural', 'países': ['Filipinas']}
}

# a. Insertar cada maravilla en el grafo
for maravilla, info in maravillas_info.items():
    maravillas_grafo.insert_vertice(maravilla)

# b. Relacionar maravillas del mismo tipo
# Distancias aproximadas entre maravillas del mismo tipo (en km)
distancias = {
    # Arquitectónicas
    ('Gran Muralla China', 'Petra'): 5000,
    ('Gran Muralla China', 'Cristo Redentor'): 17000,
    ('Gran Muralla China', 'Machu Picchu'): 17000,
    ('Gran Muralla China', 'Chichén Itzá'): 13000,
    ('Gran Muralla China', 'Coliseo'): 8000,
    ('Gran Muralla China', 'Taj Mahal'): 4000,
    ('Petra', 'Cristo Redentor'): 12000,
    ('Petra', 'Machu Picchu'): 13000,
    ('Petra', 'Chichén Itzá'): 12000,
    ('Petra', 'Coliseo'): 2300,
    ('Petra', 'Taj Mahal'): 3000,
    ('Cristo Redentor', 'Machu Picchu'): 3300,
    ('Cristo Redentor', 'Chichén Itzá'): 6600,
    ('Cristo Redentor', 'Coliseo'): 9600,
    ('Cristo Redentor', 'Taj Mahal'): 14000,
    ('Machu Picchu', 'Chichén Itzá'): 4000,
    ('Machu Picchu', 'Coliseo'): 11000,
    ('Machu Picchu', 'Taj Mahal'): 17000,
    ('Chichén Itzá', 'Coliseo'): 9000,
    ('Chichén Itzá', 'Taj Mahal'): 14000,
    ('Coliseo', 'Taj Mahal'): 6000,
    
    # Naturales
    ('Amazonas', 'Bahía de Ha-Long'): 10000,
    ('Amazonas', 'Cataratas del Iguazú'): 3000,
    ('Amazonas', 'Isla Jeju'): 16000,
    ('Amazonas', 'Komodo'): 17000,
    ('Amazonas', 'Montaña de la Mesa'): 8000,
    ('Amazonas', 'Río subterráneo de Puerto Princesa'): 17000,
    ('Bahía de Ha-Long', 'Cataratas del Iguazú'): 17000,
    ('Bahía de Ha-Long', 'Isla Jeju'): 3000,
    ('Bahía de Ha-Long', 'Komodo'): 2700,
    ('Bahía de Ha-Long', 'Montaña de la Mesa'): 11000,
    ('Bahía de Ha-Long', 'Río subterráneo de Puerto Princesa'): 1500,
    ('Cataratas del Iguazú', 'Isla Jeju'): 18000,
    ('Cataratas del Iguazú', 'Komodo'): 18000,
    ('Cataratas del Iguazú', 'Montaña de la Mesa'): 8000,
    ('Cataratas del Iguazú', 'Río subterráneo de Puerto Princesa'): 18000,
    ('Isla Jeju', 'Komodo'): 3000,
    ('Isla Jeju', 'Montaña de la Mesa'): 14000,
    ('Isla Jeju', 'Río subterráneo de Puerto Princesa'): 1500,
    ('Komodo', 'Montaña de la Mesa'): 10000,
    ('Komodo', 'Río subterráneo de Puerto Princesa'): 2500,
    ('Montaña de la Mesa', 'Río subterráneo de Puerto Princesa'): 13000
}

# Agregar las aristas en el grafo según las distancias
for (maravilla1, maravilla2), distancia in distancias.items():
    maravillas_grafo.insert_arista(maravilla1, maravilla2, distancia)

# c. Árbol de expansión mínimo para cada tipo de maravilla
def arbol_expansion_minimo_por_tipo(grafo, tipo):
    vertices_tipo = [v for v, info in maravillas_info.items() if info['tipo'] == tipo]
    sub_grafo = Graph(dirigido=False)
    
    # Insertar solo los vértices del tipo específico
    for v in vertices_tipo:
        sub_grafo.insert_vertice(v)
    for (v1, v2), distancia in distancias.items():
        if v1 in vertices_tipo and v2 in vertices_tipo:
            sub_grafo.insert_arista(v1, v2, distancia)
    
    # Calcular el árbol de expansión mínimo usando Kruskal
    return sub_grafo.kruskal(vertices_tipo[0])

# Ejemplo de uso
print("Árbol de expansión mínimo para maravillas arquitectónicas:")
print(arbol_expansion_minimo_por_tipo(maravillas_grafo, 'arquitectónica'))

print("Árbol de expansión mínimo para maravillas naturales:")
print(arbol_expansion_minimo_por_tipo(maravillas_grafo, 'natural'))

# d. Determinar si existen países que dispongan de maravillas arquitectónicas y naturales
paises_con_multiples_tipos = set()
paises_con_arquitectonicas = set()
paises_con_naturales = set()

for maravilla, info in maravillas_info.items():
    if info['tipo'] == 'arquitectónica':
        paises_con_arquitectonicas.update(info['países'])  
    elif info['tipo'] == 'natural':
        paises_con_naturales.update(info['países'])  

# Intersección de países que tienen maravillas arquitectónicas y naturales
paises_con_multiples_tipos = paises_con_arquitectonicas.intersection(paises_con_naturales)
print("Países con maravillas de ambos tipos (arquitectónica y natural):", list(paises_con_multiples_tipos))

# e. Determinar si algún país tiene más de una maravilla del mismo tipo
paises_con_multiples_maravillas = {}
for maravilla, info in maravillas_info.items():
    for pais in info['países']:  # Iterar sobre todos los países
        tipo = info['tipo']
        if pais not in paises_con_multiples_maravillas:
            paises_con_multiples_maravillas[pais] = {'arquitectónica': 0, 'natural': 0}
        paises_con_multiples_maravillas[pais][tipo] += 1

# Filtrar los países que tienen más de una maravilla del mismo tipo
paises_con_multiples_maravillas = {pais: tipos for pais, tipos in paises_con_multiples_maravillas.items() 
                                    if tipos['arquitectónica'] > 1 or tipos['natural'] > 1}
print("Países con múltiples maravillas del mismo tipo:", paises_con_multiples_maravillas)