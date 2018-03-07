a = 80000
b = 200000
pa = a * (3/100)
pb = b * (1.5/100)
c = 1
	
while a < b:
	a = a + pa
	b = b + pb
	c = c + 1
	print(c)

print("Para que os paises se igualem, levara %d anos" %c)
