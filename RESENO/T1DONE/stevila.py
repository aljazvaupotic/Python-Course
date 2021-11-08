#______________________________________________________________________________
# Termin 1
# Števila in operacije na njih
#______________________________________________________________________________

x = 5
y = 3

# Imam podani dve števili, želim jih izpisat
print(x,y)


# Izpisat želim vrednost x-a če bi se povečal za 1, 
# in vrednost y če bi se zmanjšal za 1
print(x+1,y-1)

#  y pa nastavi da bo enak x-u, Vrednost x povečaj za 7,, ter ju izpiši
y = x
x += 7 #x = x + 7
print(x, y)

# Izpiši vsoto obeh števil
print( x + y ) 

# Shrani to vsoto v novo neznanko z imenom z
z = x+y
print()
print(z)

# 2.
a = 4
b = 5
c = 94
# pod vsota shrani vsoto vseh treh števil
vsota = a + b + c
print(vsota)
# pod razlika shrani razliko med b in a
razlika = b - a
print(razlika)

# spremenljivka z imenom zmnožek naj bo enak zmnožku b in c
zmnožek = b * c
print(zmnožek)

# k1 naj bo rezultat pri deljenju c in a NATANČNO DELJENJE
k1 = c / a
print(k1)

# k2 naj bo rezultat pri deljenju c in b NATANČNO DELJENJE
k2 = c / b
print(k2)

# k3 naj bo rezultat pri deljenju a in b CELO DELJENJE

k3 = c // b
print(k3)


# ost naj bo pa ostanke pri deljenju števila c z b
ost = c % b
print(ost)
print()

# Števila lahko med seboj tudi primerjamo
x = 7
y = 2
# x == y preveri če sta števili enaki
print( x == y)
# x < y  preveri če je število x manjše od y
print( x < y )
# x <= y preveri če je število x manjše ali enako y
print( x <= y ) 
# x > y  preveri če je število x večje od y
print( x > y ) 
# x >= y preveri če je število x večje ali enako y
print( x >= y )
# x != y ali preveri če je število x različno oziroma ne enako y
print( x != y )

# 3.
# Izpiši kaj dobiš če primerjaš x in z od zgoraj za vse operacije 

print()
print("Decimalna stevila")

# DEDCIMALNA ŠTEVILA
print(type(18/6))
print(18/6)
x = 5.0198789789789797987564654
print(x)
print(float(x))

y = 12.75784564657976545646154
print(y)
print(int(y))
print(type(round(y)))
print(type(round(y,3)))


if(round(x) == 5.0):
	print("X je 5!")




















