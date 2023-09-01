from binascii import a2b_base64
from re import A, X
from unicodedata import name
import random

class Heroi(object):
    def __init__(self, name, classe):
        self.name = name
        self.enemy = ""
        self.alive = True
        self.classe = classe
        self.power = random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)
        self.life = 10
        self.enemylife = 10
        self.destreza = random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)
        self.constituição = random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)
        self.inteligencia = random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)
        self.carisma = random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)
        self.numataque = 0

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
            print(self.name, "foi abatido")
    
    def reconstituir(self):
        recupera = random.randint(1,6)

        if recupera <= 2:
            self.life +=0
        elif recupera > 2 and recupera <= 5:
            self.life +=2
        else:
            self.life +=4

print("Bem-vindo ao jogo de RPG!")
nome = input("Digite seu nick: ")
print("Escolha a sua classe: ")
print("1 - Bárbaro")
print("2 - Mago")
print("3 - Ladrão")
print("4 - Elfo")
print("5 - Clérigo")
classe = int(input())
if classe == 1:
    classe_str = "Bárbaro"
elif classe == 2:
    classe_str = "Mago"
elif classe == 3:
    classe_str = "Ladrão"
elif classe == 4:
    classe_str = "Elfo"
else:
    classe_str = "Clérigo"

player = Heroi(nome, classe_str)
inimigo_nome = input("Digite o nome do inimigo: ")
inimigo = Heroi(inimigo_nome, "Inimigo")

print("Simulação de combate iniciada!")
print(player)
print(inimigo)

while player.alive and inimigo.alive:
    player.ataca(inimigo)

while True:
    # vez do jogador
    print("Sua vez de atacar!")
    player.ataca(inimigo)
    print(inimigo)
    if not inimigo.alive:
        print(f"Você venceu! {inimigo.name} foi derrotado.")
        break

    # vez do inimigo
    print(f"Vez de {inimigo.name} atacar!")
    inimigo.ataca(player)
    print(player)
    if not player.alive:
        print(f"Você foi derrotado por {inimigo.name}.")
        break

