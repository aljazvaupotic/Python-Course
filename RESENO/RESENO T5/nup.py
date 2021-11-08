#______________________________________________________________________________
# TERMIN 5
# Numpy
#______________________________________________________________________________

import numpy as np
# USTVARIMO ARRAY 
# list -> array


l = [0,1,2,3,4]
print(l)
arr1d = np.array(l)
print(arr1d)
# preverimo type
print()
print(type(l)) 
print(type(arr1d))

# dodajmo vsakemu elementu 2
for i in range(len(l)) :
	l[i] += 2
print (l)

arr1d += 2
print(arr1d)
arr1d = arr1d - 3
print(arr1d)
arr1d *= 2
print(arr1d)
print()

import mojeFunkcije as mF
# dodamo nov element 
# 
# print(l)
# 
# 
# iz array nazaj v list
l = arr1d.tolist()
print(l)
l.append(21)
arr1d = np.array(l)
print(arr1d)

arr1d = mF.dodajVArray(arr1d,25)
print(arr1d)
print()
# 2d array / "matrika"
l2 = [[1.2,2.5,3.4],[2,4,6],[9,8,7]]
arr2d = np.array(l2)
print(l2)
print(arr2d)

# tip elementov arraya 
print(type(arr2d[0][0]))
# iz float bomo pretvorili v int
arr2d = arr2d.round()
print(arr2d)
arr2d = arr2d.astype("int").astype("str")
print()
print(arr2d)
print()
arr1d_b = np.array([1,0,10,-2],dtype="bool")
print(arr1d_b)
arr1d_s = np.array([2,"kikiriki"],dtype = "str")
print(arr1d_s)

#arr1d_i = np.array([2,"kikiriki"],dtype = "int")
#print(arr1d_i)
# oblika arraya
l3 = [[12,23,3,42],[2,4,46,82],[333,6,9,12]]
arr2 = np.array(l3)
print(arr2)
print("Oblika:", arr2.shape)

# velikost arraya
print("Velikost:",arr2.size)
print("Dolžina l3:", len(l3),"*",len(l3[0]),"=",len(l3)*len(l3[0]))
# dimenzije 
print("Tip : ",arr2.dtype)
print("dimenzije",arr2.ndim," Dimenzije ",arr1d.ndim)
# točno določen element
print(arr2[2,1]) # prvi parameter je index vrstice drugi index kolone
# željeno vrstico
print(arr2[1:2,])
# željeno kolono
print("k: ",arr2[0:3,3:4])
# željeno pod matriko
print(arr2[0,3],arr2[2,0])
for i in range(len(l3)) :
	for x in range(len(l3[i])):
		if(x == len(l3[i])-1):
			print(l3[i][x])
print()
print("TUTU")
print(arr2[0:2,0:2])

print()
print(arr2)
# if pogoj 
b = arr2 % 3 == 1
print(b)
# Obrat kolone
vrstice = len(l3)
kolone = len(l3[0])
print(vrstice)
print(kolone)
print()
print("Obracam 1x")
print(arr2[::-1,])
# Obrat vrstice
print()
print(arr2[0:3,::-1])
# Obrat arraya
print()
print(arr2[::-1,::-1])
# maximum, minimum in mediana
print("Max: ",arr2.max())
print("Min: ",arr2.min())
print("Mean: ",arr2.mean())
# cumulative sum
print(np.cumsum(arr2))
# minimum / maximum na določeni osi (vrstica / kolona)
print("V kolonah je min:", np.amin(arr2,axis = 0))
print("V vrsticah je max:", np.amax(arr2,axis = 1))

# preoblikovanje / "reshape" / "flatten" / "ravel"
print()
print(arr2)
print(arr2.reshape(4,3))
b1 = arr2.flatten()
b1[0] = 101
print(b1)
print(arr2)
b2 = arr2.ravel()
b2[9] = 101
print(b2)
print(arr2)
print()
print()
# arange
print(np.arange(5))
print(np.arange(0,10))
print(np.arange(2,21,3))
print(np.arange(50,25,-3))
print(np.arange(50,75,-3))
# linspace 
print()
print(np.linspace(start = 0, stop = 100, num = 13, dtype = int))
print(np.linspace(start = 0, stop = 100, num = 13, dtype = float))

# random/ rand, randn, randint, random, choice + probabilty
print()
print(np.random.rand(2,3))
print(np.random.randn(3,3))
print(np.random.random())
print(np.random.randint(-10,10, size = [3,3]))

print(np.random.choice(["a","e","i","o","u"],size = 4))

print(np.random.choice(["a","e","i","o","u"],size = 10,p = [0.2,0.2,0.2,0.2,0.2]))
# random seed
np.random.seed(120)
print(np.random.randint(1,10,size = [1,2]))
print(np.random.rand(2,2))
print(np.random.rand(1,1))
np.random.seed(100)
print(np.random.randint(1,10,size = [1,2]))

# index takrat ko je pogoj izpolnjen
arr5 = np.array([1,233,56,58,80,8753435,78954,3456,7654])
print(arr5)
index_v100 = np.where(arr5%2 == 1)
print(index_v100)
# vrednost na tem indexu
print(arr5.take(index_v100))

arr5 = np.arange(10)
np.savetxt("out.csv",arr5,delimiter = ",")






