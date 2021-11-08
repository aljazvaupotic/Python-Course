#____________________________________________________________________
# TERMIN 4, 12.6.2019
# JSON
#____________________________________________________________________

import json

#json je sintaksa za shranjevanje in izmenjavo podatkov. V resnici je to .txt file, ki je zapisan z JavaScript notacijo.
# python zna spreminjati iz json kode v python  in iz python kode v json.

x = "{ "ime": "Janez", "starost": 27, "mesto" : "Maribor"}"

# to bomo iz json spremenili v pyton kodo

# kakšnega tipa je ?

m = { "država" : "Republika Slovenija", "kratica" : "SLO", "valuta" : "EURO"}

# iz python dict bomo sedaj te podatke oblikovali v json




o = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

# ob pretvorbi lahko tudi oblikujemo, da bo rezultat lažje berljiv.