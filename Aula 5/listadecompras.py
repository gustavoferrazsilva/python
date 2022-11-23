# Lista de compras

from os import system
system ('cls')
titulo = 'CALCULAR LISTA DE COMPRAS'
print(titulo.center(80,'#'))

produtosDesc = []
produtosPreço = []
numeroItens = int(input('Informe numero de itens desejados: '))
for i in range (0,numeroItens):
    nomeProduto = input (f'nome do produto {i+1}: ')
    precoProduto = float(input(f'Preço do {nomeProduto}: '))
    produtosDesc.append(nomeProduto)
    produtosPreço.append(precoProduto)
total = 0
for i in range (0,numeroItens):
    print (f'{produtosDesc[i]} - R$ {produtosPreço[i]}')
    total += produtosPreço[i]
print(f'Total: R$ {total}')

print (produtosDesc)
print (produtosPreço)
