nome = input("Usuario: ")
senha = input("Senha: ")

while senha == nome:
	print("Senha invalida! Digite uma senha diferente do nome de usuario")
	nome = input("Usuario: ")
	senha = input("Senha: ")

print("Conta criada com sucesso!")
