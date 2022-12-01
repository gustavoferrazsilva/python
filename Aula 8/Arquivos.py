import os.path

class tabCat:
    def dicCat(self):
        arquivo = 'categorias.csv' #caminho do arquivo
        categorias = open(arquivo, 'r', encoding='utf-8')
        #abre somente leitura o caminho do arquivo e armazena em uma variavel
        dicCategoria = {} #instaciar uma variavel do tipo dicionario

        if os.path.isfile(arquivo): #verifica se o caminho do arquivo é valido
            for line in categorias: #para cada linha do arquivo
                colunas = line.strip().split(';') 
                #retira os espacos e separa em lista as colunas
                dados =[colunas[1], colunas[2]]
                #armazena em dados uma lista com os valores da coluna 1 e 2
                dicCategoria[colunas[0]] = dados
                #cria uma chave com o valor da coluna 0 e associa o valor com os dados

            
            categorias.close() #fecha o arquivo
            return dicCategoria

class tabProd:
    def listProd(self):
        arquivo = 'produtos.csv'

        if os.path.isfile(arquivo):
            produtos = open(arquivo,'r', encoding='utf-8')
            listaProdutos = []
            for linha in produtos:
                colunas = linha.strip().split(";")
                colunas[0] = int(colunas[0])
                colunas[2] = int(colunas[2])
                colunas[4] = int(colunas[4])
                colunas[5] = int(colunas[5])
                colunas[6] = int(colunas[6])
                colunas[7] = int(colunas[7])
                colunas[8] = float(colunas[8])
                colunas[9] = float(colunas[9])
                listaProdutos.append(colunas)
            produtos.close()
            return listaProdutos