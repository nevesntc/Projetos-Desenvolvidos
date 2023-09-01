global fila, MAX, spos, rpos

def inicializa():
    global fila, MAX, spos, rpos
    MAX = 4
    fila = []
    spos = 0   #Aponta para a próxima posição livre na fila
    rpos = 0   #Aponta para o elemento a ser retirado da fila

    for i in range(0,MAX):
        fila.append(None)
    return

def push(valor):
    global spos, fila, MAX

    if spos == MAX:
        print("\nFila cheia")
        return

    fila[spos] = valor
    spos += 1
    return

def pop():
    global spos, rpos, fila

    if rpos == spos:
        print("\nFila Vazia!!!")
        return
    
    rpos += 1
    valor = fila[rpos-1]
    fila[rpos-1] = None
    return(valor)

def mostra():
    global spos, rpos, fila

    if rpos == spos:
        print("\nFila Vazia!!!")
        return
    
    for i in range(rpos,spos):
        print(fila[i])

    return

def mostra_p():
    global spos, rpos, fila
    print("rpos = ",rpos,"    spos = ", spos)
    return


### Testando a fila ###
inicializa()
mostra_p()
push(100)
push(200)
push(300)
push(400)
mostra()
mostra_p()
push(500)
pop()
pop()
mostra()
mostra_p()
pop()
pop()
mostra_p()
mostra()
pop()
    

    
    

