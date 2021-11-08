#RosaLind

import sys

print(sys.version)


# def sumOfOdd(x,y):
# 	sum = 0
# 	for i in range(x,y):
# 		if(i % 2 == 1):
# 			sum += i

# 	return sum		

# print(sumOfOdd(100,200))



branaDatoteka = open("tekst1.txt", "r")
spisanaDatoteka = open("rezultat.txt","w")
for i,line in enumerate(branaDatoteka):
	#Vsaka druga vrstica
	if(i % 2 == 1) : 
		spisanaDatoteka.write(line)

branaDatoteka.close()
spisanaDatoteka.close()


fp = open("dict.txt", "r")
poved = fp.readline()
fp.close()

besede = poved.split(" ")
slovar = {besede[0]:poved.count(poved[0])}
for b in besede:
	for k in slovar:
		if(b == k):
			continue
		else:
			slovar[b] = poved.count(b)	
			break


for key, value in slovar.items():
    print (key, value)		