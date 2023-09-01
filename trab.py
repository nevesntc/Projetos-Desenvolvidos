global fila, spos, rpos, MAX, pilha, ponteiro, opção
MAX = 5
fila = [10,20,30]
spos = 0
rpos = 0
pilha = [10,20,30]
## MAIN MENU
while True:
    def menu():
        print(' MAIN MENU ')
        print('#1 PILHA')
        print('#2 FILA')
        print('#3 SAIR')

    def inicializa1():
        global pilha, ponteiro
        pilha = []
        ponteiro = -1
        return

    def push1():
        global pilha, ponteiro, MAX, valor
        if pilha == MAX:
           print("FILA CHEIA")
        pilha.append(int(input("ESCOLHA UM NÚMERO --------->                  ")))
        return

    def pop1():

        global pilha, ponteiro
    
        if pilha == 0:
           print("\nPilha Vazia!!!")
           return
        else:
            pilha.pop(0)
            return
    def show1():
        global pilha
        print(pilha)
        return

    def programa1():
        print('[1]- INSERIR ELEMENTO')
        print('[2]- REMOVER ELEMENTO')
        print('[3]- LISTAR CONTEUDO')
        print('[4]- INICIALIZAR PILHA')
        print('[5]- MENU PRINCIPAL')
        opção2 = int(input("ESCOLHA UMA OPÇÃO --------->         "))
        if opção2 == 1:
           push1()
        elif opção2 == 2:
             pop1()
        elif opção2 == 3:
             show1()
        elif opção2 == 4:
             inicializa1()
        elif opção2 == 5:
             menu()
        else:
             menu()

#PROGRAMAÇÃO

    menu()
    opção = int(input("ESCOLHA UMA OPÇÃO --------->         "))
    if opção == 1:
       programa1()
    elif opção == 2:
       programa1()
    elif opção == 3:
        exit()
    else:
        print("NÃO É UMA OPÇÃO VÁLIDA")

       
      
 
