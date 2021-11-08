#!/usr/bin/env python
# -*- coding: utf-8 -*-
#______________________________________________________________________________
# Termin 5 : 
#
#	Sortirni algoritmi 
#______________________________________________________________________________

import datetime as dt
# Zakaj rabimo sortiranje? 
# Včasih želimo podatke urediti, ne le poiskati najmanjše ali največje vrednosti,
# obstaja več algoritmov vsak ima svoje prednosti in slabosti.
# Spoznali bomo jih nekaj, ki so največkrat uporabljeni

# ustvari seznam 50ih naključnih števil.

s = [1,9,-7,5,9,5,87,-2,2,6,8979,879,789,75,1,21,321,34,65,42,5,132,432,4,31,31,654,21,3,7,2,4,564,654,676,7,21,32,16,54231]

# 1. BUBBLE SORT 
# Kako deluje? -> Vzamemo dva sosednja elementa in primerjamo,
# kateri od njiju je večji/manjši ter po potrebi zamenjamo.
# Napiši funkcijo ki bo sortirala ta seznam naraščajoče in za vsak korak izpisala seznam
def bs(arr):
	sorted = arr.copy()
	while True :
		menjave = 0
		for i in range(len(arr)-1):
			print(sorted)
			if(sorted[i] > sorted[i+1]):
				sorted[i],sorted[i+1] = sorted[i+1],sorted[i]
				menjave += 1
		if menjave == 0:
			break
		
	return sorted
bubbleStart = dt.datetime.now()	
print(bs(s))
bubbleStop = dt.datetime.now()	
print()

# 2. SELECTION SORT
# Kako deluje? -> Med ne sortiranimi elementi poiščemo najmanjšega / največjega 
# in ga zamenjamo s tistim ki je na prvem mestu med njimi.
# Napiši funkcijo, ki bo sortirala seznam padajoče.

def ss(arr):
	unsorted = arr.copy()
	sorted = []
	d = len(arr)
	while len(sorted) != d : 
		el = min(unsorted)
		sorted.append(el)
		unsorted.remove(el)
		print("Osnovni", unsorted, "Sortiran", sorted)
	return sorted
	
selectionStart = dt.datetime.now()
print(ss(s))
selectionStop = dt.datetime.now()
print(s)

# 3. INSERTION SORT
# Kako deluje? -> Prvi element ne sortiranega dela postavi na pravilno mesto v že sortiran del
# Napiši funkcijo, ki bo uporablia algoritem za sortiranje z vstavljanjem. 
# Lahko je naraščajoče ali padjoče.


def inseSort(arr):
	sorted = arr.copy()
	
	for i in range(1,len(arr)):
		kljuc = sorted[i]
		
		ur = i - 1
		while ur >= 0 and kljuc < sorted[ur] :
			sorted[ur+1] = sorted[ur]
			ur -= 1
		sorted[ur+1] = kljuc
		print(sorted)
	return sorted
print()
print(s)
insertionStart = dt.datetime.now()
print(inseSort(s))
insertionStop = dt.datetime.now()


# 4. Za vse algoritme še izpiši, kako dolgo potrebujejo. Kateri je najhitrejši? 
# A se kaj spremeni če je naš seznam dolg 10,000 številk? 

sortedStart = dt.datetime.now()
m = sorted(s)
print(m)
sortedStop = dt.datetime.now()

print(bubbleStop - bubbleStart)
print(selectionStop - selectionStart)
print( insertionStop - insertionStart)
print( sortedStop - sortedStart)




# BONUS: MERGE SORT