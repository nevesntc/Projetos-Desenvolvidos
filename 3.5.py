class Livro:
    def __init__(self, nome, qtdpaginas, autor, preco):
        self.nome = nome
        self.qtdpaginas = qtdpaginas
        self.autor = autor
        self.preco = preco

    def getpreco(self):
        return self.preco

    def setpreco(self, novopreco):
        self.preco = novopreco
livro = Livro("O Senhor dos Aneis", 1000, "Tolkien", 50,0)
print("Preço do Livro", livro.getpreco())
livro.setpreco(55,0)
print("Novo preço do livro:", livro.getpreco())

        