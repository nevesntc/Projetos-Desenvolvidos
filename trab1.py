class supervisor():
    def __init__(self, matricula=0, nome='', idade=0, admissao=0, setor='', cargo=''):
        self.matricula = matricula
        self.nome = nome
        self.idade = idade
        self.admissao = admissao
        self.setor = setor
        self.cargo = cargo

    def getidade(self):
        return self.idade

class funcionario(supervisor):
    def __init__(self, matricula, nome, idade, admissao, setor, cargo):
        super().__init__(matricula, nome, idade, admissao, setor, cargo)

    def mudasetor(self, setor):
        self.setor = setor

# programa principal

a = supervisor(202312035, 'Bruno', 20, '2022-01-01', 'administração', 'funcionario')

print(a.matricula)
print(a.nome)
print(a.idade)
print(a.admissao)
print(a.setor)
print(a.cargo)

f = funcionario(123, 'João', 30, '30-04-2023', 'produção', 'operador')
f.mudasetor('desenvolvimento')
print(f.setor)
