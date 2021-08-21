import random 
x = random.randint(7,10)

pss=""

for i in range(x):
	a = random.randint(33,127)
	valor = chr(a)
	pss += valor
print(pss)	