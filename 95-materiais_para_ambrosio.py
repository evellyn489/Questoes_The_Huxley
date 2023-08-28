dinheiro = float(input())
itens = int(input())

produtos = {}
for i in range(itens):
    nome_preco = input().split()

    produtos.copy()
    nome = nome_preco[0]
    preco = float(nome_preco[1])

    produtos[nome] = preco
    
menor_preco = dict(sorted(produtos.items(), key = lambda item: item[1]))
compra = {}

valor_total = 0
for chave, valor in menor_preco.items():
    valor_total += valor
    if valor_total > dinheiro:
        valor_total -= valor
        break
    compra[chave] = valor

ordem_alfabetica = dict(sorted(compra.items(), key=lambda item:item[0]))

for objeto, preco in ordem_alfabetica.items():
    print(f'{objeto} {preco:.2f}')

troco = dinheiro - valor_total

print(f'{troco:.2f}')