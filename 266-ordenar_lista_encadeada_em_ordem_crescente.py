class Node:
    def __init__(self, value):
        self.value = value
        self.previous = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)

        if self.head != None:
            if self.head.value >= value:
                new_node.next = self.head
                self.head = new_node
                return
            pointer = self.head
            while pointer.next != None and pointer.next.value <= value:
                pointer = pointer.next
            new_node.previous = pointer
            new_node.next = pointer.next
            if pointer.next != None:
                pointer.next.previous = new_node
            pointer.next = new_node

        else:
            self.head = new_node

    def __repr__(self):
        pointer = self.head

        r = ''

        while pointer != None:
            r += '' + str(pointer.value) + ' '
            pointer = pointer.next
        return r
    
    def __str__(self):
        return self.__repr__()

lista = DoublyLinkedList()

numeros = [int(x) for x in input().split()]

for elemento in numeros:
    lista.append(elemento)

print(lista)