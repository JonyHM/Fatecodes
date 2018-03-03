print ('Questao 3', '\n')
print ('Insira um número de dias, horas, minutos e segundos para conversão para minutos', '\n')
d = int(input ('Dias:'))
h = int(input ('Horas:'))
m = int(input ('Minutos:'))
s = int(input ('Segundos:'))

d = d * 86400
h = h * 3600
m = m * 60
r = d + h + m + s

print ('Os valores inseridos transformados em segundos são:', r)
