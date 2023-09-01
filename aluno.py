from datetime import datetime

class Aluno:
    def __init__(self, matricula, nome):
        self.matricula = matricula
        self.nome = nome
        self.dt_nascimento = None
        self.idade = None
        self.nota_p1 = None
        self.nota_p2 = None
        self.media = None
        self.resultado = None
    
    def calcidade(self):
        data_nascimento = input("Digite sua data de nascimento (formato: dd/mm/aaaa): ")
        data = datetime.strptime(data_nascimento, "%d/%m/%Y")
        hoje = datetime.strptime("23/5/2023", "%d/%m/%Y")
        idade = hoje.year - data.year
        print("Idade:", idade)

    def mediaaluno(self):
        nota_p1 = float(input("Insira sua nota da P1: "))
        nota_p2 = float(input("Insira sua nota da P2: "))
        media = (nota_p1 + nota_p2) / 2
        print("Média:", media)

    def resultadototal(self):
        if self.media < 4:
            resultado = "Reprovado"
        elif self.media >= 4 and self.media < 7:
            resultado = "Recuperação"
        else:
            resultado = "Aprovado"
        print("Resultado:", resultado)

a = Aluno("2023503020", "José")
print(a)
Aluno.calcidade(self=None)
Aluno.mediaaluno(self=None)
Aluno.resultadototal(self=None)
