import json

class Produto:
    def __init__(self, id, nome, quantidade, preco):
        self.id = id
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco


    def __repr__(self):
        return f'Id: {self.id} | {self.nome} | Qtd: {self.quantidade} | R$ {self.preco:.2f}'

class Mercado:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def exibir_estoque(self):
        for produto in self.produtos:
            print(produto)

    def valor_total(self):
        total = sum(produto.quantidade * produto.preco for produto in self.produtos)
        return f'Valor total: R${total:.2f}'

arquivo_json = 'produtos.json'

mercado = Mercado()
with open(arquivo_json, 'r') as file:
    produtos_data = json.load(file)
    for item in produtos_data:
        produto = Produto(item['id'], item['nome'], item['quantidade'], item['preco'])
        mercado.adicionar_produto(produto)

print("Estoque:")
mercado.exibir_estoque()
print(mercado.valor_total())
