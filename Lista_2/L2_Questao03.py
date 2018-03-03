print("Lista 2 - Questão 3", "\n")

print("Controle de pesca")
peso = int(input("Peso da pesca: "))

if peso > 50:
    excesso = peso - 50
    multa = excesso * 4
    print(f"O peso da pesca: {peso}KG excedeu em {excesso}KG o limite máximo permitido pelo governo do estado de São Paulo!")
    print(f"Sua multa será de R${multa:.2f}")
else:
    excesso = 0
    multa = 0
    print(f"O peso da pesca: {peso}KG não excedeu o limite permitido")
