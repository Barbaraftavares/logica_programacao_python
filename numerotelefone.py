class Contato:
    def __init__(self, nome, numero_telefone):
        self.nome = nome
        self.numero_telefone = numero_telefone

    def __str__(self):
        return f"Nome: {self.nome} | Telefone: {self.numero_telefone}"

class AgendaTelefonica:
    def __init__(self):
        self.contatos = []

    def adicionar_contato(self, contato):
        if contato not in self.contatos:
            self.contatos.append(contato)
            print("Contato adicionado com sucesso!")
        else:
            print("Contato já existe na agenda!")

    def remover_contato(self, nome):
        contato_remover = self.buscar_contato(nome)
        if contato_remover:
            self.contatos.remove(contato_remover)
            print("Contato removido com sucesso!")
        else:
            print("Contato não encontrado na agenda!")

    def buscar_contato(self, nome):
        for contato in self.contatos:
            if contato.nome == nome:
                return contato
        return None

    def atualizar_contato(self, nome, novo_contato):
        contato_atualizar = self.buscar_contato(nome)
        if contato_atualizar:
            self.contatos.remove(contato_atualizar)
            self.contatos.append(novo_contato)
            print("Contato atualizado com sucesso!")
        else:
            print("Contato não encontrado na agenda!")

    def listar_contatos(self):
        if not self.contatos:
            print("Agenda vazia!")
        else:
            for contato in self.contatos:
                print(contato)

def main():
    agenda = AgendaTelefonica()
    while True:
        print("Agenda Telefônica:")
        print("1. Adicionar novo contato")
        print("2. Remover contato")
        print("3. Buscar contato")
        print("4. Atualizar contato")
        print("5. Listar contatos")
        print("6. Sair")
        opcao = input("Escolha uma das opções: ")
        if opcao == "1":
            nome = input("Digite o nome do contato: ")
            numero_telefone = input("Digite o número de telefone do contato: ")
            contato = Contato(nome, numero_telefone)
            agenda.adicionar_contato(contato)
        elif opcao == "2":
            nome = input("Digite o nome do contato para apagar: ")
            agenda.remover_contato(nome)
        elif opcao == "3":
            nome = input("Digite o nome do contato para pesquisar: ")
            contato = agenda.buscar_contato(nome)
            if contato:
                print(contato)
            else:
                print("Contato não foi encontrado!")
        elif opcao == "4":
            nome = input("Digite o nome do contato para atualizar: ")
            novo_nome = input("Digite o novo nome do contato: ")
            novo_numero_telefone = input("Digite o novo número de telefone do contato: ")
            novo_contato = Contato(novo_nome, novo_numero_telefone)
            agenda.atualizar_contato(nome, novo_contato)
        elif opcao == "5":
            agenda.listar_contatos()
        elif opcao == "6":
            break
        else:
            print("Opção não encontrada. Tente mais tarde.")

if __name__ == "__main__":
    main()