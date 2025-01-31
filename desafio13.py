valores = []

for x in range(1, 11):
    valores.append(input(f"Digite um nome {x}: "))

nome = input("Digite um nome para buscar: ")

if nome in valores:
    print("Achei")
else:
    print("Não achei")