#______________________________________________________________________________
# TERMIN 5
# Matplotlib
#______________________________________________________________________________
import matplotlib.pyplot as plt
import numpy as np
# Preprost graf 
plt.plot([0,10,20,30],[1,23,12,3])

# ime osi, ime grafa
plt.xlabel("Starost")
plt.ylabel("Norost")
plt.title("Graf N -> S")

# meje grafov
plt.axis([0,40,-10,30])

# barve in znaki
# več funkcij na en graf

plt.plot(
	[0,10,20,30],[2,8,12,-5],"ro",
	[1,2,3,4,5,6,7,8,9,10],[1,10,15,17,-5,6,42,23,23,-0],"g--")

# Komentarji na grafu
plt.annotate(
	"pri 10ih letih", 
	xy = (10,7.6),
	xytext =(25,30),
	arrowprops= dict(facecolor= "black",shrink = 0.05))
imena = ["Jože","Marjan","Mojca"]
plt.legend(imena)
plt.show()

# Različni tipi grafov

labels = "HP","Asus","Microsoft","Samsung","Apple"
kolicne = [2,2,1,1,1]
ax1 = plt.subplot(111)
ax1.pie(kolicne,labels = labels,shadow = True,startangle = 0)
plt.show()
plt.subplot (131)
plt.figure(figsize = (10,5))
labels = ["HP","Asus","Microsoft","Samsung","Apple"]
plt.bar(labels, kolicne)
plt.show()
plt.subplot(132)
plt.scatter(labels,kolicne)
plt.show()

#