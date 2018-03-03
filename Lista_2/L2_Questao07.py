print("Lista 2 - Questão 7","\n")

m = float(input("Metros quadrados a serem pintados: "))

lit = m / 3
lat = lit / 18

if m % 3 != 0:
    lit = lit + 1
if lit % 18 != 0:
    lat = int(lat + 1)

p = lat * 80
print(f"Latas a serem utilizadas: {lat}")
print(f"Preço a ser pago: R${p:.2f}")
