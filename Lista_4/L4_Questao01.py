print("\n Lista 4 - Questao 1 \n")

# Importa da biblioteca de geracao aleatoria, a funcao "randint", que gera numeros aleatorios
from random import randint

count = 0
lista = []

while count < 10: 
  
# Adiciona a lista criada, 10 numeros aleatorios entre 1 e 100
	lista.append(randint(1,100))
	count = count + 1

# Organiza os numeros da lista
lista.sort()

print("Maior numero: ", lista[9],". Menor numero: ", lista[0])
