import json

nomes_produtos = ["banana", "arroz", "carne", "maçã", "pera"]
precos_produtos = [10.00, 5.00, 9.00, 6.00, 12.21]

def calcular_desconto(quantidade_prod):
 return 0.1 if quantidade_prod >= 11 and quantidade_prod <= 20 else \
 0.2 if quantidade_prod >= 21 and quantidade_prod <= 50 else \
 0.25 if quantidade_prod > 50 else 0

def main():
 escolha = int(input("Escolha o produto (1-5): ")) - 1
 quantidade_prod = int(input("Digite a quantidade: "))
 preco = precos_produtos[escolha]
 desconto = calcular_desconto(quantidade_prod)
 valor_total = preco * quantidade_prod * (1 - desconto)
 print(f"Valor total: R${valor_total:.2f}")

main()