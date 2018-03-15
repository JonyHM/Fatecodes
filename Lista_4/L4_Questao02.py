print("\n Lista 4 - Questao 2 \n")

# Importa da biblioteca de geracao aleatoria, a funcao "randint", que gera numeros aleatorios
from random import randint

count = 0
lista = []
par = []
impar = []

while count < 20: 
  
# Adiciona a lista criada, 20 numeros aleatorios entre 1 e 100. Testa se e par ou impar e armazena o resultado nas listas correspondentes
	lista.append(randint(1,100))
	if lista[count] % 2 == 0:
		par.append(lista[count])
	else:
		impar.append(lista[count])
	count = count + 1

print("Total lista: ", lista,"\nLista PAR: ", par,"\nLista IMPAR: ", impar)
