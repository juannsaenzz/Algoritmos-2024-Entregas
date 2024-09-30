
#! PUNTO 3
#! Saenz de Santa Maria, Juan Ignacio

#! ACLARACIÓN: en los puntos a, d, e, f, g, i: muestro toda la infromacion de los jedis ya que me
#! pareció lo correcto para el caso en que se necesiten datos para realizar alguna actividad en
#! concreto, aunque con una simple modificación se puede mostrar solamente el nombre.

jedis = [
    {
        "name": "Qui-Gon Jinn",
        "rank": "Jedi Master",
        "species": "Human",
        "master": "Tera Sinube/Count Dooku",
        "lightsaber_color": "Green",
        "homeworld": "Coruscant",
        "birth_year": "79ABY",
        "height": 1.93,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Obi-Wan Kenobi",
        "rank": "Jedi Master",
        "species": "Human",
        "master": "Qui-Gon Jinn/Yoda",
        "lightsaber_color": "Blue",
        "homeworld": "Stewjon",
        "birth_year": "57ABY",
        "height": 1.82,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Anakin Skywalker/Darth Vader",
        "rank": "Jedi Knight",
        "species": "Human",
        "master": "Obi-Wan Kenobi",
        "lightsaber_color": "Blue",
        "homeworld": "Tatooine",
        "birth_year": "41ABY",
        "height": 1.88,
        "to_darkside": True,
        "come_lightside": True
    },
    {
        "name": "Quinlan Vos",
        "rank": "Jedi Master",
        "species": "Human/Kiffar",
        "master": "Tholme",
        "lightsaber_color": "Green",
        "homeworld": "Kiffu",
        "birth_year": "59ABY",
        "height": 1.91,
        "to_darkside": True,
        "come_lightside": False
    },
    {
        "name": "Yoda",
        "rank": "Grand Master",
        "species": None,
        "master": None,
        "lightsaber_color": "Green",
        "homeworld": None,
        "birth_year": "896ABY",
        "height": 0.66,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Mace Windu",
        "rank": "Jedi Master/Master of the Order",
        "species": "Human",
        "master": "Cyslin Myr",
        "lightsaber_color": "Purple",
        "homeworld": "Haruun Kal",
        "birth_year": "72ABY",
        "height": 1.92,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Ki-Adi-Mundi",
        "rank": "Jedi Master",
        "species": "Cerean",
        "master": None,
        "lightsaber_color": "Purple/Blue",
        "homeworld": "Cerea",
        "birth_year": "92ABY",
        "height": 1.98,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Plo Koon",
        "rank": "Jedi Master",
        "species": "Kel Dor",
        "master": None,
        "lightsaber_color": "Yellow/Blue/Orange",
        "homeworld": "Dorin",
        "birth_year": "71ABY",
        "height": 1.88,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Saesee Tiin",
        "rank": "Jedi Master",
        "species": "Iktotchi",
        "master": None,
        "lightsaber_color": "Green",
        "homeworld": "Iktotch",
        "birth_year": None,
        "height": 1.93,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Yaddle",
        "rank": "Jedi Master",
        "species": None,
        "master": None,
        "lightsaber_color": "Green",
        "homeworld": None,
        "birth_year": "509AYB",
        "height": 0.61,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Even Piell",
        "rank": "Jedi Master",
        "species": "Lannik",
        "master": None,
        "lightsaber_color": "Green",
        "homeworld": "Lannik",
        "birth_year": None,
        "height": 1.22,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Oppo Rancisis",
        "rank": "Jedi Master",
        "species": "Thisspiasian",
        "master": "Yaddle",
        "lightsaber_color": "Green",
        "homeworld": "Thisspias",
        "birth_year": "206ABY",
        "height": 1.38,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Adi Gallia",
        "rank": "Jedi Master",
        "species": "Tholothian",
        "master": None,
        "lightsaber_color": "Green/Blue",
        "homeworld": "Coruscant",
        "birth_year": None,
        "height": 1.84,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Yarael Poof",
        "rank": "Jedi Master",
        "species": "Quermian",
        "master": None,
        "lightsaber_color": "Blue",
        "homeworld": "Quermia",
        "birth_year": None,
        "height": 2.64,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Eeth Koth",
        "rank": "Jedi Master",
        "species": "Zabrak",
        "master": None,
        "lightsaber_color": "Green/Blue",
        "homeworld": "Iridonia",
        "birth_year": None,
        "height": 1.71,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Depa Billaba",
        "rank": "Jedi Master",
        "species": "Chalactan",
        "master": None,
        "lightsaber_color": "Green",
        "homeworld": "Chalacta",
        "birth_year": None,
        "height": 1.68,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Kit Fisto",
        "rank": "Jedi Master",
        "species": "Nautolan",
        "master": None,
        "lightsaber_color": "Green",
        "homeworld": "Glee Anselm",
        "birth_year": None,
        "height": 1.96,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Luminara Unduli",
        "rank": "Jedi Master",
        "species": "Mirialan",
        "master": None,
        "lightsaber_color": "Green",
        "homeworld": "Mirial",
        "birth_year": "58ABY",
        "height": 1.76,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Barriss Offee",
        "rank": "Padawan",
        "species": "Mirialan",
        "master": "Luminara Unduli",
        "lightsaber_color": "Blue",
        "homeworld": "Mirial",
        "birth_year": "40ABY",
        "height": 1.66,
        "to_darkside": True,
        "come_lightside": False
    },
    {
        "name": "Shaak Ti",
        "rank": "Jedi Master",
        "species": "Togruta",
        "master": None,
        "lightsaber_color": "Blue",
        "homeworld": "Shili",
        "birth_year": None,
        "height": 1.87,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Coleman Trebor",
        "rank": "Jedi Master",
        "species": "Vurk",
        "master": None,
        "lightsaber_color": "Green",
        "homeworld": "Sembla",
        "birth_year": None,
        "height": 2.13,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Jocasta Nu",
        "rank": "Jedi Master",
        "species": "Human",
        "master": None,
        "lightsaber_color": "Blue",
        "homeworld": "Coruscant",
        "birth_year": None,
        "height": 1.69,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Aayla Secura",
        "rank": "Jedi Knight",
        "species": "Twi'lek",
        "master": "Quinlan Vos",
        "lightsaber_color": "Blue",
        "homeworld": "Ryloth",
        "birth_year": "47ABY",
        "height": 1.72,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Sifo-Dyas",
        "rank": "Jedi Master",
        "species": "Human",
        "master": None,
        "lightsaber_color": "Green",
        "homeworld": "Mundos Cassandranos",
        "birth_year": "75ABY",
        "height": None,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Count Dooku",
        "rank": "Jedi Master",
        "species": "Human",
        "master": "Yoda",
        "lightsaber_color": "Blue/Red",
        "homeworld": "Serenno",
        "birth_year": "102ABY",
        "height": 1.93,
        "to_darkside": True,
        "come_lightside": False
    },
    {
        "name": "Pablo-Jill",
        "rank": "Jedi Knight",
        "species": None,
        "master": None,
        "lightsaber_color": "Blue",
        "homeworld": "Cúmulo Estelar Skustell",
        "birth_year": None,
        "height": 1.60,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Bultar Swan",
        "rank": "Jedi Knight",
        "species": "Human",
        "master": "Plo Koon",
        "lightsaber_color": "Green",
        "homeworld": "Kuat",
        "birth_year": None,
        "height": 1.68,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Agen Kolar",
        "rank": "Jedi Master",
        "species": "Zabrak",
        "master": None,
        "lightsaber_color": "Green/Blue",
        "homeworld": "Coruscant",
        "birth_year": None,
        "height": 1.90,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Stass Allie",
        "rank": "Jedi Master",
        "species": "Tholothian",
        "master": None,
        "lightsaber_color": "Green",
        "homeworld": "Tholoth",
        "birth_year": None,
        "height": 1.80,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Ahsoka Tano",
        "rank": "Padawan",
        "species": "Togruta",
        "master": "Anakin Skywalker",
        "lightsaber_color": "Green/Yellow/Blue/White",
        "homeworld": "Shili",
        "birth_year": "36ABY",
        "height": 1.88,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Asajj Ventress",
        "rank": "Padawan",
        "species": "Dathomirian",
        "master": "Ky Narec",
        "lightsaber_color": "Yellow/Red",
        "homeworld": "Dathomir",
        "birth_year": None,
        "height": 1.80,
        "to_darkside": True,
        "come_lightside": False
    },
    {
        "name": "Ima-Gun Di",
        "rank": "Jedi Master",
        "species": "Nikto",
        "master": None,
        "lightsaber_color": "Blue",
        "homeworld": None,
        "birth_year": None,
        "height": 1.92,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Nahdar Vebb",
        "rank": "Jedi Knight",
        "species": "Mon Calamari",
        "master": "Kit Fisto",
        "lightsaber_color": "Blue",
        "homeworld": "Dac",
        "birth_year": None,
        "height": None,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Bolla Ropal",
        "rank": "Jedi Master",
        "species": "Rodian",
        "master": None,
        "lightsaber_color": "Blue",
        "homeworld": "Rodia",
        "birth_year": None,
        "height": 1.75,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Ord Enisence",
        "rank": "Jedi Master",
        "species": "Skrilling",
        "master": None,
        "lightsaber_color": "Green",
        "homeworld": "Agrimundo-2079",
        "birth_year": None,
        "height": 1.83,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Tera Sinube",
        "rank": "Jedi Master",
        "species": "Cosian",
        "master": None,
        "lightsaber_color": "Blue",
        "homeworld": "Cosia",
        "birth_year": "102ABY",
        "height": 1.83,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Ky Narec",
        "rank": "Jedi Master",
        "species": "Human",
        "master": None,
        "lightsaber_color": "Green",
        "homeworld": None,
        "birth_year": None,
        "height": None,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Pong Krell",
        "rank": "Jedi Master",
        "species": "Besalisk",
        "master": None,
        "lightsaber_color": "Blue/Green",
        "homeworld": "Ojom",
        "birth_year": None,
        "height": 2.36,
        "to_darkside": True,
        "come_lightside": False
    },
    {
        "name": "Coleman Kcaj",
        "rank": "Jedi Master",
        "species": "Ongree",
        "master": None,
        "lightsaber_color": "Green",
        "homeworld": "Skustell",
        "birth_year": None,
        "height": None,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Tiplar",
        "rank": "Jedi Master",
        "species": "Mikkian",
        "master": None,
        "lightsaber_color": "Green",
        "homeworld": None,
        "birth_year": None,
        "height": None,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Tiplee",
        "rank": "Jedi Master",
        "species": "Mikkian",
        "master": None,
        "lightsaber_color": "Blue",
        "homeworld": None,
        "birth_year": None,
        "height": None,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Tu-Anh",
        "rank": "Jedi Master",
        "species": "Human",
        "master": None,
        "lightsaber_color": None,
        "homeworld": None,
        "birth_year": None,
        "height": None,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Kanan Jarrus",
        "rank": "Jedi Master",
        "species": "Human",
        "master": "Depa Billaba",
        "lightsaber_color": "Blue",
        "homeworld": "Coruscant",
        "birth_year": "33ABY",
        "height": 1.90,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Ezra Bridger",
        "rank": "Padawan",
        "species": "Human",
        "master": "Kanan Jarrus",
        "lightsaber_color": "Blue",
        "homeworld": "Lothal",
        "birth_year": "19ABY",
        "height": 1.65,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Luke Skywalker",
        "rank": "Jedi Master",
        "species": "Human",
        "master": "Obi-Wan Kenobi/Yoda",
        "lightsaber_color": "Green/Blue",
        "homeworld": "Tatooine",
        "birth_year": "19ABY",
        "height": 1.72,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Leia Organa",
        "rank": "Jedi Master",
        "species": "Human",
        "master": "Luke Skywalker",
        "lightsaber_color": "Blue",
        "homeworld": "Alderaan",
        "birth_year": "19ABY",
        "height": 1.50,
        "to_darkside": None,
        "come_lightside": None
    },
    {
        "name": "Ben Solo/Kylo Ren",
        "rank": "Padawan",
        "species": "Human",
        "master": "Luke Skywalker",
        "lightsaber_color": "Green/Blue",
        "homeworld": "Chandrila",
        "birth_year": "5DBY",
        "height": 1.89,
        "to_darkside": True,
        "come_lightside": True
    },
    {
        "name": "Rey Skywalker",
        "rank": "Jedi Sentinel",
        "species": "Human",
        "master": "Luke Skywalker/Leia Organa",
        "lightsaber_color": "Blue/Green/Yellow",
        "homeworld": "Jakku",
        "birth_year": "15DYB",
        "height": 1.70,
        "to_darkside": None,
        "come_lightside": None
    }
 ]

