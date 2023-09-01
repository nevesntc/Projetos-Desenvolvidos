class Funcionario():
    def __init__(self, nome='', cpf=0, salario=0, departamento=0):
        self.nome = nome
        self.cpf = cpf
        self.salario = salario
        self.departamento = departamento

    def premiar(self, percentual):
        self.salario *= (1 + percentual/100)

class Coordenador(Funcionario):
    def __init__(self, nome='', cpf=0, salario=0, departamento="estagio", senha='', funcionariossubornados=20):
        super().__init__(nome, cpf, salario, departamento)
        self.senha = senha
        senha = 1234
        self.funcionariossubornados = funcionariossubornados

    def confirmasenha(self, senha):
        return self.senha == senha

a = Coordenador(nome='Bruno', cpf=123456789, salario=5000, departamento='TI', senha='1234', funcionariossubornados=5)
print(a.nome)
print(a.confirmasenha('1234'))
