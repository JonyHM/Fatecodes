#!/usr/bin/python -tt
# Exerc�cios by Nick Parlante (CodingBat)

# A. dormir
# dia_semana � True para dias na semana
# feriado � True nos feriados
# voc� pode ficar dormindo quando � feriado ou n�o � dia semana
# retorne True ou False conforme voc� v� dormir ou n�o
def dormir(dia_semana, feriado):
  if dia_semana and not feriado:
    return False
  else:
    return True
    
# B. alunos_problema
# temos dois alunos a e b
# a_sorri e b_sorri indicam se a e b sorriem
# temos problemas quando ambos est�o sorrindo ou ambos n�o est�o sorrindo
# retorne True quando houver problemas
def alunos_problema(a_sorri, b_sorri):
  return 

# C. soma_dobro
# dados dois n�meros inteiros retorna sua soma
# por�m se os n�meros forem iguais retorna o dobro da soma
# soma_dobro(1, 2) -> 3
# soma_dobro(2, 2) -> 8
def soma_dobro(a, b):
  return

# D. diff21
# dado um inteiro n retorna a diferen�a absoluta entre n e 21
# por�m se o n�mero for maior que 21 retorna dobro da diferen�a absoluta
# diff21(19) -> 2
# diff21(25) -> 8
# dica: abs(x) retorna o valor absoluto de x
def diff21(n):
  return

# E. papagaio
# temos um papagaio que fala alto
# hora � um par�metro entre 0 e 23
# temos problemas se o papagaio estiver falando
# antes da 7 ou depois das 20
def papagaio(falando, hora):
  return

# F. dez
# dados dois inteiros a e b
# retorna True se um dos dois � 10 ou a soma � 10
def dez(a, b):
  return

# G. dista10
# seja um inteiro n
# retorna True se a diferen�a absoluta entre n e 100 ou n e 200
# for menor ou igual a 10
# dista10(93) -> True
# dista10(90) -> True
# dista10(89) -> False
def dista10(n):
  return

# H. apaga
# seja uma string s e um inteiro n
# retorna uma nova string sem a posi��o n
# apaga('kitten', 1) -> 'ktten'
# apaga('kitten', 4) -> 'kittn'
def apaga(s, n):
  return 

# I. troca
# seja uma string s
# se s tiver tamanho <= 1 retorna ela mesma
# caso contr�rio troca a primeira e �ltima letra
# troca('code') -> 'eodc'
# troca('a') -> 'a'
# troca('ab') -> 'ba'
def troca(s):
  return 

# Provided simple test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(obtido, esperado):
  if obtido == esperado:
    prefixo = ' Parab�ns!'
  else:
    prefixo = ' Ainda n�o'
  print ('%s obtido: %s esperado: %s'
         % (prefixo, repr(obtido), repr(esperado)))

def main():

  print ('Oba! Hoje vou ficar dormindo!')
  test(dormir(False, False), True)
  test(dormir(True, False), False)
  test(dormir(False, True), True)
  test(dormir(True, True), True)

  print ()
  print ('Alunos problema')
  test(alunos_problema(True, True), True)
  test(alunos_problema(False, False), True)
  test(alunos_problema(True, False), False)
  test(alunos_problema(False, True), False)

  print ()
  print ('Soma dobro')
  test(soma_dobro(1, 2), 3)
  test(soma_dobro(3, 2), 5)
  test(soma_dobro(2, 2), 8)
  test(soma_dobro(-1, 0), -1)
  test(soma_dobro(0, 0), 0)
  test(soma_dobro(0, 1), 1)

  print ()
  print ('Diff21')
  test(diff21(19), 2)
  test(diff21(10), 11)
  test(diff21(21), 0)
  test(diff21(22), 2)
  test(diff21(25), 8)
  test(diff21(30), 18)

  print ()
  print ('Papagaio')
  test(papagaio(True, 6), True)
  test(papagaio(True, 7), False)
  test(papagaio(False, 6), False)
  test(papagaio(True, 21), True)
  test(papagaio(False, 21), False)
  test(papagaio(True, 23), True)
  test(papagaio(True, 20), False)

  print ()
  print ('Dez')
  test(dez(9, 10), True)
  test(dez(9, 9), False)
  test(dez(1, 9), True)
  test(dez(10, 1), True)
  test(dez(10, 10), True)
  test(dez(8, 2), True)
  test(dez(8, 3), False)
  test(dez(10, 42), True)
  test(dez(12, -2), True)

  print ()
  print ('Dista 10')
  test(dista10(93), True)
  test(dista10(90), True)
  test(dista10(89), False)
  test(dista10(110), True)
  test(dista10(111), False)
  test(dista10(121), False)
  test(dista10(0), False)
  test(dista10(5), False)
  test(dista10(191), True)
  test(dista10(189), False)
  test(dista10(190), True)
  test(dista10(200), True)
  test(dista10(210), True)
  test(dista10(211), False)
  test(dista10(290), False)

  print ()
  print ('Apaga')
  test(apaga('kitten', 1), 'ktten')
  test(apaga('kitten', 0), 'itten') 
  test(apaga('kitten', 4), 'kittn')
  test(apaga('Hi', 0), 'i')
  test(apaga('Hi', 1), 'H')
  test(apaga('code', 0), 'ode')
  test(apaga('code', 1), 'cde')
  test(apaga('code', 2), 'coe')
  test(apaga('code', 3), 'cod')
  test(apaga('chocolate', 8), 'chocolat')

  print ()
  print ('Troca letras')
  test(troca('code'), 'eodc')	    
  test(troca('a'), 'a')
  test(troca('ab'), 'ba')
  test(troca('abc'), 'cba')
  test(troca(''), '')
  test(troca('Chocolate'), 'ehocolatC')
  test(troca('nythoP'), 'Python')
  test(troca('hello'), 'oellh')
  
if __name__ == '__main__':
  main()
