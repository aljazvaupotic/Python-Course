#Hammingova razdalja

fp = open("rosalind_hamm.txt","r")

prvi = fp.readline()
drugi = fp.readline()
prvi = list(prvi)
drugi = list(drugi)

razlike = 0

if(len(prvi) == len(drugi)):
	for x in range(len(prvi)):
		if(prvi[x]!= drugi[x]):
			razlike += 1
print(len(prvi),len(drugi))
print(razlike)