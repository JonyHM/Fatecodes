print("Lista 2 - Questão 1", "\n")

print("Insira três lados de um trângulo")
a = int(input("1: "))
b = int(input("2: "))
c = int(input("3: "))

if (a + b) < c or (a + c) < b or (b + c) < a:
    print("Esta forma não é um triângulo")
elif a == b == c:
    print("Este triangulo é equilátero")
elif a == b or a == c or b == c:
    print("Este triângulo é isóceles")
else:
    print ("Este triâgulo é escaleno")