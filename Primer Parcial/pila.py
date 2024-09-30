
class Stack:

    def __init__(self): #! Inicia una pila
        self.__elements = []

    def push(self, element): #! Agrega un elemento al final de la pila
        self.__elements.append(element)

    def pop(self): #! Elimina el ultimo elemento de la pila
        if len(self.__elements) > 0:
            return self.__elements.pop()
        else:
            return None

    def on_top(self): #! Muestra el ultimo elemento (cima) de la pila
        if len(self.__elements) > 0:
            return self.__elements[-1]
        else:
            return None

    def size(self): #! Muestra la cantidad de elementos de la pila
        return len(self.__elements)