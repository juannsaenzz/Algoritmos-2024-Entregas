
#! Desarrollar una función que permita convertir un número romano en un número decimal.

def convert_romanos(num_romano):
    #! Defino un diccionario con cada valor romano y su decimal correspondiente
    romanos = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    
    #! Convierto los simbolos en mayusculas
    num_romano = num_romano.upper()
    
    #! Asegurarse de que todos los simbolos ingresados son validos
    for char in num_romano:
        if char not in romanos:
            raise ValueError(f"El simbolo '{char}' no es valido dentro de los numeros romanos")
    
    #! Caso base: cuando ya recorrimos todo el numero romano
    if len(num_romano) == 0:
        return 0
    
    #! Caso base: si la longitud del numero romano es 1, se devuelve el decimal correspondiente del diccionario
    if len(num_romano) == 1:
        return romanos[num_romano]
    
    #! Si el valor del primer caracter romano es menor que el siguiente, es un caso de sustracción
    if romanos[num_romano[0]] < romanos[num_romano[1]]:
        #! Al segundo caracter le restamos el primero y se llama a la funcion recursivsa desde el tercer caracter en adelante
        return romanos[num_romano[1]] - romanos[num_romano[0]] + convert_romanos(num_romano[2:])
    else:
        #! Sino, se suma el valor del primer simbolo y se llama a la funcion recursiva desde el segundo caracter en adelante
        return romanos[num_romano[0]] + convert_romanos(num_romano[1:])

try:
    num_romano = input('Ingrese un numero romano: ')
    nnum_romano = num_romano.upper()
    print(f'El {num_romano} en decimal es: {convert_romanos(nnum_romano)}')
except ValueError as error:
    print(error)