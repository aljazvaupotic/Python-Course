#!/usr/bin/env python
# -*- coding: utf-8 -*-
#____________________________________________________________________
# TERMIN 4, 
# naloge1
#____________________________________________________________________
x = 5
y = 6.3
f = "Hi"

print(type(x),type(f))

if isinstance(str(x),str):
	print("Je int")
else:
	print("Ni int")
# Sestavi funkcijo  `precisti_seznam(seznam)`,
# ki iz seznama umakne vse elemente kateri niso števila.
def precistiSeznam(seznam):
	seznamInt = []
	for el in seznam:
		if isinstance(el,float) or isinstance(el,int):
			seznamInt.append(el)
	return seznamInt
	
print(precistiSeznam([1,4,6,87,342.23,"ejhakl","kal","5"]))




# =============================================================================
# Nepadajoča zaporedja
#
# Končno zaporedje celih števil $a_1, a_2, \ldots, a_n$ ($n \ge 1$)
# je _nepadajoče_, če velja $a_i \le a_{i+1}$ za vsak $i=1, \ldots, n-1$.
# Takšno zaporedje podamo s seznamom. Na primer,
# 
#     [-3, -1, 0, 5, 7, 8]
# 
# je nepadajoče zaporedje.
# =====================================================================@015287=
# 1. podnaloga
# Sestavite funkcijo `nepadajoce(s)`, ki prejme končno zaporedje celih
# števil in preveri, ali je zaporedje nepadajoče. Primer:
# 
#     >>> nepadajoce([1, 2, 3])
#     True
#     >>> nepadajoce([-1, 3, 2])
#     False
# =============================================================================

def nepadajoca(seznam):
	dolzina = len(seznam)
	i = 1
	while i < dolzina and seznam[i] >= seznam[i-1] :
		i += 1
	if i == dolzina :
		return True
	return False
print(nepadajoca([1, 2, 3, -1, 5,6]))



# =====================================================================@015288=
# 2. podnaloga
# Dano zaporedje celih števil $a_1, a_2, \ldots, a_n$ lahko _nagnemo_,
# tako da dobimo zaporedje $a_1, a_2 + 1, a_3 + 2, \ldots, a_n + (n-1)$.
# 
# Sestavite funkcijo `nagni(s)`, ki kot argument dobi zaporedje `s` in
# vrne pripadajoče nagnjeno zaporedje. Primer:
# 
#     >>> nagni([2, 4, 1])
#     [2, 5, 3]
#     >>> nagni([4, 0, 5, 5])
#     [4, 1, 7, 8]
# =============================================================================
def nagni(s):
	c = 0
	for el in s:
		s[c] = el + c
		c += 1
	return s
arr = [2, 4, 1]
print()
print(arr)
print(nagni(arr))

def nagniN(s):
	for i,el in enumerate(s):
		el += i

	return s
print(nagniN(arr))
# =============================================================================
# Delo z več seznami
#
# V tem sklopu so naloge pri katerih je potrebno vzporeno indeksiranje
# po dveh enako dolgih seznamih.
# =====================================================================@015255=
# 1. podnaloga
# Sestavite funkcijo `vektorsko_sestevanje(vec1, vec2)`, ki sešteje vektorja
# `vec1` in `vec2`. Funkcija naj za enako dolga seznama števil `vec1` in `vec2`
# vrne seznam `vec3`, ki vsebuje seštevke za pripadajoče komponente.
# 
# Primer:
# 
#     >>> vektorsko_sestevanje([1,2,3], [8,55,-4])
#     [9, 57, -1]
#     >>> vektorsko_sestevanje([1,2,3,4,5], [8,55,-4,7,7])
#     [9, 57, -1, 11, 12]
# =============================================================================
print()
def vektorjskoS (v1,v2):
	v3 = []
	if len(v1) != len(v2):
		print("Popravi dolzino vektorjev")
		return v3
	for i in range(len(v1)) :
		if (isinstance(v1[i],int) or isinstance(v1[i],float))  and  (isinstance(v2[i],int) or isinstance(v2[i],float)):
			v3.append(v1[i] + v2[i])
	if len(v1) != len(v3):
		print("Izbriši stringe")
		return 0
	return v3
	
	
v1 = [1,2,3]
v2 = [8,55,-1]

print(vektorjskoS(v1,v2))	

# =====================================================================@015256=
# 2. podnaloga
# Sestavite funkcijo `skalarni_produkt(vec1, vec2)`, ki za vektorja `vec1` in
# `vec2` vrne njun skalarni produkt. Funkcija naj za enako dolga seznama števil
# `vec1` in `vec2` vrne vsoto vseh pripadajočih produktov elementov prvega in 
# drugega seznama.
# Matematični primer
# `(1,2,3) * (7,8,9) = 1*7 + 2*8 + 3*9 = 7 + 16 + 27 = 50`
# Primer:
# 
#     >>> skalarni_produkt([1,2,3], [7,8,9])
#     50
# =============================================================================

def skalar(v1,v2):
	produkt = 0
	i = 0
	while i < len(v1):
		produkt += v1[i] * v2[i]
		i += 1
	return produkt
print(skalar(v1,v2))
	
x = 5
print(x)
x += 2+2
print(x)











