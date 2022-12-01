from os import system
import os.path, datetime
system ('cls')

arquivo = 'categorias.csv'
categorias = open(arquivo,'r',encoding='utf-8')
# abre somente leitura o caminho do arquivo e armazena em uma variável
dicCategoria = {} #instanciar uma variável do tipo dicionario

if os.path.isfile(arquivo): # strip é para remover espaços em branco. #split delimita caracter separador
    for line in categorias: # para cada linha do arquivo
        colunas =line.strip().split(';')
        # retira os espaços e separa em lista as colunas
        dados = [colunas[1],colunas[2]]
        # armazena em dados uma lista com os valores da coluna 1 e 2
        dicCategoria[colunas[0]] = dados
        # cria uma chave com o valor da coluna 0 e associa com os dados

    categorias.close() # fecha o arquivo
    print(dicCategoria) # exibe o dicionario 