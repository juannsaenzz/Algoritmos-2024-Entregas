
#! PUNTO 1
#! Saenz de Santa Maria, Juan Ignacio

def listar_inverso(lista):
    if len(lista) == 0:
        return []
    else:
        return [lista[-1]] + listar_inverso(lista[:-1])

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print(listar_inverso(lista))