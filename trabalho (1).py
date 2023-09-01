from binascii import a2b_base64
from re import A, X
from unicodedata import name
import random

class Heroi(object):
    def __init__(self, name,): ##atributos definidos
        self.name = name  #nome

        self.enemy = print("Inimigo")  #inimigo
        

        self.alive = True  #player está vivo

        self.classe = habilidade
        habilidade = print("Temos as classes ---- Bárbaro, Mago, Ladrão, Elfo, Clérigo")
        str(input("Escolha a sua Classe ----   "))
                     
        self.power = random.randint(6) + random.randint(6) + random.randint(6)  #define um numero aleatório entre 1 e 6.
    
        self.life = 10 #100% de vida pro player
        
        self.enemylife = 10 #100% de vida pro inimigo

        self.destreza = random.randint(6) + random.randint(6) + random.randint(6)
                                                                                
        self.constituição = random.randint(6) + random.randint(6) + random.randint(6)

        self.inteligencia = random.randint(6) + random.randint(6) + random.randint(6)

        self.carisma = random.randint(6) + random.randint(6) + random.randint(6)

##metodos
    def __str__(self):
        if self.alive:
            return "%s (%i name, %iclasse, %ivida)" % (self.name, self.classe, self.life)
        else:
            return "%s(morto)" % (self.name)

    def __ataca__(self):
        if self.enemylife>=1:
           self.enemylife -=1
           print(self.name, "atirou em", self.enemy)
        else:
            print(self,name, "tu não consegue atacar, doidao")

    def dano(self):
        self.life = -(random.randint(6))
        print(self.name, "foi atingido...")

        if self.life <= 2:
           return(self.name, self.classe, "valor 0")

        elif self.life >2<=5:
           return(self.name, self.classe, "valor 2")
        
        elif self.life == 6:
           return(self.name, self.classe, "valor 4")

        elif self.life <= 0:
            self.morreu()
    def morreu(self):
        self.alive = False
        print(self.name, self.classe, "morreu")

    def reconstituir(enemy,valor):
        if valor <=2:
           return("A VIDA NÃO PODE SER RECONSTITUIDA")

        elif valor >2<=5:
            return(enemy.life + 2)

        elif valor == 6:
            return(enemy.life + 4)
