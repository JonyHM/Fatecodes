print("Lista 2 - Questão 2", "\n")

print("Descubra se o ano é bissexto ou não:", "\n")
ano = int(input("Insira o ano: "))

if ano % 4 == 0:
    if ano % 100 == 0:
        print(f"O ano de {ano} não é bissexto")
    else:
        print(f"O ano de {ano} é bissexto")
elif ano % 400 == 0:
    print(f"O ano de {ano} é bissexto")
else:
    print(f"O ano de {ano} não é bissexto")
