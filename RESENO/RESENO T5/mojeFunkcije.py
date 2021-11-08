import numpy as np
def dodajVArray(arr,x):
	l = arr.tolist()
	l.append(x)
	arr = np.array(l)
	return arr