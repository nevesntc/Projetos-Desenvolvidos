#!c:\python36\python.exe
# -*- coding: ISO-8859-1 -*-
"""
@author: Maverick

HERANÇA e POLIMORFISMO
Uma classe pode herdar características de outra 
(superclasse) e incluir suas próprias. A superclasse é mais 
genérica, a subclasse, que herda da superclasse, é mais 
especializada. Essa funcionalidade recebe o nome de Herança

Polimorfismo é semelhante à Heranca, porém, nesse caso,
a subclasse pode adicionar alguma informação (atributo ou 
método, além daquelas herdadas da superclasse).
"""
class Pessoa:
    def __init__(self, nome ='', idade=0):
       self.nome = nome
       self.idade = idade
    def getIdade(self):
       return self.idade

class PessoaFisica(Pessoa):
    def __init__(self, CPF, nome='', idade=0):
       Pessoa.__init__(self, nome, idade)
       self.CPF = CPF

class PessoaJuridica(Pessoa):
    def __init__(self, CNPJ, nome='', idade=0):
       Pessoa.__init__(self, nome, idade)
       self.CNPJ = CNPJ

# Programa Principal
a = Pessoa()
Pessoa.__init__(a, 'Juvenelcio', 22)
b = PessoaFisica('122.333.332-1', nome='Cezefredo', idade=50)
banco = PessoaJuridica('00.000.000/0001-11',nome='Banco do Dinheiro',idade=43)

print(a.nome)   
print(a.idade)  
print(b.CPF)
print(b.getIdade())
print(b.nome)   
print(banco.CNPJ) 
