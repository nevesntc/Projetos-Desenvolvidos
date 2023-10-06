#Bruno Lourenço Neves - Matrícula: 202312035

class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None

class NaoOrdenada:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def add(self, data):
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def search(self, target):
        current = self.head
        while current is not None:
            if current.data == target:
                return True
            current = current.next_node
        return False

    def remove(self, target):
        if self.head is None:
            return

        if self.head.data == target:
            self.head = self.head.next_node
            return

        current = self.head
        previous = None
        while current is not None:
            if current.data == target:
                previous.next_node = current.next_node
                return
            previous = current
            current = current.next_node

    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end=' -> ')
            current = current.next_node
        print("None")

class Ordenada:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def add(self, data):
        new_node = Node(data)
        if self.head is None or data < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            previous = None
            while current is not None and current.data < data:
                previous = current
                current = current.next_node
            new_node.next_node = current
            previous.next_node = new_node

    def search(self, target):
        current = self.head
        while current is not None:
            if current.data == target:
                return True
            if current.data > target:
                return False
            current = current.next_node
        return False

    def remove(self, target):
        if self.head is None:
            return

        if self.head.data == target:
            self.head = self.head.next_node
            return

        current = self.head
        previous = None
        while current is not None:
            if current.data == target:
                previous.next_node = current.next_node
                return
            previous = current
            current = current.next_node

    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end=' -> ')
            current = current.next_node
        print("None")

def main():
    lista_nao_ordenada = NaoOrdenada()
    lista_ordenada = Ordenada()

    while True:
        print("\nTRABALHANDO COM LISTAS ENCADEADAS")
        print("1 – Lista encadeada ordenada")
        print("2 – Lista encadeada não-ordenada")
        print("3 – Desenvolvedor")
        print("4 – Finalizar programa")

        choice = input("Escolha uma opção: ")

        if choice == '1':
            while True:
                print("\nLISTA ENCADEADA ORDENADA")
                print("1 – Criar lista")
                print("2 – Adicionar elemento na lista")
                print("3 – Excluir elemento da lista")
                print("4 – Procurar elemento da lista")
                print("5 – Mostrar lista")
                print("6 – Voltar para o menu anterior")

                sub_choice = input("Escolha uma opção: ")

                if sub_choice == '1':
                    lista_ordenada = Ordenada()
                    print("Lista ordenada criada com sucesso!")

                elif sub_choice == '2':
                    element = int(input("Digite o elemento a ser adicionado: "))
                    lista_ordenada.add(element)
                    print("Elemento adicionado com sucesso!")

                elif sub_choice == '3':
                    element = int(input("Digite o elemento a ser excluído: "))
                    lista_ordenada.remove(element)
                    print("Elemento excluído com sucesso!")

                elif sub_choice == '4':
                    element = int(input("Digite o elemento a ser procurado: "))
                    if lista_ordenada.search(element):
                        print("Elemento encontrado na lista!")
                    else:
                        print("Elemento não encontrado na lista.")

                elif sub_choice == '5':
                    lista_ordenada.display()

                elif sub_choice == '6':
                    break

                else:
                    print("Opção inválida. Por favor, escolha uma opção válida.")

        elif choice == '2':
            while True:
                print("\nLISTA ENCADEADA NÃO-ORDENADA")
                print("1 – Criar lista")
                print("2 – Adicionar elemento na lista")
                print("3 – Excluir elemento da lista")
                print("4 – Procurar elemento da lista")
                print("5 – Mostrar lista")
                print("6 – Voltar para o menu anterior")

                sub_choice = input("Escolha uma opção: ")

                if sub_choice == '1':
                    lista_nao_ordenada = NaoOrdenada()
                    print("Lista não ordenada criada com sucesso!")

                elif sub_choice == '2':
                    element = int(input("Digite o elemento a ser adicionado: "))
                    lista_nao_ordenada.add(element)
                    print("Elemento adicionado com sucesso!")

                elif sub_choice == '3':
                    element = int(input("Digite o elemento a ser excluído: "))
                    lista_nao_ordenada.remove(element)
                    print("Elemento excluído com sucesso!")

                elif sub_choice == '4':
                    element = int(input("Digite o elemento a ser procurado: "))
                    if lista_nao_ordenada.search(element):
                        print("Elemento encontrado na lista!")
                    else:
                        print("Elemento não encontrado na lista.")

                elif sub_choice == '5':
                    lista_nao_ordenada.display()

                elif sub_choice == '6':
                    break

                else:
                    print("Opção inválida. Por favor, escolha uma opção válida.")

        elif choice == '3':
            print("\nDESENVOLVEDOR")
            print("Bruno Neves")
            input("Pressione qualquer tecla para voltar para o menu anterior: ")

        elif choice == '4':
            print("Programa finalizado.")
            break

        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()
