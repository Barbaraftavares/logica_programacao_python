operacao = input("Escolha a operação (+, -, *, /): ")
numero_1 = int(input("Digite o primeiro valor: "))
numero_2 = int(input("Digite o segundo valor: "))

match operacao:
    case "+":
        print(f"Resultado da soma: {numero_1 + numero_2}")
    case "-":
        print(f"Resultado da subtração: {numero_1 - numero_2}")
    case "*":
        print(f"Resultado da multiplicação: {numero_1 * numero_2}")
    case "/":
        if numero_2 != 0:
            print(f"Resultado da divisão: {numero_1 / numero_2}")
        else:
            print("Erro: divisão por zero!")
    case _:
        print("Operação inválida.")

