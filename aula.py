from re import X
from unicodedata import name
class Tank(object):
    def __init__(self, name):
        self.name = name
        self.alive = True
        self.ammo = 5
        self.armor = 60
    def __str__(self):
        if self.alive:
        
            return "%s (%i armadura, %i tiros)" % (self.name, self.armor, self.ammo)
        else:
            return "%s(Destruído)" % (self.name)
    def fire_at(self,enemy):
        if self.ammo>= 1:
           self.ammo -= 1
           print(self.name, "atirou em", enemy.name)
           enemy.hit()
        else:
           print(self.name, "não possui munição")
    def hit(self):
        self.armor -= 20
        print(self.name, "foi atingido...")
        if  self.armor<= 0:
            self.explode()
    def explode(self):
            self.alive = False
            print(self.name, "explodiu...")
            
#### CRIANDO O OBJETO
player = Tank("NEVES")
inimigo = Tank("BOT")
print(player)
print(inimigo)

#atacando
player.fire_at(inimigo)
print(player.ammo)
print(inimigo.armor)

#restaurar armadura em +20
(armadura) = (player.armor) + 20
print(armadura)
# armadura 100%
(totalarmadura) = (player.armor) + 40
(player.armor) = 60
print(totalarmadura)