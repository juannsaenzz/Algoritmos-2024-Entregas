
#! EJERCICIO 6

#! Dada una lista de superhéroes de comics, de los cuales se conoce su nombre,
#! año aparición, casa de comic a la que pertenece (Marvel o DC) y biografía,
#! implementar la funciones necesarias para poder realizar las siguientes actividades:

#! a. eliminar el nodo que contiene la información de Linterna Verde;
#! b. mostrar el año de aparición de Wolverine;
#! c. cambiar la casa de Dr. Strange a Marvel;
#! d. mostrar el nombre de aquellos superhéroes que en su biografía menciona la
#! palabra “traje” o “armadura”;
#! e. mostrar el nombre y la casa de los superhéroes cuya fecha de aparición sea
#! anterior a 1963;
#! f. mostrar la casa a la que pertenece Capitana Marvel y Mujer Maravilla;
#! g. mostrar toda la información de Flash y Star-Lord;
#! h. listar los superhéroes que comienzan con la letra B, M y S;
#! i. determinar cuántos superhéroes hay de cada casa de comic.

from lista import search, remove, by_name

def show_heroes(super_heroes):
    for heroe in super_heroes:
        print(f"Nombre: {heroe['nombre']}")
        print(f"Año de aparicion: {heroe['año_aparicion']}")
        print(f"Casa de comics: {heroe['casa_comic']}")
        print(f"Biografia: {heroe['biografia']}")
        print()

def show_info(heroe):
  print(f"Nombre: {heroe['nombre']}")
  print(f"Año de aparicion: {heroe['año_aparicion']}")
  print(f"Casa de comics: {heroe['casa_comic']}")
  print(f"Biografia: {heroe['biografia']}")
    
super_heroes = [
  {
    "nombre": "Linterna Verde",
    "año_aparicion": 1940,
    "casa_comic": "DC Comics",
    "biografia": "Miembro de la Tropa de Linternas Verdes, posee un anillo que le otorga poderes basados en la fuerza de voluntad."
  },
  {
    "nombre": "Wolverine",
    "año_aparicion": 1974,
    "casa_comic": "Marvel Comics",
    "biografia": "Mutante con garras retráctiles y habilidades regenerativas, miembro de los X-Men."
  },
  {
    "nombre": "Doctor Strange",
    "año_aparicion": 1963,
    "casa_comic": "Marvel Comics",
    "biografia": "Hechicero supremo del universo Marvel, maestro de las artes místicas y protector de la realidad."
  },
  {
    "nombre": "Capitana Marvel",
    "año_aparicion": 1968,
    "casa_comic": "Marvel Comics",
    "biografia": "Heroína cósmica con poderes de vuelo, fuerza sobrehumana y energía cósmica."
  },
  {
    "nombre": "Mujer Maravilla",
    "año_aparicion": 1941,
    "casa_comic": "DC Comics",
    "biografia": "Princesa amazona y una de las principales defensoras de la justicia y la igualdad en el Universo DC."
  },
  {
    "nombre": "Flash",
    "año_aparicion": 1940,
    "casa_comic": "DC Comics",
    "biografia": "Velocista con la capacidad de correr a velocidades superiores a la luz, miembro de la Liga de la Justicia."
  },
  {
    "nombre": "Star-Lord",
    "año_aparicion": 1976,
    "casa_comic": "Marvel Comics",
    "biografia": "Líder de los Guardianes de la Galaxia, experto en combate y estrategia intergaláctica."
  },
  {
    "nombre": "Superman",
    "año_aparicion": 1938,
    "casa_comic": "DC Comics",
    "biografia": "El Hombre de Acero, uno de los héroes más icónicos de DC con superpoderes sobrehumanos."
  },
  {
    "nombre": "Batman",
    "año_aparicion": 1939,
    "casa_comic": "DC Comics",
    "biografia": "El Caballero Oscuro, detective y luchador experto que protege Gotham City."
  },
  {
    "nombre": "Iron Man",
    "año_aparicion": 1963,
    "casa_comic": "Marvel Comics",
    "biografia": "Tony Stark, genio multimillonario y superhéroe con una armadura tecnológica de alta tecnología."
  },
  {
    "nombre": "Wonder Woman",
    "año_aparicion": 1941,
    "casa_comic": "DC Comics",
    "biografia": "La princesa amazona Diana, guerrera y defensora de la paz y la justicia en el mundo."
  },
  {
    "nombre": "Spider-Man",
    "año_aparicion": 1962,
    "casa_comic": "Marvel Comics",
    "biografia": "Peter Parker, joven héroe con habilidades arácnidas tras ser picado por una araña radiactiva."
  },
  {
    "nombre": "Thor",
    "año_aparicion": 1962,
    "casa_comic": "Marvel Comics",
    "biografia": "Dios nórdico del trueno y miembro de los Vengadores, posee un martillo encantado llamado Mjolnir."
  },
  {
    "nombre": "Aquaman",
    "año_aparicion": 1941,
    "casa_comic": "DC Comics",
    "biografia": "Rey de Atlantis con la capacidad de comunicarse con la vida marina y controlar el agua."
  },
  {
    "nombre": "Green Arrow",
    "año_aparicion": 1941,
    "casa_comic": "DC Comics",
    "biografia": "Oliver Queen, arquero habilidoso y defensor de la justicia con su arco y flechas."
  },
  {
    "nombre": "Hulk",
    "año_aparicion": 1962,
    "casa_comic": "Marvel Comics",
    "biografia": "Bruce Banner, científico transformado en monstruo verde con fuerza increíble."
  },
  {
    "nombre": "Black Widow",
    "año_aparicion": 1964,
    "casa_comic": "Marvel Comics",
    "biografia": "Natasha Romanoff, espía rusa y experta en combate mano a mano y armas."
  },
  {
    "nombre": "Mr. Fantástico",
    "año_aparicion": 1961,
    "casa_comic": "Marvel Comics",
    "biografia": "Líder de los 4 Fantásticos, científico brillante con la capacidad de estirar y deformar su cuerpo."
  },
  {
    "nombre": "La Mujer Invisible",
    "año_aparicion": 1961,
    "casa_comic": "Marvel Comics",
    "biografia": "Miembro de los 4 Fantásticos, posee el poder de hacerse invisible y crear campos de fuerza."
  },
  {
    "nombre": "La Antorcha Humana",
    "año_aparicion": 1961,
    "casa_comic": "Marvel Comics",
    "biografia": "Miembro de los 4 Fantásticos, puede envolverse en llamas y volar a altas velocidades."
  },
  {
    "nombre": "La Cosa",
    "año_aparicion": 1961,
    "casa_comic": "Marvel Comics",
    "biografia": "Miembro de los 4 Fantásticos, posee una fuerza y resistencia sobrehumanas, con piel rocosa."
  },
  {
    "nombre": "Capitán América",
    "año_aparicion": 1941,
    "casa_comic": "Marvel Comics",
    "biografia": "El supersoldado Steve Rogers, símbolo de libertad y justicia con escudo indestructible."
  },
  {
    "nombre": "Ant-Man",
    "año_aparicion": 1962,
    "casa_comic": "Marvel Comics",
    "biografia": "Hank Pym o Scott Lang, héroes capaces de cambiar de tamaño y comunicarse con insectos."
  }
]

