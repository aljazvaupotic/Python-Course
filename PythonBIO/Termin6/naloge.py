#______________________________________________________________________________
# TERMIN 6 5/6 Junij 2019
# 
#______________________________________________________________________________
#tiny.cc/PYNTF

# Različni tipi spremenljivk, operacije na njih in med njimi.
  

# 1. Ustvari x,y,z. Vsi naj imajo vrednost isto vrednost (št. med 1-10).
# x naj bo besedni niz, y naj bo celo število, z naj bo decimalno število

x = str(5) # "5"
y = 5 # int(5)
z = float(5) # 5.

print(type(x),type(y),type(z))

# 2. Na 3 različne načine izpiši niza "Python" in "je lahek programski jezik."


print("Python","je lahek programski jezik.")
print("Python"+ " " + "je lahek programski jezik.")
print("Python je lahek programski jezik.")
niz1 = "Python"
niz2 = "je lahek programski jezik."
print(niz1,niz2)
niz3 = niz1 + " " + niz2

print(niz3)
# 3. Preveri če se v prejšnem nizu pojavi črka "k"/"K". 
# Če se pojavi, preveri še koliko krat se pojavi. V primeru, da se pojavi več kot y krat izpiši več, drugače manj.

if "k" in niz3.lower():
	if(niz3.lower().count("k") < y):
		print("Manj")
	else :
		print("Več")
else:
	print("Ni nobenega")
sfasd
# Zanke, seznami, slovarji, razredi, branje podatkov, funkcije, datoteke

# 1. Ustvari seznam Sadje, katerega elementi so sadezi.
# Sadez naj vsebuje ime in informacijo o tem ali ima koščice ali ne (jagoda nima, jabolko ima =D )

#class sadez:
#sadje = [] 
# 2. Ustvari funkcijo, ki bo dodajala elemente v seznam. Izmisli si tudi 5 

# 3. V seznamu preštej, koliko sadežev nima koščic.

# 4. Uporabnik naj doda še en sadež 

# 5. Iz datoteke sadje.txt preberi sadeže, preveri če sadež še ne obstaja ga dodaj drugače preskoči.

# 6 Izpiši imena sadežev.


# Obstoječe knjižnice

# 1. poiši knjižico, ki ima funkcijo za računanje kvadratnega korena in odgovor za n

n = 1764

# 2. Poišči knjižnico, katera ima možnost izposovanja 
# kateri operecaijski sistem trenutno poganja ta računalnik


# 3. Na ekran zapiši kako dolgo se je izvajal celoten program do sedaj(pazi na komentarje)


# 3. Nariši sonček s pomočjo risanja z grafiko






