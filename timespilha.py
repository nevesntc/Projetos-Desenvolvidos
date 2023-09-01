global pilha, ponteiro, MAX

pilha = []
ponteiro = -1
MAX = 5
while True:

    def push():
        global pilha, ponteiro, MAX
        if pilha == MAX-1:
            print("pilha cheia")
        else:
            pilha.append(input(""))
            ponteiro = ponteiro + 1
            return
    def pop():
        global pilha, ponteiro
        if pilha == []:
            print("pilha vazia")
            return
        else:
           opção2 = pilha[ponteiro]
           del(pilha[ponteiro])
           ponteiro = ponteiro - 1
           return(opção2)
    def show():
        print(pilha)

    def menu():

        print("TIMES")
        print("1- ADICIONAR TIMES")
        print("2- REMOVER TIMES ")
        print("3- VISUALIZAR TIMES")
        print("4- SAIR")

        opção = int(input(""))

        if opção == 1:
            push()
        elif opção == 2:
            pop()
        elif opção == 3:
            show()
        elif opção == 4:
            exit()
        else:
            print("OPÇÃO INVÁLIDA")
    menu()


