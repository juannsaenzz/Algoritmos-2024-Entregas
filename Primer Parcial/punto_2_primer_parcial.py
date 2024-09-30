
#! PUNTO 2
#! Saenz de Santa Maria, Juan Ignacio

from pila import Stack

dinosaurios = [
    {
      "nombre": "Tyrannosaurus Rex",
      "especie": "Theropoda",
      "peso": "7000 kg",
      "descubridor": "Barnum Brown",
      "ano_descubrimiento": 1902
    },
    {
      "nombre": "Triceratops",
      "especie": "Ceratopsidae",
      "peso": "6000 kg",
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1889
    },
    {
      "nombre": "Velociraptor",
      "especie": "Dromaeosauridae",
      "peso": "15 kg",
      "descubridor": "Henry Fairfield Osborn",
      "ano_descubrimiento": 1924
    },
    {
      "nombre": "Brachiosaurus",
      "especie": "Sauropoda",
      "peso": "56000 kg",
      "descubridor": "Elmer S. Riggs",
      "ano_descubrimiento": 1903
    },
    {
      "nombre": "Stegosaurus",
      "especie": "Stegosauridae",
      "peso": "5000 kg",
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1877
    },
    {
      "nombre": "Spinosaurus",
      "especie": "Spinosauridae",
      "peso": "10000 kg",
      "descubridor": "Ernst Stromer",
      "ano_descubrimiento": 1912
    },
    {
      "nombre": "Allosaurus",
      "especie": "Theropoda",
      "peso": "2000 kg",
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1877
    },
    {
      "nombre": "Apatosaurus",
      "especie": "Sauropoda",
      "peso": "23000 kg",
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1877
    },
    {
      "nombre": "Diplodocus",
      "especie": "Sauropoda",
      "peso": "15000 kg",
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1878
    },
    {
      "nombre": "Ankylosaurus",
      "especie": "Ankylosauridae",
      "peso": "6000 kg",
      "descubridor": "Barnum Brown",
      "ano_descubrimiento": 1908
    },
    {
      "nombre": "Parasaurolophus",
      "especie": "Hadrosauridae",
      "peso": "2500 kg",
      "descubridor": "William Parks",
      "ano_descubrimiento": 1922
    },
    {
      "nombre": "Carnotaurus",
      "especie": "Theropoda",
      "peso": "1500 kg",
      "descubridor": "José Bonaparte",
      "ano_descubrimiento": 1985
    },
    {
      "nombre": "Styracosaurus",
      "especie": "Ceratopsidae",
      "peso": "2700 kg",
      "descubridor": "Lawrence Lambe",
      "ano_descubrimiento": 1913
    },
    {
      "nombre": "Therizinosaurus",
      "especie": "Therizinosauridae",
      "peso": "5000 kg",
      "descubridor": "Evgeny Maleev",
      "ano_descubrimiento": 1954
    },
    {
      "nombre": "Pteranodon",
      "especie": "Pterosauria",
      "peso": "25 kg",
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1876
    },
    {
      "nombre": "Quetzalcoatlus",
      "especie": "Pterosauria",
      "peso": "200 kg",
      "descubridor": "Douglas A. Lawson",
      "ano_descubrimiento": 1971
    },
    {
      "nombre": "Plesiosaurus",
      "especie": "Plesiosauria",
      "peso": "450 kg",
      "descubridor": "Mary Anning",
      "ano_descubrimiento": 1824
    },
    {
      "nombre": "Mosasaurus",
      "especie": "Mosasauridae",
      "peso": "15000 kg",
      "descubridor": "William Conybeare",
      "ano_descubrimiento": 1829
    },

  ]

dino_stack = Stack()
for dino in dinosaurios:
    dino_stack.push(dino)

#! A
def contar_especies(stack):
    especies = set()
    temp_stack = Stack()
    
    while stack.size() > 0:
        dino = stack.pop()
        especies.add(dino['especie'])
        temp_stack.push(dino)
    
    while temp_stack.size() > 0:
        stack.push(temp_stack.pop())
    
    return len(especies)

#! B
def contar_descubridores(stack):
    descubridores = set()
    temp_stack = Stack()
    
    while stack.size() > 0:
        dino = stack.pop()
        descubridores.add(dino['descubridor'])
        temp_stack.push(dino)
    
    while temp_stack.size() > 0:
        stack.push(temp_stack.pop())
    
    return len(descubridores)

#! C
def dinos_con_T(stack):
    result = []
    temp_stack = Stack()
    
    while stack.size() > 0:
        dino = stack.pop()
        if dino['nombre'].startswith('T'):
            result.append(dino)
        temp_stack.push(dino)
    
    while temp_stack.size() > 0:
        stack.push(temp_stack.pop())
    
    return result

#! D
def dinos_menos_de_275_kg(stack):
    result = []
    temp_stack = Stack()
    
    while stack.size() > 0:
        dino = stack.pop()
        peso_kg = int(dino['peso'].split()[0])
        if peso_kg < 275:
            result.append(dino)
        temp_stack.push(dino)
    
    while temp_stack.size() > 0:
        stack.push(temp_stack.pop())
    
    return result

#! E
def dinos_con_AQS(stack):
    aqs_stack = Stack()
    temp_stack = Stack()
    
    while stack.size() > 0:
        dino = stack.pop()
        if dino['nombre'].startswith(('A', 'Q', 'S')):
            aqs_stack.push(dino)
        else:
            temp_stack.push(dino)
    
    while temp_stack.size() > 0:
        stack.push(temp_stack.pop())
    
    return aqs_stack

#! A
print("Cantidad de especies:", contar_especies(dino_stack))
print()

#! B
print("Cantidad de descubridores distintos:", contar_descubridores(dino_stack))
print()

#! C
print("Dinosaurios que empiezan con T:", dinos_con_T(dino_stack))
print()

#! D
print("Dinosaurios que pesan menos de 275 kg:", dinos_menos_de_275_kg(dino_stack))
print()

#! E
aqs_pila = dinos_con_AQS(dino_stack)
print("Dinosaurios que comienzan con A, Q, S:")
while aqs_pila.size() > 0:
    print(aqs_pila.pop())