#! A
remove(super_heroes, 'nombre', 'Linterna Verde')

#! B
index_wolverine = search(super_heroes, 'nombre', 'Wolverine')
if index_wolverine is not None:
    año_wolverine = super_heroes[index_wolverine]['año_aparicion']
    print(f'El año de aparicion de Wolverine es {año_wolverine}')
else:
    print('Wolverine no se encuentra en la lista')

#! C
index_dr_strange = search(super_heroes, 'nombre', 'Doctor Strange')
if index_dr_strange is not None:
    super_heroes[index_dr_strange]['casa_comic'] = 'Marvel'

#! D
print()
print('Superheroes que en su biografia tienen la palabra traje o armadura:')
for index, heroe in enumerate(super_heroes):
    if "traje" in heroe["biografia"] or "armadura" in heroe["biografia"]:
        print(index, heroe['nombre'])

#! E
print()
print('Superheroes cuya fecha de aparicion es anterior a 1963:')
for index, heroe in enumerate(super_heroes):
    if heroe['año_aparicion'] < 1963:
        print(f"{index} Nombre: {heroe['nombre']}, Casa Comic: {heroe['casa_comic']}")

#! F
print()
index_capitana_marvel = search(super_heroes, 'nombre', 'Capitana Marvel')
if index_capitana_marvel is not None:
    casa_capitana_marvel = super_heroes[index_capitana_marvel]['casa_comic']
    print(f'La casa de comic de Capitana Marvel es {casa_capitana_marvel}')
else:
    print('Capitana Marvel no se encuentra en la lista')

index_mujer_maravilla = search(super_heroes, 'nombre', 'Mujer Maravilla')
if index_mujer_maravilla is not None:
    casa_mujer_maravilla = super_heroes[index_mujer_maravilla]['casa_comic']
    print(f'La casa de comic de Mujer Maravilla es {casa_mujer_maravilla}')
else:
    print('Mujer Maravilla no se encuentra en la lista')

#! G
print()
index_flash = search(super_heroes, 'nombre', 'Flash')
if index_flash is not None:
    print(show_info(super_heroes[index_flash]))
else:
    print('Flash no se encuentra en la lista')

print()
index_starlord = search(super_heroes, 'nombre', 'Star-Lord')
if index_starlord is not None:
    print(show_info(super_heroes[index_starlord]))
else:
    print('Star-Lord no se encuentra en la lista')

#! H
print()
iniciales = ['B', 'M', 'S']
lista_bms = []

for heroe in super_heroes:
    if heroe['nombre'][0] in iniciales:
        lista_bms.append(heroe)

lista_bms.sort(key=by_name)
print('Listado de superheroes que comienzan con las letra B, M o S:')
show_heroes(lista_bms)

#! I
print()
dic_contador= {}

for heroe in super_heroes:
    casa_comic = heroe['casa_comic']
    if casa_comic in dic_contador:
        dic_contador[casa_comic] += 1
    else:
        dic_contador[casa_comic] = 1

print('Cantidad de superheroes por cada casa de comic:')
for casa_comic, cantidad in dic_contador.items():
    print(f"{casa_comic}: {cantidad}")

print()
print("Lista de superheroes actualizada:")
show_heroes(super_heroes)