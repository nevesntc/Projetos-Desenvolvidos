


global fila, spos, rpos, MAX, pilha, ponteiro
MAX = 5
fila = []
spos = 0
rpos = 0

## MAIN MENU

def menu():
     while True:
     
           print(' MAIN MENU ')
           print('#1 PILHA')
           print('#2 FILA')
           print('#3 SAIR')
opção = int(input("DIGITE A OPÇÃO DESEJADA ENTRE 1 E 3 = "))

if opção == 3:
        exit()

if opção == 1 or 2:
     print('[1]- INSERIR ELEMENTO')
     print('[2]- REMOVER ELEMENTO')
     print('[3]- LISTAR CONTEUDO')
     print('[4]- INICIALIZAR PILHA')
     print('[5]- MENU PRINCIPAL')

     opçãopilha = int(input("ESCOLHA UMA DAS OPÇÕES = "))

     if opçãopilha == 1:
        def inserirpilha():
         global pilha, ponteiro, MAX
         if ponteiro == MAX-1:
           print("\nPilha Cheia!!!")
           return()
         else:  
            pilha.append()
            ponteiro = ponteiro + 1
         return()

     if opçãopilha == 2:
        def pop():
            global pilha, ponteiro, rpos, spos
            if  ponteiro < 0:
                print("\nPilha Vazia!!!")
                return()
            else:
             valor = pilha[ponteiro]
            del(pilha[ponteiro])
            ponteiro = ponteiro - 1
            return(valor)
   
     if opçãopilha == 3:

        def push():
          global pilha, ponteiro, MAX
        if ponteiro == MAX-1:
           print("\nLISTA TOTALMENTE CHEIA")
        else:
           fila.append()
        ponteiro = ponteiro + 1

     if opçãopilha == 4:
        def inicializa():
          global pilha, ponteiro
          pilha = []
          ponteiro = -1
          return()

     if opçãopilha == 5:
      exit()
