import json
def media_total(nota_1, nota_2, nota_3):
    return (nota_1 + nota_2 + nota_3) / 3

def verificar_media(media):
    if media >= 7:
        return "Aprovado"
    elif media >= 5:
        return "Recuperação"
    else:
        return "Reprovado"

def main():
    print("Programa de Cálculo de Notas Finais")
    
    nota_1 = float(input("Digite a primeira nota: "))
    nota_2 = float(input("Digite a segunda nota: "))
    nota_3 = float(input("Digite a terceira nota: "))

    media = media_total(nota_1, nota_2, nota_3)
    situacao_aluno = verificar_media(media)

    print(f"\nMédia: {media:.2f}")
    print(f"Situação: {situacao_aluno}")

if __name__ == "__main__":
    main()

