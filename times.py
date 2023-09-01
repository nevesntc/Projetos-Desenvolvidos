##estrutura de fila times

global fila, spos, rpos
MAX = 4
fila = []
spos = 0
rpos = 0

while True:
    def push():
        global fila, spos, MAX
        if fila == MAX:
           print("fila cheia")
        else:
            fila.append(input(""))
            spos = spos + 1
            return

    def pop():
        global fila, rpos, spos
        if fila == 0:
           print("fila vazia")
        else:
           fila.pop(0)
           rpos = rpos - 1
           return

    def show():
        print(fila)
        return

    def menu():
        print("CARIOCÃO")
        print("1- ADICIONAR TIME")
        print("2- REMOVER TIME")
        print("3- MOSTRAR A LISTA")
        print("4- SAIR")
        opção = int(input(""))
        if opção == 1:
           push()

        elif opção ==2:
            pop()
    
        elif opção == 3:
            show()
    
        elif opção == 4:
             exit()

        else:
            print("NÃO É UMA OPÇÃO VÁLIDA")

    menu()

