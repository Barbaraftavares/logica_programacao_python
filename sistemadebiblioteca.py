class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True

    def __str__(self):
        return f"Livro(titulo={self.titulo}, autor={self.autor}, disponivel={self.disponivel})"

class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionarlivro(self, livro):
        if livro in self.livros:
            raise Exception("Livro já existe na biblioteca!")
        self.livros.append(livro)
        print("Livro adicionado com sucesso!")

    def emprestarlivro(self, titulo):
        for livro in self.livros:
            if livro.titulo == titulo:
                if not livro.disponivel:
                    raise Exception("Livro não está disponível para ser emprestado!")
                livro.disponivel = False
                print("Livro emprestado com sucesso!")
                return
        raise Exception("Livro não encontrado na biblioteca!")

    def devolverlivro(self, titulo):
        for livro in self.livros:
            if livro.titulo == titulo:
                if livro.disponivel:
                    raise Exception("Livro já está disponível na biblioteca!")
                livro.disponivel = True
                print("Livro foi devolvido com sucesso!")
                return
        raise Exception("Livro não foi encontrado na biblioteca!")

def main():
    biblioteca = Biblioteca()

    try:
        livro1 = Livro("Livro 1", "Autor 1")
        biblioteca.adicionarlivro(livro1)
        livro2 = Livro("Livro 1", "Autor 1")
        biblioteca.adicionarlivro(livro2)  # Lança exceção
    except Exception as e:
        print(e)

    try:
        biblioteca.emprestarlivro("Livro 1")
        biblioteca.emprestarlivro("Livro 1")  # Lança exceção
    except Exception as e:
        print(e)

    try:
        biblioteca.devolverlivro("Livro 2")  # Lança exceção
        biblioteca.devolverlivro("Livro 1")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()