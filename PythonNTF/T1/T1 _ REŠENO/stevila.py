#______________________________________________________________________________
# Termin 1, 16.5.2019
# Števila in operacije na njih
#______________________________________________________________________________

x = 5
y = 3

# Imam podani dve števili, želim jih izpisat
print(x,y)
print()
# Izpisat želim vrednost x-a če bi se povečal za 1, 
# in vrednost y če bi se zmanjšal za 1
print(x+1)
print(y-1)
print()
#  y pa nastavi da bo enak x-u, Vrednost x povečaj za 7,, ter ju izpiši
# x = x + 7
y = x
x += 7

print(x,y)

# Izpiši vsoto obeh števil
print(x+y)

# Shrani to vsoto v novo neznanko z imenom z
z = x + y
print(z)
print()

# 2.
a = 4
b = 5
c = 94
# pod vsota shrani vsoto vseh treh števil
vsota1 =  a + b + c
print(vsota1)
# pod razlika shrani razliko med b in a
razlika = b - a
print(razlika)
# spremenljivka z imenom zmnožek naj bo enak zmnožku b in c
zmnožek = b * c
print(zmnožek)
# k1 naj bo rezultat pri deljenju c in a NATANČNO DELJENJE
k1 =  c / a
print(k1)
# k2 naj bo rezultat pri deljenju c in b NATANČNO DELJENJE
k2 = c / b
print(k2)
# k3 naj bo rezultat pri deljenju a in b CELO DELJENJE
k3 = a // b
print(k3)
o3 = a % b
print(o3)
# ost naj bo pa ostanke pri deljenju števila c z b
print(c,":",b,"=",c//b,"ostanek =",c % b)
ost = c/b
print(c,":",b,"=",c/b,"ostanek =",c % b)
print(ost, int(ost),round(ost))

pi = 3.14
e = 2.72
print("E je enako PI",round(pi),round(e))

# Števila lahko med seboj tudi primerjamo

x = 6.6
y = 6636/1000
print()

print(x,y)
# x == y preveri če sta števili enaki
print(x == y)
# x < y  preveri če je število x manjše od y
print (x < y)
# x <= y preveri če je število x manjše ali enako y
print (x <= y)
# x > y  preveri če je število x večje od y
print (x > y)
# x >= y preveri če je število x večje ali enako y
print (x >= y)
# x != y ali preveri če je število x različno oziroma ne enako y
print (x != y)
print(round(y,1))
print(x == round(y,1))

# 3.
# Izpiši kaj dobiš če primerjaš x in z od zgoraj za vse operacije 






