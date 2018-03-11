print("\n Lista 3 - Questao 5 \n")

print("Calculo de MDC \n")
a = int(input("Insira um numero para o calculo: "))
b = int(input("Insira o segundo numero: "))

mx = max(a, b) #MX recebe o maior numero entre as entradas
mn = min(a, b) #MN recebe o menor numero entre as entradas


while True:

	if mx % mn == 0:
		print("O MDC dos numeros informados e: ", (mx / mn))
		break
	else:
		d = mn / (mx % mn)
		mx = mn
		mn = d
