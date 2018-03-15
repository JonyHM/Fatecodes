print("\n Lista 4 - Questao 3 \n")

# Importa da biblioteca de geracao aleatoria, a funcao "randint", que gera numeros aleatorios
from random import randint

count = 0
a = []
b = []
c = []

while count < 10: 
  
# Adiciona as listas criada, 10 numeros aleatorios entre 1 e 100
	a.append(randint(1,100))
	b.append(randint(1, 100))
	c.append(a[count])
	c.append(b[count])
	count = count + 1


print("Lista 1: ", a,"\nLista 2: ", b,"\nLista 3: ", c)
