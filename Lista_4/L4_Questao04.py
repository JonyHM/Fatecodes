print("\nLista 4 - Questao 4\n")

import re

statement = "The Python Software Foundation and the global Python community welcome and encourage participation by everyone. Our community is based on mutual respect, tolerance, and encouragement, and we are working to help each other live up to these principles. We want our community to be more diverse: whoever you are, and whatever your background, we welcome you"

statement = re.sub(u'[,.:]', '', statement)
statement = statement.lower()

vetor = statement.split()
python = []
count = 0

for count in range (len(vetor)):
	pt = vetor[count]
	if pt[0] in "python":
		python.append(pt)
	if pt[-1] in "python":
		python.append(pt)	

print("Lista de palavras: ", vetor, "\n \nLista com palavreas que tem as mesmas letras de 'python': ",python)
