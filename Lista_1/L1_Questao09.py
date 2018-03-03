print ('Questao 9', '\n')

print ('Aluguel de carros', '\n')
km = float (input ('Insira a quantidade de KM percorridos com o veiculo alugado: '))
dias = int (input ('Insira a quantidade de dias alugados: '))

pd = dias * 60
pkm = km * 0.15
pt = pd + pkm

print ('Valor total a pagar: R$', pt)
