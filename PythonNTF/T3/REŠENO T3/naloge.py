#______________________________________________________________________________
# TERMIN 3      11.6.2019
# Naloge
#______________________________________________________________________________




# 1. Ustvari seznam Sadje, katerega elementi so sadezi.
# Sadez naj vsebuje ime in informacijo o tem ali ima koščice ali ne (jagoda nima, jabolko ima =D )

class sadez:
	def __init__(self,ime,k):
		self.ime = ime
		self.k = k

sadje = [] 
# FUNKICJA ZA DUPLIKATE
def neobstaja(ime):
	global sadje
	for s in sadje:
		if ime.capitalize() == s.ime:
			return False
	return True

# 2. Ustvari funkcijo, ki bo dodajala elemente v seznam. Izmisli si tudi 5 
def dodaj(ime,k):
	global sadje
	s = sadez(ime.capitalize(),k.upper())
	if s.k != "DA" and s.k != "NE":
		s.k = input("Vnesi ali ima sadež "+ s.ime + " koščice! (DA/NE)")
		s.k = s.k.upper()
	if neobstaja(s.ime) :
		sadje.append(s)

dodaj("Lubenica","Da")
dodaj("malina","Ne")
dodaj("baNANA","ne")
dodaj("jagoda","ne")
dodaj("jabolko","da")

#for x in sadje :
#	print(x.ime,x.k)


# 3. V seznamu preštej, koliko sadežev nima koščic.
st = 0
for p in sadje:
	if p.k == "NE" :
		st += 1
print()
#print(st)

# 4. Uporabnik naj doda še en sadež 


def vnos(u):
	u = u.split(" ")
	#print(u)
	dolzina = len(u)
	imeS = ""
	for x in range(dolzina - 1):
		imeS += u[x] + " "
	koscice = u[dolzina-1]

	imeS = imeS.capitalize().strip()
	koscice = koscice.upper()
	dodaj(imeS,koscice)


u = input("Vnesi ime sadeža in ali ima koščice (DA/NE) ")
vnos(u)
#us = input("Vnesi ime sadež ")
#uk = input("Ali ima ta sadež koščice (DA/NE) ")
print()
#for x in sadje :
#	print(x.ime,x.k)


# 5. Iz datoteke sadje.txt preberi sadeže, 
# preveri: če sadež obstaja ga preskoči drugače dodaj.
fp = open("sadje.txt","r")

for line in fp:
	vnos(line.strip())

# 6 Izpiši imena sadežev.
for x in sadje :
	print(x.ime,x.k)


# Ta novi seznam pa želimo zapisat v datoteko sadjeVTrgovini.txt
import datetime as dt
ura = dt.datetime.now()
ura = ura.strftime("%d-%m-%y-%H%malina")
datoteka = "sadjeVTrgoviniOb"+str(ura)+".txt"
pisanje = open(datoteka,"w")

for s in sadje:
	pisanje.write(s.ime+ " " + s.k + "\n")
pisanje.close()



