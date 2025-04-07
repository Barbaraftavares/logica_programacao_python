class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True

    def __str__(self):
        return f"Livro(titulo={self.titulo}, autor={self.autor}, disponivel={self.disponivel})"

    def __eq__(self, outro):
        return self.titulo == outro.titulo and self.autor == outro.autor

class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro):
        if livro in self.livros:
            raise Exception(f"Livro '{livro.titulo}' já existe na biblioteca!")
        print(f"Livro '{livro.titulo}' adicionado com sucesso!")
        self.livros.append(livro)

    def emprestar_livro(self, titulo):
        for livro in self.livros:
            if livro.titulo == titulo:
                if not livro.disponivel:
                    raise Exception(f"Livro '{livro.titulo}' não está disponível para ser emprestado!")
                print(f"Livro '{titulo}' emprestado com sucesso!")
                livro.disponivel = False
                return
        raise Exception(f"Livro '{titulo}' não encontrado na biblioteca!")

    def devolver_livro(self, titulo):
        for livro in self.livros:
            if livro.titulo == titulo:
                if livro.disponivel:
                    raise Exception(f"Livro '{titulo}' já está disponível na biblioteca!")
                print(f"Livro '{titulo}' foi devolvido com sucesso!")
                livro.disponivel = True
                return
        raise Exception(f"Livro '{titulo}' não foi encontrado na biblioteca!")

def main():
    biblioteca = Biblioteca()
    try:
        #Adicionando Livros
        livro1 = Livro("Livro 1", "Autor 1")
        livro2 = Livro("Livro 2", "Autor 1")
        livro3 = Livro("Livro 3", "Autor 1")
        livro4 = Livro("Livro 4", "Autor 1")

        biblioteca.adicionar_livro(livro1)
        biblioteca.adicionar_livro(livro2)
        biblioteca.adicionar_livro(livro3)
        biblioteca.adicionar_livro(livro4)

        #Tentando adicionar novamente Livro 1
        novo_livro1 = Livro("Livro 1", "Autor 1")
        biblioteca.adicionar_livro(novo_livro1)
    except Exception as e:
        print(e)

    print("\n**************************\n")

    try:
        # Emprestando Livros
        biblioteca.emprestar_livro("Livro 1")
        biblioteca.emprestar_livro("Livro 3")
        biblioteca.emprestar_livro("Livro 1")
    except Exception as e:
        print(e)

    try:
        # Emprestando Livro Inexistente
        biblioteca.emprestar_livro("Livro 10")
    except Exception as e:
        print(e)

    print("\n**************************\n")

    try:
        #Devolvendo Livros
        biblioteca.devolver_livro("Livro 1")
        biblioteca.devolver_livro("Livro 2")
    except Exception as e:
        print(e)

    try:
        #Devolvendo Livro Inexistente
        biblioteca.devolver_livro("Livro 10")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
