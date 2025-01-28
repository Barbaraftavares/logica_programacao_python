while True:
    nota_1 = float(input("Digite a primeira nota: "))
    nota_2 = float(input("Digite a segunda nota: "))

    media = (nota_1 + nota_2) / 2

    if media >= 7:
        situacao_aluno = "Aprovado"
    else:
        situacao_aluno = "Reprovado"

    print("Programa de Cálculo de Notas Finais")
    print(f"\nMédia: {media:.2f}")
    print(f"Situação: {situacao_aluno}")

    resposta = input("Deseja realizar um novo cálculo? (s/n): ")
    if resposta.lower() != 's':
        break