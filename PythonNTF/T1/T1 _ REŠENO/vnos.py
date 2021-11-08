#______________________________________________________________________________
# Termin 1, 16.5.2019
# Vnos podatkov
#______________________________________________________________________________

x = 2
# Od uprabnika programov lahko tudi zahtevamo, da vnese podatke.
# Zato uporabljamo vgrajeno metodo input 
#y = input("Vnesi stevilko: ")
#print(x, y)
#Želimo da uporabnik vnese svoje ime. Nato ga pa pozdravimo
ime = input("Ime :")
print("hej", ime)
# Sedaj od uporabnika še želimo, da nam poda svojo starost in domači kraj
starost = int(eval(input("Starost: ")))
domaciKraj = input("Hometown: ")

# preverimo tipe podatkov 
print(type(ime), type(starost),type(domaciKraj))
print(ime,starost,domaciKraj)
# podatke lahko manipuluramo, da nam njihovi tipi vedno odgovarjajo


# 4 
# Uporabnik naj vnese neko letnico v prihodnosti ti pa izračunaj koliko bo oseba
# stara tisto leto in to tudi izpiši
trenutnoLeto = 2019
letnicaVPrihodnosti = int(eval(input("Vnesi letnico v prihodnosti: ")))

novaStarost = starost + (letnicaVPrihodnosti - trenutnoLeto)
if(letnicaVPrihodnosti < trenutnoLeto):
	print("V letu", letnicaVPrihodnosti,"je bil star",novaStarost)
else:
	print("V letu", letnicaVPrihodnosti,"bo star",novaStarost)