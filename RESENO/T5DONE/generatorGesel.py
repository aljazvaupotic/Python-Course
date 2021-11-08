# 2. generator gesel:
# oseba vnese kako močno geslo želi : weak/ avg / strog / superstrong. in dolžino gesla:
# šibka/weak gesla imajo samo majhne črke
# srednja/avg gesla imajo samo majhne črke in številke
# močna/strong gesla imajo majhne in velike črke, ter številke
# superstrong pa imajo polek majhnih in velikh črk, ter številk še posebne znake "!@#$%^&*()?"
import string 
import random as rd

# INPUT 
x = input("Vnesi kako mocno geslo zelis : weak/ avg / strong / superstrong: ")
y = eval(input("Vnesi dolzino zeljenga gesla: "))
# preveri moč
# generiraj 
def generiraj(x,y) :
	geslo = ""
	while y != 0:
		mala = rd.choice(string.ascii_lowercase)
		velika = rd.choice(string.ascii_uppercase)
		st = rd.choice(string.digits)
		znak = rd.choice(string.punctuation)
		#print(mala,velika,st,znak)
		if x == "weak" :
			opt = mala
			geslo += mala
			print(opt)
		elif x == "avg":
			opt = mala + velika
			geslo += rd.choice(opt)
			print(opt)
		elif x == "strong":
			opt = mala + velika + st
			geslo += rd.choice(opt)
			print(opt)
		elif x == "superstrong" : 
			opt = mala + velika + st + znak
			geslo += rd.choice(opt)
			print(opt)
		else:
			x = input("Popravi moc gesla (weak/avg/strong/superstrong): ")
		y -= 1
	return geslo
print(generiraj(x,y))
	