class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self) -> None:
        self.top = None
        self._size = 0
    
    def __len__(self):
        return self._size
    
    def append(self, element):
        node = Node(element)
        node.next = self.top
        self.top = node

        self._size += 1

    def pop(self):
        if self.top:
            node = self.top
            self.top = self.top.next
            self._size -= 1
            return node.data
        else:
            self._size -= 1
            return False
        
    def peek(self):
        return self.top.data
    
    def __repr__(self) -> str:
        pointer = self.top
        string = ''

        while pointer:
            string += str(pointer.data) + '\n'
            pointer = pointer.next
        return string
    
    def __str__(self) -> str:
        return self.__repr__()

qtd_string = int(input())

for i in range(qtd_string):
    balanceado = False
    string = input()
    pilha_parenteses = Stack()
    pilha_colchetes = Stack()

    for item in string:
        if item == '(':
            pilha_parenteses.append('(')
        elif item == '[':
            pilha_colchetes.append('[')
        if item == ')':
            if len(pilha_parenteses) > 0:
                pilha_parenteses.pop()
            else:
                pilha_parenteses.append(')')
                break
        elif item == ']':
            if len(pilha_colchetes) > 0:
                pilha_colchetes.pop()
            else: 
                pilha_colchetes.append(']')
                break

    if len(pilha_parenteses) == 0 and len(pilha_colchetes) == 0:
        balanceado = True
    
    if balanceado:
        print('Yes')
    else:
        print('No')