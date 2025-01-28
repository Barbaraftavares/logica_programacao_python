tentativas = 0
while True:
    usuario = str(input("Digite o seu nome: "))
    senha = str(input("Digite a sua senha: "))

    if usuario == "aluno" and senha == "segredo":
        print(f'Seja bem vindo ao programa, {usuario}!')
        break
    else:
        tentativas += 1
        print(f"usuário e/ou senha inválidos. Tentativas restantes: {3 - tentativas}")

        if tentativas == 3:
            print("Excedeu o limite de três tentativas! Acesso Bloqueado.")
            break