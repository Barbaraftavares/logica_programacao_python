valores = []
impar = 0

for x in range(1, 11):
    valores.append(int(input(f"Digite o valor {x}: ")))

for valor in valores:
    if valor % 2 != 0:
        impar += 1

print(f"Quantidade de valores ímpares: {impar}")