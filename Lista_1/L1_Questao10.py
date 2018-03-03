print ('Questao 10', '\n')

print ('Quantos dias de vida ja perdeu?', '\n')
c = int (input ('Quantos cigarros aproximadamente voce fuma por dia?: '))
a = int (input ('Ha quantos anos aproximadamente voce e fumante?: '))

dias = a*365
cig = c*10
minutos = dias * cig
horas = minutos/60
dias = horas/24

print ('Voce perdeu, ate agora, %d dias de vida' %dias)

#Perguntar sobre o uso do datetime#
