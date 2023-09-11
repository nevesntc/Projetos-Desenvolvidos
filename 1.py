class Funcionario:
    def __init__(self, matricula, nome, endereço, bairro, cidade, estado, cep, cargo, data_admis, setor ):

        self.matricula = matricula
        self.nome = nome
        self.endereço = endereço
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado
        self.cep = cep
        self.cargo = None
        self.data_admis = None
        self.setor = None

    def define_admissao(self, data_admis):
        self.data_admis = data_admis

    def define_cargo(self, cargo):

        self.cargo = cargo

    def define_setor(self, setor):

        self.setor = setor

class Cargos:
    def __init__(self, cod_cargo, cargo, atividades):

        self.cod_cargo = cod_cargo

        self.cargo = cargo
        
        self.atividades = atividades

class Setor:
    def __init__(self, cod_setor, nome, supervisor, num_func):

        self.cod_setor = cod_setor
        self.nome = nome
        self.supervisor = supervisor
        self.num_func = num_func

    def defineresponsavel(self, supervisor):
        self.supervisor = supervisor

    def definecargo(self, num_func):
        self.num_func = num_func












































































        

        
    
    