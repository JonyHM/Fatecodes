print("Lista 3 - Questao 1", "\n")
nota = int(input("Insira uma nota entre 0 e 10: "))

while nota < 0 or nota > 10:
	print ("Nota invalida! Tente novamente")
	nota = int(input("Insira uma nota entre 0 e 10: "))
print("Nota Valida")
