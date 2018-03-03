print ('Questao 6', '\n')

dist = float (input ('Insira a distancia a ser percorrida (em KM): '))
velo = float (input ('Insira a velocidade media em que espera percorrer este trajeto (em km/h): '))

tempo = dist / velo

print ('Sua viagem tera duracao de aproximadamente %.2f horas' %tempo)
