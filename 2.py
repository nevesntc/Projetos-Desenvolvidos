from datetime import datetime

class Aluno:
    def __init__(self,matricula, nome, dt_nascimento, nota_p1, nota_p2):

        self.matricula = matricula
        self.nome = nome
        self.dt_nascimento = datetime.strptime(dt_nascimento, "%d/%m/%y")
        self.nota_p1 = nota_p1
        self.nota_p2 = nota_p2 

    def idade(self):

        hoje = datetime.now()
        idade = hoje.year - self.dt_nascimento.year

        if hoje.month < self.dt_nascimento.month or (hoje.month == self.dt_nascimento.month and hoje.day < self.dt_nascimento.day):
            idade -=1
        return idade

    def media(self):
        (self.nota_p1 + self.nota_p2) / 2

    def resultado(self):

        if self.media < 4:
            print("reprovado")
        elif self.media >= 4 and self.media <=7:
            print("recuperação")
        else:

            print("aprovado")

            
        

    