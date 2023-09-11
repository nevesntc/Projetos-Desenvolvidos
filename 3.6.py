class Aluno:
    def __init__(self, nome, curso, temposemdormir):

        self.nome = nome
        self.curso = curso
        self.temposemdormir = temposemdormir

    def estudar(self, horasestudo):
        self.temposemdormir += horasestudo

    def dormir(self, horassono):
        self.temposemdormir -= horassono

    def gettemposemdormir(self):
        return(self.temposemdormir)

aluno = Aluno("Bruno", "Software", 24)
print("Tempo sem dormir", aluno.gettemposemdormir())
aluno.estudar(5)
print("Tempo sem dormir após estudar", aluno.gettemposemdormir())
aluno.dormir(8)
print("Tempo sem dormir após dormir", aluno.gettemposemdormir())