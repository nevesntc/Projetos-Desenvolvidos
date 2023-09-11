class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def aumentasalario(self, percdeaumento):
        aumento = self.salario *(percdeaumento / 100)
        self.salario += aumento

harry = Funcionario("Harry", 25000)
print("Salario antes do aumento:", harry.salario)
harry.aumentasalario(10)
print("Salario pós aumento", harry.salario)

