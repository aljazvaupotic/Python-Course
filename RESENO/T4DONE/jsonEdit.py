#!/usr/bin/env python
# -*- coding: utf-8 -*-
#____________________________________________________________________
# TERMIN 4, 
# JSON
#____________________________________________________________________

import json

#json je sintaksa za shranjevanje in izmenjavo podatkov. V resnici je to .txt file, ki je zapisan z JavaScript notacijo.
# python zna spreminjati iz json kode v python  in iz python kode v json.

x = '{ "ime": "Janez", "starost": 27, "mesto" : "Maribor"}'
print(x)
y = json.loads(x)
print(type(x))
print(y["mesto"])
print(type(y))

# to bomo iz json spremenili v pyton kodo

# kakšnega tipa je ?

m = { "drzava" : "Republika Slovenija", "kratica" : "SLO", "valuta" : "EURO"}
print(m)
print(type(m))
n = json.dumps(m)
print(n)
print(type(n))
# iz python dict bomo sedaj te podatke oblikovali v json


# ob pretvorbi lahko tudi oblikujemo, da bo rezultat lažje berljiv.
o = {
	"name" : "John",
	"age" : 30,
	"married" : True,
	"divorced" : False,
	"children" : ("Ann","Billy"),
	"cars" : [
		{"model": "BMW 230", "mpg" : 27.5},
		{"model": "Ford Edge", "mpg" : 19.6}
	]
}
print(o)
print()
fp = open("j.txt","w")
fp.write(json.dumps(o, indent = 4, separators = ("."," = ")))
fp.close()




