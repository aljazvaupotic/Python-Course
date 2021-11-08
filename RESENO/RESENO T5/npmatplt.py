import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0.,10.,2)

plt.plot(t,t,"y--",t,-t,"bs",t,2*t,"r*")
plt.legend(("t od t","t od -t"," t od 2*t"))
plt.show()

def f(t):
	return np.cos(2*np.pi*t)
t1 = np.arange(0,5,0.1)
t2 = np.arange(0,5,0.02)

plt.figure(1)
plt.subplot(211)
plt.plot(t1,f(t1),"bo",t2,f(t2),"k")

plt.show()