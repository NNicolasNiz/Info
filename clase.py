import os
os.system('color')


x = int(input("ingrese fil:\t"))
y = int(input("ingrese col:\t"))

if y%2 == 0:
	impar = False
else:
	impar = True

for x in range(x):
	for i in range(y//2):
		if x%2 == 0:
			print("\033[1;32;40m[*]", end ="")
			print("\033[93m[*]",end ="")
		else:
			print("\033[93m[*]", end ="")
			print("\033[1;32;40m[*]",end ="")
	if impar:
		if x%2 == 0:
			print("\033[1;32;40m[*]", end ="")
		else:
			print("\033[93m[*]", end ="")

	print("")