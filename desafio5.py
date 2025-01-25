import json

def main():
    vendedor = input("Digite o nome do vendedor: ")
    valor_imovel = float(input(f"Digite o valor do imóvel: "))

    if valor_imovel >= 50000:
        comissao = 0.20
    elif valor_imovel >= 30000:
        comissao = 0.15
    else:
        comissao = 0.10

    total_comissao = valor_imovel * comissao

    print(f"Vendedor: {vendedor}")
    print(f"Valor do Imóvel: R${valor_imovel:.2f}")
    print(f"Total da Comissão: R${total_comissao:.2f}")

if __name__ == "__main__":
    main()