#! A
def sort_by_name(jedis):
    return sorted(jedis, key=lambda x: x['name'])

def sort_by_species(jedis):
    return sorted(jedis, key=lambda x: x['species'] if x['species'] else '')

#! B
def show_jedi_info(jedis, name):
    for jedi in jedis:
        if jedi['name'] == name:
            return jedi
    return None

#! C
def find_padawans(jedis, master_name):
    padawans = []
    for jedi in jedis:
        if jedi['master'] and master_name in jedi['master']:
            padawans.append(jedi['name'])
    return padawans

#! D
def filter_by_species(jedis, species_list):
    return [jedi for jedi in jedis if jedi['species'] in species_list]

#! E
def jedis_starting_with_A(jedis):
    a_jedis = [jedi for jedi in jedis if jedi['name'].startswith('A')]
    a_jedis_sorted = sorted(a_jedis, key=lambda jedi: jedi['name'])
    enumerated_jedis = [(index, jedi) for index, jedi in enumerate(a_jedis_sorted)]
    return enumerated_jedis

#! F
def jedis_with_multiple_lightsaber_colors(jedis):
    return [jedi for jedi in jedis if jedi['lightsaber_color'] and '/' in jedi['lightsaber_color']]

#! G
def jedis_with_yellow_or_purple_lightsabers(jedis):
    return [jedi for jedi in jedis if jedi['lightsaber_color'] and ('Yellow' in jedi['lightsaber_color'] or 'Purple' in jedi['lightsaber_color'])]

