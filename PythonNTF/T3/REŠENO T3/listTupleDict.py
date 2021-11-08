#______________________________________________________________________________
# TERMIN 3      11.6.2019
# Slovarji
#______________________________________________________________________________


# Do sedaj smo spoznali tipe: int,float,str,list,bool

x = 4  # int 
y = 4.0 # float
z = "4" # str
f =  x < 3 #bool
a = [1,"pet",True] #list
print(type(x),type(y),type(z),type(f),type(a),type(a[1]))
# Obstajajo še 3je tipi, ki jih večkrat uporabljamo
# tuple , set ,dict

# List je zbirka, ki je urejena in zamenljiva. 
# Dovoli podvajanje elementov.

# Tuple je zbirka, ki je urejena in nezamenljiva 
# Dovoli podvajanje elementov.

# Set je zbirka, ki je neurejena in neindexirana.
# Ne dovoli podvajanje elementov.

# Dictionary je zbirka, ki je neurejena, zamenljiva in indexirana.
# Ne dovoli podvajanje elementov.

l = ["jabolko","banana","jagoda"] # http://prntscr.com/o0d0tw
t = ("jabolko","banana","jagoda") # http://prntscr.com/o0d14p
s = {"jabolko","banana","jagoda"} # http://prntscr.com/o0d1d4
d = {   "ime"       : "jabolko", 
        "poreklo"   : "SLO" ,
        "barva"     : "rdeča"
} # http://prntscr.com/o0d1li




print()

print("Dostopanje do elementov")
#Kako dostopamo do elementov:

# LIST 
# Izpiši samo en element:
print(l[0])

# Izpiši cel list:
print(l)

for el in l :
	print(el)
print()

# TUPLE
# Izpiši samo en element:
print(t[0])

# Izpiši cel tuple:
print(t)

for el in t :
	print(el)

print()
# SET
# Izpiši samo en element:
if "jagoda" in s:
	print("jagoda")
#print("jagoda" in s)

# Izpiši cel set:

print(s)

for el in s:
	print(el)

print()

# DICT

# Izpiši samo en element:
print(d.get("priimek"))

# Izpiši cel dict:
print(d)

# ta se sprehaja po ključih
for el in d:
	print(el)
# ta se pa sprehaja po vrednostih

for el in d:
	print(d[el])



#Preverimo če element obstaja v tej spremenljivki:

#list
if "banana" in l:
	print("Banana obstaja")
#tuple
if "jagoda" in t:
	print("Jagoda obstaja")
if "marelica" in t:
	print("Marelica je")
else:
	print("Marelice ni!")
#set
if "jagoda" in s:
	print("Jagoda obstaja")
#dict

print()
if "ime" in d:
	print("Ključ ime obstaja")
else:
	print("Ni ga")

for x in d.items():
	if "SLO" in x:
		print("obstaja")


# Dolžina spremenljivke:

#list
print(len(l))
#tuple
print(len(t))
#set
print(len(s))
#dict
print(len(d))

print()
# Dodajanje elementov

#list
print(l)
l.append("melona")
print(l)
l.insert(1,"kivi")
l.insert(1,"hruška")
l.append("jagoda")
print(l)



#tuple JE TO NEMOGOČE

#set
print()
print(s)
s.add("melona")
print(s)
s.add("jabolko")
print(s,"tukaj sem dodal še eno jabolko")
print()
#dict
print(d)
d["teža"] = 5
print(d)
d["ime"] = "Hruška"
print(d)


# Brisanje elementov

print()
print(	)
#list
print(l)
del(l[3])
print(l)
l.pop() # odstrani zadnji element
l.pop(0) # element na indexu 0 (prvi v seznamu)
x = "melona"
l.remove(x) # element na neznanem indexu, ki ima vrednost x
print(l)
l.clear()
print(l)

#tuple TEGA NI

#set
print()
print(s)
s.remove("jabolko")
print(s)
s.discard("banana")
print(s)
s.pop()
print(s)
s.clear()
print(s)


#dict
print()
print(d)
d.pop("poreklo")
print(d)
d.popitem()
print(d)



