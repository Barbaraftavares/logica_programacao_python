
while True:
    numero = int(input("Digite um valor entre 1 e 10: "))
    if numero>= 1 and numero <=10:
        for x in range (1, 11):
            print(f"{numero} x {x}=", (numero * x))
        break
    else: 
        print("Número inválido")

