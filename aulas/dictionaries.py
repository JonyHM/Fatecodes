from pprint import pprint

lista = {}

lista['n'] = 'jonathas'
lista['r'] = 'fodac#'

pprint(lista)
pprint(lista.keys())
pprint(lista.items())

for chave in lista:
    print (chave, lista[chave])
