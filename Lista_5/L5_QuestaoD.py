lista = []
sorte = 0

for s in range(18644, 33088):
	lista = str(s)
	if '2' in lista:
		if '7' not in lista: 
			sorte += 1
			
print (sorte)

