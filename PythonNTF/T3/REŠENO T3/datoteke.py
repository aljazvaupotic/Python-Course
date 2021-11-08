#______________________________________________________________________________
# TERMIN 3      11.6.2019
# Datoteke
#______________________________________________________________________________


# odpremo lahko že obstoječo ali pa novo datoteko
# pazimo da sta že obstoječa datoteka in naš program v isti mapi! če nista moramo dodati pravilno pot (path)

# Datoteko lahko :
#		- beremo (prevzeta vrednost, odpre datoteko za branje, error če ta ne obstaja)
#		- dodajamo (odpre datoteko z možnostjo dodajanja, če ne obstaja jo ustvari)
#		- pišemo (odpre datoteko za pisanje, prav tako jo ustvari če ne obstaja)
#		- ustvarimo (ustvari datoteko, error če ta obstaja)


#lahko še dodamo tip datoteke (text ali binary)

datoteka = open("demo.txt","r")

# Branje datoteke
vsebina = datoteka.readline()
vsebina2 = datoteka.readline()
print(vsebina)
print(vsebina2)

# Zapiranje datoteke
datoteka.close()

#1. Odpri datoteko tekst1.txt in izpiši vsako drugo vrstico.
branaDatoteka = open("tekst1.txt","r")
for index,vrstico in enumerate(branaDatoteka):
	if index % 2 == 0:
		print(vrstico.strip())

#2. Odpri datoteko dict.txt in preštej koliko krat 
#	se pojavi katera beseda. 
#  (Ločuj med velikimi začetnicami in malimi)

print()

fp = open("dict.txt","r")

poved = fp.read()
print(poved)
sb = poved.split(" ")
print(sb)

d = {}
# za besedo v seznamu besed bomo preverjali
# ali ta beseda že obstaja kot ključ v našem slovarju d
for b in sb:
	dodaj = 0
	#print(b,"primerjam s:")
	for kljuc,vrednost in d.items():
		#print(kljuc)
	
		if(b.lower() == kljuc):# če obstaja v slovarju bomo dodali število ponovitev
			dodaj = vrednost
	for kljuc,vrednost in d.items():
		print(kljuc,vrednost)
	print()
	# če ne obstaja pa bomo na konec slovarja dodali nov ključ = b in 1 ponovitev
	d[b.lower()] = 1 + dodaj
print()
for kljuc,vrednost in d.items():
	print(kljuc,vrednost)













