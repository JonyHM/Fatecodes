print("\nLista 4 - Questao 4\n")

# Importa a biblioteca da funcao que retira caracteres especificados quando executado
import string

statement = "The Python Software Foundation and the global Python community welcome and encourage participation by everyone. Our community is based on mutual respect, tolerance, and encouragement, and we are working to help each other live up to these principles. We want our community to be more diverse: whoever you are, and whatever your background, we welcome you"

# Retirando os caracteres especiais
for s in string.punctuation:
	statement = statement.replace(s,' ')

# Deixando todas as letras minusculas
statement = statement.lower()

# Criando um vetor com todas as palavras da frase em 'statement'
vetor = statement.split()
python = []
count = 0

# Repeticao enquanto o contador 'count' estiver dentro do comprimento da lista de palavras
for count in range (len(vetor)):

	# Variavel com cada palavra do vetor de palavras
	pt = vetor[count]

	# Se a palavra da variavel 'pt' (que muda a cada repeticao) comecar ou terminar com 'python', ela deve ser inserida na lista 'python'
	if pt[0] in "python":
		python.append(pt)
	if pt[-1] in "python":
		python.append(pt)	

print("Lista de palavras: ", vetor, "\n \nLista 'python': ",python, "\n")
