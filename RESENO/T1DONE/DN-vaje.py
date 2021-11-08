#______________________________________________________________________________
# Termin 1
# Vaje
#______________________________________________________________________________


# Uporabnik naj vnese 2 številki, ti si izmisli eno in nato napiši program ki bo izpisal 
# največjo med njimi in njen izvor (USER/COMP)

x = 13029
st1 = eval(input("Vnesi prvi številko: "))
st2 = eval(input("Vnesi drugo številko: "))
#print(st1,type(st1), st2, type(st2)) ; testiranje vnosov

if( x >= st1 and x >=  st2):
	print(x, "je NAJVEČJE ŠTEVILO! Izvor: COMP")
else:
	if( st1 > st2) :
		print(st1, "je NAJVEČJE ŠTEVILO! Izvor: USER")
	else:
		print(st2, "je NAJVEČJE ŠTEVILO! Izvor: USER")
		

# Preberi čas v vojaškem načinu (1230 -> 12h in 30min),
# ter izpiši a je popoldan ali dopoldan in dodaj izpis 
# časa v obliki HH:mm

cas = eval(input("Vnesi uro v vojaskem nacinu (1230 -> 12h in 30min): "))
#print(cas)
ura = cas // 100
minute = cas % 100
print(ura, minute)
if( ura < 10) :
	izpis = "0" + str(ura) + ":" + str(minute)
else:
	izpis = str(ura) + ":" + str(minute)
if ( minute == 0):
	izpis += "0"
elif( minute < 10):
	izpis = str(ura) + ":0" + str(minute) 
print(izpis)


if(ura > 12):
	#POPOLDAN
	print("Je POPOLDAN. Ura je", izpis)
elif ( ura == 12) :
	if( minute != 0):
		print("Je POPOLDAN. Ura je", izpis)
	else:
		print("Je DOPOLDAN. Ura je", izpis)
else:
	#DOPOLDAN
	print("Je DOPOLDAN. Ura je", izpis)












# Sestavi funkcijo `st_ljudi(n)`, ki kot argument sprejme poljubno naravno
# število in nato v slovnično pravilni obliki vrne opis števila ljudi
# v dvorani kulturnega doma (glej zglede). Dvorana sprejme največ 500 ljudi. Podatki so simeslni, torej
# celo število, večje ali enako 0.
# Primer za n=0:
# 
#      "Dvorana je prazna."
# 
# Primer za n=1:
# 
#      "V dvorani je 1 človek."
# 
# Primer za n=303:
# 
#      "V dvorani so 303 ljudje."
# 
# Primer za n=500:
# 
#      "Dvorana je polna."
# 
# Primer za n=502:
# 
#      "Dvorana je polna. Zunaj sta ostala 2 človeka."

def st_ljudi (n) :
	# 1 = človek
	# 2 = človeka
	# 3 / 4 = ljudje
	# 5 / 0 = ljudi
	ostanek = n % 100 
	if n == 0:
		return "Dvorana je prazna."
	elif n < 500:
		# v dvorani so ljudje
		if ostanek == 1 : 
			return "V dvorani je " + str(n) + " človek."
		elif ostanek == 2 : 
			return "V dvorani sta " + str(n) + " človeka."
		elif ostanek == 3 or ostanek == 4 : 
			return "V dvorani so " + str(n) + " ljudje."
		else:
			return "V dvorani je " + str(n) + " ljudji."
	elif n == 500:
		return "Dvorana je polna."
	else:
		if ostanek == 1 : 
			return "Dvorana je polna. Zunaj je ostal " + str(n-500) + " človek."
		elif ostanek == 2 : 
			return "Dvorana je polna. Zunaj sta ostala " + str(n-500) + " človeka."
		elif ostanek == 3 or ostanek == 4 : 
			return "Dvorana je polna. Zunaj so ostali " + str(n-500) + " ljudje."
		else:
			return "Dvorana je polna. Zunaj je ostalo " + str(n-500) + " ljudi."

		
print(st_ljudi(11))

print(st_ljudi(100))

print(st_ljudi(4))
print(st_ljudi(500))

print(st_ljudi(546))

print(st_ljudi(142))
