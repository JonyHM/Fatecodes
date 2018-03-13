print("\n Lista 3 - Questao 5 \n")

print("Calculo de MDC \n")
a = int(input("Insira um numero para o calculo: "))
b = int(input("Insira o segundo numero: "))

mx = max(a, b) # mx recebe o maior numero inserido
mn = min(a, b) # mn recebe o menor numero inserido

while mn != 0:

	mx, mn = mn, mx % mn 	# Caso o menor numero seja diferente de 0, a variavel que continha o maior numero (mx) recebe o menor numero entre as
				# entradas e a outra variavelrecebe o resto da divisao dos dois numeros ate nao haver mais resto na divisao

print("\nO MDC dos numeros informados e: ", mx, "\n")
