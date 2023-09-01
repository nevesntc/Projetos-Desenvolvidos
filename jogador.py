class Livro:
    def __init__(self, nome, paginas, autor, preco):
        self.nome = nome
        self.paginas = paginas
        self.autor = autor
        self.preco = preco

    def get_preco(self):
        return self.preco

    def set_preco(self, novo_preco):
        self.preco = novo_preco

a = Livro("Diário de um Banana", 20, "Não Sei", 20)
print(a.get_preco())

a.set_preco(30)
print(a.get_preco())
