print("Lista 2 - Questão 6","\n")

sh = float(input("Salário por hora: "))
h = int(input("Horas mensais: "))

b = sh * h 
ir = b * 0.11
inss = b * 0.08
sind = b * 0.05
sl = b - ir - inss - sind

print("\n","Extrato: ","\n")
print(f"Salário bruto: R${b:.2f}")
print(f"Imposto de renda: R${ir:.2f}")
print(f"INSS: R${inss:.2f}")
print(f"Sindicato: R${sind:.2f}")
print(f"Salário líquido: R${sl:.2f}")
