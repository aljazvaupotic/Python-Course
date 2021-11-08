#____________________________________________________________________
# TERMIN 4, 12.6.2019
# JSON
#____________________________________________________________________

import json

#json je sintaksa za shranjevanje in izmenjavo podatkov. V resnici je to .txt file, ki je zapisan z JavaScript notacijo.
# python zna spreminjati iz json kode v python  in iz python kode v json.

x = '{ "ime": "Janez", "starost": 27, "mesto" : "Maribor"}'

# to bomo iz json spremenili v pyton kodo
print(x)
print(type(x))
y = json.loads(x)
# kakšnega tipa je ?
print(y)
print(y["mesto"])
print(type(y))

m = { "država" : "Republika Slovenija", "kratica" : "SLO", "valuta" : "EURO"}

# iz python dict bomo sedaj te podatke oblikovali v json
n = json.dumps(m)
print(m)
print(type(m))
print()
print(n)
print(type(n))

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

print(json.dumps(o))
print()
print(json.dumps(o, indent = 4))
print()
print(json.dumps(o,indent = 4, separators=("." , " = ")))
