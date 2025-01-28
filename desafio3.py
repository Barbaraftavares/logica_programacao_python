
print("Programa de Cálculo de Notas Finais")
print("=========================================")

while True:
    nota_1 = float(input("Digite a primeira nota: "))
    nota_2 = float(input("Digite a segunda nota: "))
    nota_3 = float(input("Digite a terceira nota: "))

    media = (nota_1 + nota_2 + nota_3) / 3

    if media >= 7:
        situacao_aluno = "Aprovado"
    elif media >= 5:
        situacao_aluno = "Recuperação"
    else:
        situacao_aluno = "Reprovado"

    print(f"\nMédia: {media:.2f}")
    print(f"Situação: {situacao_aluno}")