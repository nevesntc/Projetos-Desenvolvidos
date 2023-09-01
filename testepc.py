class gamer:
    def __init__(self, nome, precopc, idade):

        self.nome=nome
        self.precopc=precopc
        self.idade=idade
    def __str__(self):
        return f" {self.nome}, {self.precopc}, {self.idade}"
    

class cpu(gamer):
    def __init__(self, nome, precopc, idade, placadevideo):
        super().__init__(nome, precopc, idade)
        self.placadevideo = placadevideo
    def __str__(self):
        return f" {self.nome}, {self.precopc}, {self.idade},{self.placadevideo}"

a = gamer("Bruno", 4500, 20)
b = cpu("Bruno", 4500, 20, "gtx1660")
print(isinstance(b, gamer), isinstance(b, cpu))
print(isinstance(a, gamer))