f = open('alice.txt', 'r')
texto = f.read().lower()

import string
for c in string.punctuation:
    texto = texto.replace(c, ' ')
    #Tirando caracteres especiais

texto = texto.split()
conta_palavras = {}

for palavra in texto:
    if palavra in conta_palavras:
        conta_palavras[palavra] += 1
    else:
        conta_palavras[palavra] = 1
print('O nome "Alice" aparece: ', conta_palavras['alice'], 'vezes')