#! H
def padawans_of_specific_masters(jedis):
    padawans = {}
    padawans['Qui-Gon Jinn'] = find_padawans(jedis, 'Qui-Gon Jinn')
    padawans['Mace Windu'] = find_padawans(jedis, 'Mace Windu')
    return padawans

#! I
def grand_masters(jedis):
    return [jedi for jedi in jedis if jedi['rank'] == 'Grand Master']


#! A
sorted_by_name = sort_by_name(jedis)
sorted_by_species = sort_by_species(jedis)

#! B
ahsoka_info = show_jedi_info(jedis, 'Ahsoka Tano')
kit_fisto_info = show_jedi_info(jedis, 'Kit Fisto')

#! C
yoda_padawans = find_padawans(jedis, 'Yoda')
luke_padawans = find_padawans(jedis, 'Luke Skywalker')

#! D
human_and_twilek_jedis = filter_by_species(jedis, ['Human', 'Twi\'lek'])

#! E
jedis_starting_A = jedis_starting_with_A(jedis)

#! F
multiple_colors_jedis = jedis_with_multiple_lightsaber_colors(jedis)

#! G
yellow_or_purple_jedis = jedis_with_yellow_or_purple_lightsabers(jedis)

#! H
specific_padawans = padawans_of_specific_masters(jedis)

