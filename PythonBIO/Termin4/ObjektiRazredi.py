#______________________________________________________________________________
# Objekti in razredi
# Termin 4
# 14/15.5.2019
#______________________________________________________________________________

# Python je objektno orientiran programski jezik,
# to pomeni, da so skoraj vse stvari, katere uporabljamo objekti
# vsak objekt ima svoje lastnosti (vrednosti) in metode
# Razred je konstruktro objekta, torej nekaj kar sestavlja objekt

#primer

class MojRazred :
	x = 5
	j = "Janez"

r1 = MojRazred()


# funkcija __init__() uporabljamo ko želimo določeim objektom 
# pripisati vrednosti, ki se bojo spreminjale

class Oseba:
	def __init__(self, ime, starost,spol):
		self.ime = ime
		self.starost = starost
		self. spol = spol
	def mFunkcija(self):
		print("Živjo, ime mi je " + self.ime + ", star sem " + str(self.starost))

# self je parameter ki se nanaša na trenutno instanco/ stanje tega razreda
# uporabljamo ga zato da se navezujemo na vrednosti v tem razredu()
# ime tega parametra nerabi biti self, mora pa biti prva podana spremenljivka 
# v definiciji funkcij

#Ustvari osebo 

# Spremeni starost osebe

# zbriši osebo


# dedovanje

# razred je starš drugemu razredu torej "otrok" bo podedoval njegove
# lastnosti -> variable
# otroku pa lahko dodamo nove lastnosti ki pa jih starš nebo imel

#class Oseba bo starš classu Student
# __init__ bo prepisal vrednosti iz starša razen če pokličemo funkcijo
# za starša
class Student(Oseba):
	def __init__(self, ime, starost,spol, letnik):
		Oseba.__init__(self,ime,starost,spol)
		self.letnik = letnik

#Ustvari študenta in mu daj vse potrebe parametra

