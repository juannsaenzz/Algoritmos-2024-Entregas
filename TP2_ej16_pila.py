
#! Se tienen dos pilas con personajes de Star Wars, en una los del episodio V de “The empire strikes back”
#! y la otra los del episodio VII “The force awakens”. Desarrollar un algoritmo que permita obtener la
#! intersección de ambas pilas, es decir los personajes que aparecen en ambos episodios.

from pila import Stack

#! Crea una pila para cada episodio y una pila para la interseccion de ambas pilas
episodio_V = Stack()
episodio_VII = Stack()
interseccion = Stack()

#! Carga los personajes de ambas pilas

episodio_V.push('Luke Skywalker')
episodio_V.push('Han Solo')
episodio_V.push('Darth Vader')
episodio_V.push('Princesa Leia Organa')
episodio_V.push('Ben (Obi-Wan) Kenobi')
episodio_V.push('C3PO')
episodio_V.push('Emperador Palpatine')
episodio_V.push('Yoda')
episodio_V.push('Lando Calrissian')
episodio_V.push('Boba Fett')
episodio_V.push('Almirante Piett')
episodio_V.push('Capitán Needan')
episodio_V.push('Almirante Ozzel')

episodio_VII.push('Ben Solo / Kylo Ren')
episodio_VII.push('Rey')
episodio_VII.push('Finn/FN-2187')
episodio_VII.push('Han Solo')
episodio_VII.push('Chewbacca')
episodio_VII.push('Poe Dameron')
episodio_VII.push('Leia Organa')
episodio_VII.push('Maz Kanata')
episodio_VII.push('General Armitage Hux')
episodio_VII.push('C3PO')
episodio_VII.push('Snoke')
episodio_VII.push('Luke Skywalker')

#! Crea una lista para almacenar los personajes de la pila episodio V
data_V = []

print('Episodio V:')

#! Agrega los personajes de la pila episodio V a la lista creada
while episodio_V.size() > 0:
    data = episodio_V.pop()
    print(data)
    data_V.append(data)

print()
print('Episodio VII:')

#! Compara cada personaje de la pila episodio VII con los personajes almacenados en la lista del episodio V
while episodio_VII.size() > 0:
    data_VII = episodio_VII.pop()
    print(data_VII)
    #! Si el personaje de la pila episodio VII se encuentra en la lista del episodio V, se agrega a la pila 'interseccion
    if data_VII in data_V:
        interseccion.push(data_VII)

print()        

#! Muestra la intersección de los personajes
print('Personajes que aparecen en ambos episodios:')
while interseccion.size() > 0:
    print(interseccion.pop())