#! I
grand_master_jedis = grand_masters(jedis)


#! A
print("Listado ordenado por nombre:")
for index, jedi in enumerate(sorted_by_name):
    print(f"{index}. {jedi}")
print()

print("Listado ordenado por especie:")
for index, jedi in enumerate(sorted_by_species):
    print(f"{index}. {jedi}")
print()

#! B
print("Información de Ahsoka Tano:")
print(ahsoka_info)
print()
print("Información de Kit Fisto:")
print(kit_fisto_info)
print()

#! C
print("Padawans de Yoda:")
print(yoda_padawans)
print()
print("Padawans de Luke Skywalker:")
print(luke_padawans)
print()

#! D
print("Jedis humanos y twi'lek:")
for jedi in human_and_twilek_jedis:
    print(jedi)
print()

#! E
print("Jedis que comienzan con A:")
for index, jedi in jedis_starting_A:
    print(f"{index}. {jedi}")
print()

#! F
print("Jedis con sable de más de un color:")
for jedi in multiple_colors_jedis:
    print(jedi)
print()

#! G
print("Jedis con sable amarillo o violeta:")
for jedi in yellow_or_purple_jedis:
    print(jedi)
print()

#! H
print("Padawans de Qui-Gon Jinn y Mace Windu:")
print(specific_padawans)
print()

#! I
print("Jedis con ranking de Grand Master:")
for jedi in grand_master_jedis:
    print(jedi)