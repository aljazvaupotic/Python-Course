#!/usr/bin/env python
# -*- coding: utf-8 -*-

#______________________________________________________________________________
# TERMIN 3     
# 
#______________________________________________________________________________


# Do sedaj smo spoznali tipe: int,float,str,list,bool

x = 4  # int 
y = 4.0 # float
z = "4" # str
f =  x != 3 #bool
a = [1,"pet",True] #list

# Obstajajo še 3je tipi, ki jih večkrat uporabljamo
# tuple , set ,dict

# List je zbirka, ki je urejena in zamenljiva. Dovoli podvajanje elementov.
# Tuple je zbirka, ki je urejena in nezamenljiva Dovoli podvajanje elementov.
# Set je zbirka, ki je neurejena in neindexirana. Ne dovoli podvajanje elementov.
# Dictionary je zbirka, ki je neurejena, zamenljiva in indexirana. Ne dovoli podvajanje elementov.

l = ["jabolko","banana","jagoda"] # http://prntscr.com/o0d0tw
t = ("jabolko","banana","jagoda") # http://prntscr.com/o0d14p
s = {"jabolko","banana","jagoda"} # http://prntscr.com/o0d1d4
d = {   "ime"       : "jabolko", 
        "poreklo"   : "SLO" ,
        "barva"     : "rdeča"
} # http://prntscr.com/o0d1li




print("Dostop do elementov")
#Kako dostopamo do elementov:
print()
print("LIST")
# LIST 
# Izpiši samo en element:
print(l[2])

# Izpiši cel list:
print(l)
for el in l:
	print(el)
	
	
# TUPLE
print()
print("TUPLE")
# Izpiši samo en element:
print(t[0])

# Izpiši cel tuple:
print(t)
for el in t:
	print(el)
	
print()
print("SET")	

# SET
# Izpiši samo en element:
if "jagoda" in s :
	print("jagoda")

# Izpiši cel set:
print(s)
for el in s:
	print(el)

# DICT
print()
print("DICT")
# Izpiši samo en element:
print(d.get("uzitna"))
print(d["ime"])
# Izpiši cel dict:
print(d)

# samo po ključih
for el in d:
	print(el)
	
# po vrednostih
for el in d:
	print(d[el])

for el in d.items() :
	print(el)

for key, value in d.items():
	print(key, value)
	
#Preverimo če element obstaja v tej spremenljivki:
print()
print("OBSTOJ")

#list
if "banana" in l:
	print("BANANANA")
#tuple
if "jagoda"  in t:
	print("JAAAGODA")
if "marelica" in t:
	print("Marelica je!")
else:
	print("Marelica ni!")
#set
if "jagoda" in s :
	print("jagoda")

#dict
print()
if "ime" in d:
	print("KLJUČ OBSTAJA")

for x in d.items():
	if "SLO" in x:
		print("Obstaja vrednost SLO")

# Dolžina spremenljivke:
print()
print("DOLŽINA")

#list
print(len(l))
#tuple
print(len(t))
#set
print(len(s))
#dict
print(len(d))

# Dodajanje elementov
print()
print("DODAJANJE")
#list
print(l)
l.append("melona")
print(l)
l.insert(1,"kivi")
print(l)
l += ["ananas","papaja"]
print(l)
l.append("jabolko")
print(l)

#tuple
#NI MOGOČE 
#set
print()
print(s)
s.add("melona")
s.add("kivi")
print(s)
s.add("jabolko")
print("DODAL SEM JABOLKO")
print(s)


#dict
print()
print(d)
d["teža"] = 5
print(d)
d["ime"] = "hruška"
print(d)

# Brisanje elementov
print()
print("BRISANJE")
#list
print(l)
l.remove("jabolko")
print(l)
l.pop(2)
print(l)
del(l[4])
print(l)
l.clear()
print(l)

#tuple
#NI MOGOČE


#set
print()
print(s)
s.remove("jabolko")
print(s)
s.pop()
print(s)
s.discard("banana")
print(s)
s.clear()
print(s)

#dict
print()
print(d)
d.pop("ime")
print(d)
d.popitem()
print(d)

