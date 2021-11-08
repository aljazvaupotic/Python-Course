#______________________________________________________________________________
# Termin 1
# Pogojni stavek
#______________________________________________________________________________

# Ugotovili smo da primerjave nam za odgovor podajo tip boolean (True/False)
# To lahko uporabimo tako da programu naročimo da preveri če je nek pogoj pravilen
# potem izvede del kode drugače pa je ne

st1 = 315
st2 = 472
st3 = -23
st4 = 7

# Lahko imamo več kot en pogoj! Preverimo če je st2 večje, manjše ali enako 1,7,99
if (st2 < 1) :
	print(st2,"je manjse od 1")
elif ( st2 == 1):
	print( st2, "je enako 1")
else:
	print(st2, "je vecje od 1")

if( st3 > 7 or st3 == 99 or st3 < 1):
	print(st3, "je vecje od 7 ali enako 99 ali manjse od 1")

if( st4 == 7 and st4 > 99 and st4 > 1):
	print(st4, " je enako 7, hkrati je manjse od 99 in vecje od 1")
	
# V enem pogojnem stavko lahko preverimo več stvari
# Poglejmo če je število med 10 IN 15
if( st4 <= 15 and st4 >= 10):
	print("yay")
else:
	print("Nay")

# Preverimo če je s večji od 10 ALI manjši od 15 
if( st4 <= 15 or st4 >= 10):
	print("yay")
else:
	print("Nay")





# Vsi boksarji se morajo pred dvobojem stehtati. Ker nihče ne ve natanko
# v katero kategorijo kdo spada, so si organizatorji zaželeli novo
# supermoderno tehtnico, ki ob tehtanju izpiše ne le težo boksarja,
# temveč tudi v katero težnostno kategorijo sodi.  Napiši funkcijo
# `teznostna_kategorija(teza)` za pripadajoči program tehtnice, ki vrne podatek,
# v katero težnostno kategorijo sodi boksar. Boks je razdeljen na 11
# kategorij in sicer: 
#lahka mušja (do 48 kg), 
#mušja (do 51 kg), 
#bantam(do 54 kg), 
#peresna (do 57 kg), 
#lahka (do 60 kg), 
#lahka velterska(do 64 kg), 
#velterska (do 69 kg), 
#srednja (do 75 kg), 
#poltežka(do 81 kg), 
#težka (do 91 kg) ter 
#super težka (nad 91 kg).
# Za argumente
# manjše ali enake 0 naj funkcija vrne niz »Napaka!«.
# 
#     >>> teznostna_kategorija(54)
#     "bantamska kategorija"
#     >>> teznostna_kategorija(48.000001)
#     "mušja kategorija"

def teznostna_kategorija(x):
	if x <= 0:
		return("Napaka!")
	elif x < 48:
		return("Lahka mušja kategorija")
	elif x < 51:
		return("Mušja kategorija")
	elif x < 54:
		return("Bantam kategorija")
	elif x < 57:
		return("Peresna kategorija")
	elif x < 60:
		return("Lahka kategorija")
	elif x < 64:
		return("Lahka velterska kategorija")
	elif x < 69:
		return("Velterska kategorija")
	elif x < 75:
		return("Srednja kategorija")	
	elif x < 81:
		return("Poltežka kategorija")
	elif x < 91:
		return("Težka kategorija")
	else:
		return("Super težka kategorija")
print()
print(teznostna_kategorija(-5))				
print(teznostna_kategorija(52))
print(teznostna_kategorija(75))
print(teznostna_kategorija(74.9999))	