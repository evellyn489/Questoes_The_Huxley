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
    
    def __len__(self):
        return self._size

    def __getitem__(self, index): 
        pointer = self.top
        for i in range(index):
            if pointer != None:
                pointer = pointer.next
            else:
                raise IndexError('Index no existing')
        return pointer.data
    
    def __setitem__(self, index, elemento):
        pointer = self.top
        for i in range(index):
            if pointer != None:
                pointer = pointer.next
            else:
                raise IndexError('Index no existing')
        pointer.data = elemento

    def __repr__(self):
        r =''
        pointer = self.top
        while pointer != None:
            r += str(pointer.data) + '\n'
            pointer = pointer.next
        return r
    
    def __str__(self):
        return self.__repr__()



qtd_amigos = int(input())
nomes = Stack()
comidas = Stack()

for i in range(qtd_amigos):
    nome, comida = [x for x in input().split()]
    
    nomes.push(nome)
    comidas.push(int(comida))

for i in range(len(nomes)):
    print(f'{nomes[i]} foi servido(a).')
    while comidas[i] > 400:
        print(f'Fica tranquilo(a), {nomes[i]} pode se servir novamente!')
        comidas[i] -= 400
        print(f'{nomes[i]} foi servido(a).')
        
