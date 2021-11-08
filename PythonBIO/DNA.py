# Iz datoteke DNA bomo presteli koliko krat se pojavijo kateri "A" "C" "T" "G"

fp = open("rosalind_dna.txt","r")

sekvenca = fp.readline()

print(sekvenca.count("A"),sekvenca.count("C"),sekvenca.count("G"),sekvenca.count("T"))