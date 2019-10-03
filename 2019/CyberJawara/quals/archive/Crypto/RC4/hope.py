

import os


with open("CYBER JAWARA 2019 QUALS - RULES-OF-THE-GAME.pdf.encrypted") as f:
	e1 = f.read()

with open("5_6303015062663594053.pdf") as f:
	p1 = f.read()

with open("flag.pdf.encrypted") as f:
	e2 = f.read()

p2 = ''
for i in range(len(e2)):
	p2 += chr(ord(p1[i]) ^ ord(e1[i]) ^ ord(e2[i]))

print p2
