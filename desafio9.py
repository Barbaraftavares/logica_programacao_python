numero1 = float(input("Digite o primeiro valor válido: "))
while True:
    numero2 = float(input("Digite o segundo valor válido: "))
    if numero2 == 0:
        print("Número inválido")
    else:
        divisao= numero1/numero2
        print(f"{numero1} / {numero2}= resultado da divisão é: {divisao:.2f}")
        break
    