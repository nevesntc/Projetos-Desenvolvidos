class Triangulo:
    def __init__(self, ladoa, ladob, ladoc):
        self.ladoa = ladoa
        self.ladob = ladob
        self.ladoc = ladoc
    
    def calcularperimetro(self):
        return self.ladoa +self.ladob + self.ladoc

    def getmaiorlado(self):
        return max(self.ladoa, self.ladob, self.ladoc)

    def programa(self):
    
        ladoa = float(input("Digite um valor para o lado A"))
        ladob = float(input("Digite um valor para o lado B"))
        ladoc = float(input("Digite um valor para o lado B"))

        triangulo = Triangulo(ladoa, ladob, ladoc)
        perimetro = triangulo.calcularperimetro()
        maiorlado = triangulo.getmaiorlado()

        print("Perimetro do Triangulo", perimetro)
        print("Maior lado do triangulo", maiorlado)

        

        