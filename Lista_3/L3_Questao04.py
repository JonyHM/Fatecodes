print("Lista 3 - Questao 4", "\n")

fib = int(input("Insira um numero para o calculo de fibonacci: "))

au = 1.62 #proporcao aurea arredondada para cima
r5 = 2.24 #raiz de 5 arredondadapara cima

fib = (au ** fib - (1 - au) ** fib) / r5

print("O numero de Fibonacci do algarismo digitado e: %d" %fib)
