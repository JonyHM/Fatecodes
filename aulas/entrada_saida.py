#Fazer um programa que leia o arquivo 'entrada.txt' como leitura e 'saida.txt' como gravação
#Gravar tudo o que ler em 'entrada.txt' para 'saida.txt', trocando as vogais por '*'

e = open('entrada.txt', 'r')
s = open('saida.txt', 'w')

for linha in e.readlines():
    for letra in linha:
        if letra in "aeiou":
            s.write('*')
        else:
            s.write(letra)
e.close()
s.close()
