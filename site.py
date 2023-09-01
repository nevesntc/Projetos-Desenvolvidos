import webbrowser

while True:
    def menu():
        print("MAIN MENU")
        print("1 - SITE")
        print("2 - SAIR")


    def site():
        webbrowser.open("beacons.ai/nevesntc")
        print("ENTRANDO NO SITE...")

#PROGRAMAÇÃO    
    menu()
    opção = int(input("ESCOLHA UMA OPÇÃO         "))
    if opção == 1:
        site()
    elif opção == 2:
        exit()
    else:
        exit()
    

