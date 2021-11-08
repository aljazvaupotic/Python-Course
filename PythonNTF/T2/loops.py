#______________________________________________________________________________
# Termin 2, 30.5.2019
# While and For
#______________________________________________________________________________

# Izpiši števila od 1 do 10:

print(1,2,3,4,5,6,7,8,9)
print()
# Izpiši števila od 1 do 10 z uporabo zanke while:
x = 1
st = []
while x < 10:
	print(x)
	x += 0.5
print(st)
print()
# Izpiši števila od 1 do 10 z uporabo zanke for:
for i in range(1,10):
	print(i)

niz = "Janezek vozi kolo."

for c in niz:
	if(c == "e"):
		print("Našel sem E")
print()
dolzina = len(niz)
ix = 0
while ix < dolzina :
	if(niz[ix] == "e"):
		print("Našel sem E")
	ix += 1





# 	Kakšna je razlika med while in for?
# While uporabljamo, ko ne vemo kolikokrat bomo dostopali v zanko.
# For uporabljamo, ko poznamo dolžino svojega "sprehoda"



# Dokler nebos prestel 2eh Ojev izpisuj nisem še

stOjev = 0
for c in niz:
	if(c == "o"):
		stOjev += 1
		print("Našel o")
	if(stOjev != 2):
		print("Nisem še")
	elif(stOjev == 2):
		break

print()
ix = 0
stOjev = 0
while(stOjev < 2):
	print("Nisem še")
	if(niz[ix] == "o"):
		stOjev += 1
		print("Našel o")	
	ix += 1

# Izberi si eno število med 1 in 100. 
x = 27
# a) Izpiši vsa števila CELA POZITVNA manjša od izbranega, uporabi obe zanki!

for st in range(1,100):
	
	print("sem v loopu",str(st)+"ič")
	if(st < x):
		print(st)
	else:
		break
st = 1
while( st < x):
	print("sem v loopu",str(st)+"ič")
	print(st)
	st += 1


# b) Izpiši le to število in njegove večkratnike, manjše od števila 500. 
# Ponovno uporabi obe zanki!
print()
loopanje = 0
for i in range(1,100000):
	loopanje += 1
	if(i % x == 0):
		print(i)
print()

print(loopanje)
loopanje = 0
print()

y = 1

while(y < 100000):
	loopanje += 1
	if(y % x == 0):
	#	print(y)
		y += x
	else:
		y += 1

print(loopanje)






