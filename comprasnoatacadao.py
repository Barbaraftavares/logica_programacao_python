# Classe Produto
class Produto:
    def __init__(self, id, nome, preco):
        self.id = id
        self.nome = nome
        self.preco = preco

    def __repr__(self):
        return f'Id: {self.id} | {self.nome} | R$ {self.preco:.2f}'


# Classe Mercado
class Mercado:
    def __init__(self):
        self.produtos = {
            1: Produto(1, "Café 1kg", 53.00),
            2: Produto(2, "Sabão em pó", 36.00),
            3: Produto(3, "Caixa de Leite", 82.00),
            4: Produto(4, "Refrigerante", 8.50)
        }

    def obter_produto(self, id):
        return self.produtos.get(id, None)

    def exibir_estoque(self):
        print("\nCatalogo de Produtos:\n")
        for produto in self.produtos:
            print(self.obter_produto(produto))


# Classe CaixaDoAtacado
class CaixaDoAtacado:
    def __init__(self, mercado):
        self.mercado = mercado

    def computarCompra(self, input_string):
        linhas = input_string.split('\n')
        metodo_pagamento = linhas[0].strip()
        itens = [linha.split(',') for linha in linhas[1:] if linha.strip()]

        total = 0
        for item in itens:
            id_produto = int(item[0])
            quantidade = int(item[1])
            produto = self.mercado.obter_produto(id_produto)

            if produto:
                preco_total = produto.preco * quantidade

                # Aplicar descontos por quantidade
                if quantidade > 25:
                    preco_total *= 0.75  # 25% de desconto
                elif quantidade > 15:
                    preco_total *= 0.80  # 20% de desconto
                elif quantidade > 5:
                    preco_total *= 0.90  # 10% de desconto

                total += preco_total

        # Aplicar descontos/acréscimos por método de pagamento
        if metodo_pagamento == "dinheiro":
            total *= 0.95  # 5% de desconto
        elif metodo_pagamento == "credito":
            total *= 1.03  # 3% de acréscimo

        return total


# Exemplo de uso
input_string = """credito
1,2
2,1"""

mercado = Mercado()
#mercado.exibir_estoque()

caixa = CaixaDoAtacado(mercado)
valor_total = caixa.computarCompra(input_string)
print(f'Valor total: R${valor_total:.2f}')