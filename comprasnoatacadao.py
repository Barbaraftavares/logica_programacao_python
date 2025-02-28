class Produto:
    def __init__(self, id, nome_produto, preco_produto):
        self.id = id
        self.nome = nome_produto
        self.preco = preco_produto

    def __repr__(self):
        return f'Id: {self.id} | {self.nome} | R$ {self.preco:.2f}'


class Atacadao:
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
        print("\nExibir o catalogo dos produtos:\n")
        for produto in self.produtos:
            print(self.obter_produto(produto))


class CaixaDoAtacadao:
    def __init__(self, mercado):
        self.mercado = mercado

    def computarCompra(self, input_compra):
        linhas = input_compra.split('\n')
        metodo_pagamento = linhas[0].strip()
        itens = [linha.split(',') for linha in linhas[1:] if linha.strip()]

        valor_total = 0
        for item in itens:
            id_produto = int(item[0])
            quantidade = int(item[1])
            produto = self.mercado.obter_produto(id_produto)

            if produto:
                preco_total = produto.preco * quantidade

                if quantidade > 25:
                    preco_total *= 0.75  # 25% de desconto
                elif quantidade > 15:
                    preco_total *= 0.80  # 20% de desconto
                elif quantidade > 5:
                    preco_total *= 0.90  # 10% de desconto

                valor_total += preco_total

        if metodo_pagamento == "dinheiro":
            valor_total *= 0.95  # 5% de desconto
        elif metodo_pagamento == "credito":
            valor_total *= 1.03  # 3% de acréscimo

        return valor_total


input_compra = """credito
1,2
2,1"""

mercado = Atacadao()

caixa = CaixaDoAtacadao(mercado)
valor_total = caixa.computarCompra(input_compra)
print(f'Valor total: R${valor_total:.2f}')