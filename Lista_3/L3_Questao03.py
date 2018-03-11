print("Lista 3 - Questao 3", "\n")
a = 80000
b = 200000
c = 0
	
while a <= b:
	a = (a * 3) / 100 + a
	b = (b * 1.5) / 100 + b
	c = c + 1
	print(c)

print("Para que a populacao dos paises se iguale, levara %d anos" %c)
