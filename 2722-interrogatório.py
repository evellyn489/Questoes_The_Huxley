class Node:
     def __init__(self, nome, fd):
          self.nome = nome
          self.fd = fd
          self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, nome, fd):
        new_node = Node(nome, fd)
        if self.head == None:
            self.head = new_node
        else:
            pointer = self.head
            while pointer.next != None:
                 pointer = pointer.next
            else:
                pointer.next = new_node
        self.size += 1

    def __getitem__(self, index):
        pointer = self.head

        for a in range(index):
            pointer = pointer.next
        if fi >= pointer.fd:
            if pointer.next != None:
                print(f'Conseguimos interrogar {pointer.nome}, que nos entregou {pointer.next.nome}.')
            else:
                print(f'Agora sim, com a confissao de {pointer.nome}, prendemos todos os canalhas.')
        else: 
            print(f'Droga, a busca acabou em {pointer.nome}.')
            return False
            

    def __len__(self):
        return self.size

    
lista = LinkedList()

fi = int(input())

while True:
    criminoso = input().split()
    nome = criminoso[0]
    if criminoso == ['Fim']:
        break
    fd = int(criminoso[1])
    lista.append(nome, fd)

for i in range(len(lista)):
    if lista[i] == False:
        break
