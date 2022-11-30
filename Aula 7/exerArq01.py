from os import system
import os.path, datetime
system ('cls')

arquivo = 'produtos.csv'

if os.path.isfile(arquivo):
    produtos = open(arquivo,'r', encoding ='utf-8')
    tamanho = os.path.getsize(arquivo)
    dataModificacao = os.path.getmtime(arquivo)
    print(f'Data de modificacao: {datetime.datetime.fromtimestamp(dataModificacao)}')
    print(f'Tamanho do arquivo(bytes): {tamanho}')

    listaProdutos = []
    for linha in produtos:
        colunas = linha.strip().split (";")
        print(colunas) 
        colunas[0]= int(colunas[0])
        colunas[2]= int(colunas[2])
        colunas[4]= int(colunas[4])
        colunas[5]= int(colunas[5])
        colunas[6]= int(colunas[6])
        colunas[7]= int(colunas[7])
        colunas[8]= float(colunas[8])
        colunas[9]= float(colunas[9])
        listaProdutos.append(colunas)
    produtos.close ()
    for prod in listaProdutos:
        print(prod)
     

    #calculando total de custo
    totalCusto = 0
    for prod in listaProdutos:
        totalCusto += prod [9]
    print(f'Total do custo: {totalCusto}')