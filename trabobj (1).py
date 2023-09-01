from binascii import a2b_base64
from re import A, X
from unicodedata import name
import random

class Heroi(object):
    def __init__(self, name, classe): ##atributos definidos
        self.name = name  #nome

        self.enemy = "inimigo"  #inimigo

        self.alive = True  #player está vivo

        self.classe = classe #classes
        
        self.power = random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)  #define um numero aleatório entre 1 e 6.
    
        self.life = 10 #100% de vida pro player
        
        self.enemylife = 10 #100% de vida pro inimigo

        self.destreza = random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)  #define um numero aleatório entre 1 e 6.
                                                                                
        self.constituição = random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)  #define um numero aleatório entre 1 e 6.

        self.inteligencia = random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)  #define um numero aleatório entre 1 e 6.

        self.carisma = random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)  #define um numero aleatório entre 1 e 6.

        self.numataque = 0

##metodos
    def __str__(self):
        if self.alive:
            return "Nome: %s, Classe: %s, Vida: %i" % (self.name, self.classe, self.life)
        else:
            return "%s(morto)" % (self.name)

    def ataca(self, inimigo):
        ataque = random.randint(1,6)

        if ataque <= 2:
            inimigo.dano(0)
        elif ataque >2 and ataque <= 5:
            inimigo.dano(2)
        else:
            inimigo.dano(6)

    def dano(self, ataque):
        self.numataque += 1

        if self.numataque == 3:
            self.numataque = 0
            self.reconstituir()

        self.life -= ataque
        if self.life <= 0:
            print(self.name, " foi abatido")
    
    def reconstituir(self):
        recupera = random.randint(1,6)

        if recupera <= 2:
            self.life +=0
        elif recupera > 2 and recupera <= 5:
            self.life +=2
        else:
            self.life +=4
            
######## programação

print("MAIN MENU")
player = Heroi("Jogador")
inimigo = Heroi("BOT")
print(player)
print(inimigo)
escolhaclasse = print("ESCOLHA A SUA CLASSE")
print("1-Bárbaro, 2- Mago, 3- Ladrão, 4- Elfo, 5- Clérigo")
int(input())
escolhaclasse = player.classe



while True:
    player.ataca()
    print(inimigo.name, inimigo.life)
    inimigo.ataca()
    print(player.name, player.classe, player.life)



        
           

        
           
        





        

        