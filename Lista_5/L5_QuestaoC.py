count = 0

for i in range(1067, 3628):
	if i % 2 == 0:
		if i % 7 == 0:
			count += 1
print("Dentro deste range,", count ,"numeros sao pares e divisiveis por 7")
