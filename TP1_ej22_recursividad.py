
#! El problema de la mochila Jedi. Suponga que un Jedi (Luke Skywalker, Obi-Wan Kenobi, Rey u otro,
#! el que más le guste) está atrapado, pero muy cerca está su mochila que contiene muchos objetos.
#! Implementar una función recursiva llamada “usar la fuerza” que le permita al Jedi “con ayuda de la fuerza”
#! realizar las siguientes actividades:

#! A. sacar los objetos de la mochila de a uno a la vez hasta encontrar un sable de luz o que no
#! queden más objetos en la mochila;

#! B. determinar si la mochila contiene un sable de luz y cuantos objetos fueron necesarios sacar para encontrarlo;

#! C. Utilizar un vector para representar la mochila.

import random

class Mochila:
    #! La clase mochila tiene dos metodos: __init__ inicia la mochila con una lista de objetos
    def __init__(self, objetos):
        self.objetos = objetos
    
    #! sacar_objeto saca y devuelve el primer objeto de la lista
    def sacar_objeto(self):
        if not self.objetos:
            #! Devuelve None si la mochila esta vacia
            return None
        #! Saca y borra el primer objeto
        return self.objetos.pop(0)

#! Funcion recursiva, recibe un objeto mochila como parametro
def usar_la_fuerza(mochila, cont = 0):
    #! Mezclar de forma aleatoria los objetos de la mochila
    random.shuffle(mochila.objetos)
    
    #! Caso base: cuando la mochila esta vacia
    if not mochila.objetos:
        return False, cont
    
    #! Saca el primer objeto
    objeto = mochila.sacar_objeto()
    #! Muestra el objeto sacado
    print(f'Usando la fuerza para sacar el objeto: {objeto}')
    #! Contar la cantidad de objetos sacados
    cont += 1
    
    #! Si encuentra un sable de luz, termina la recursion
    if objeto == 'sable de luz':
        return True, cont
    
    #! Llamada a la funcion recursiva para sacar el siguiente objeto
    return usar_la_fuerza(mochila, cont)

mochila_jedi = Mochila(['comida', 'sable', 'mapa', 'espada','brujula', 'sable de luz', 'ropa'])
se_encontro, cont = usar_la_fuerza(mochila_jedi)
if se_encontro:
    print('La mochila de Jedi contiene un sable de luz')
    print(f'Fueron necesarios sacar {cont-1} objetos para encontrarlo')
else:
    print('El sable de luz no fue encontrado dentro de la mochila')