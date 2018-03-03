print ('Questao 5', '\n')

p = float (input ('Insira o valor de sua mercadoria: '))
d = int (input ('Insira o percentual de desconto a ser atribuido: '))
vd = p*(d/100)
vf = p - vd

print ('Seu produto recebeu R$ %.2f de desconto' %vd)
print ('Voce pagara R$ %.2f neste produto' %vf)
