class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self._size = 0

    def push(self, elemento):
        node = Node(elemento)

        node.next = self.top
        self.top = node
        self._size += 1

    def pop(self):
        if self._size >0:
            node = self.top
            self.top = self.top.next
            self._size -= 1
        else:
            raise IndexError
        
    def __repr__(self):
        c = 0
        r = ''
        pointer = self.top

        while pointer != None:
            r += str(pointer.data)
            c += 1
            if c < self._size:
                r += ' '
            pointer = pointer.next
        return r
    
    def __str__(self):
        return self.__repr__()
    
pilha = Stack()

while True:
    comando = input().split()
    if comando[0] == 'Empilhar':
        pilha.push(comando[1])
        print(pilha)
    elif comando[0] == 'Desempilhar':
        pilha.pop()
        print(pilha)
    else:
        break