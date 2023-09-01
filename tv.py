#Exemplo de Classe em Python

class Televisao:
    def __init__(self,maxchannel=4):
        self.ligada = False
        self.canal = 3
        self.maxchannel = maxchannel

    def Power(self):
        if self.ligada == False:
            self.ligada = True
        else:
            self.ligada = False

    def UpChannel(self):
        if self.canal < self.maxchannel:
            self.canal += 1
        else:
            self.canal = 1

    def DownChannel(self):
        if self.canal > 1:
            self.canal -= 1
        else:
            self.canal = self.maxchannel
            

# Criando um objeto (instância da classe)
tv01 = Televisao()
tv02 = Televisao(99)

print(tv01.ligada)
print(tv01.canal)

tv01.UpChannel()
tv01.Power()
print(tv01.ligada)
print(tv01.canal)

tv01.UpChannel()
print(tv01.canal)
tv01.DownChannel()
print(tv01.canal)

print(tv02.maxchannel)
