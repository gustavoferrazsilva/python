import io
from Arquivos import tabCat
from Arquivos import tabProd

cat = tabCat() # instanciando o objetvo da classe
prod = tabProd() # instanciando o objeto da classe

dicCategoria = cat.dicCat() # chamando a função/ método do objeto
listaProdutos = prod.listProd() # chamando a função / método do obnjeto

relatorio = open("relatorio.txt", mode="w", encoding="utf-8")
# open metodo que no 'w' ele edita, escreve, cria um arquivo
for item in dicCategoria: # percorrendo (loop) no dicionário de categoria
    titulo = f'{dicCategoria[item][0]}\n{dicCategoria[item][1]}\n\nProdutos\n'
    prod = []
    # lista vazia para armazenar todos os produtos pro categoria
    for itemP in listaProdutos: # percorre a listaprodutos do arquivo
        if str(itemP[2]) == item: # compara com a coluna  com o valor de item
            valor = f'{itemP[8]:.2f}' # pega o calor do produto e formata
            produto = '''{:<60} | R$ {:>8}
            ''' . format(str(itemP[1].capitalize() + ' ' + itemP[3])[0:60], valor) 
            # pego a descrição e embalagem e formato a frase
            prod.append(produto)
            # adiciona produto na lista prod
    prod.sort()
    # ordendo a lista por ordem alfanumerica
    lista = ''
    i = 1
    # indice para ordem 'código' do reltáorio
    for p in prod:
        lista += '{:>4}. {}\n' . format(i,p)
        i+=1 # incerementa mais uma na posição do item no relatório
    divisor = ' Categoria ' .center(80,'*')
    # divisor de reltório
    relatorio.write(divisor + '\n' + titulo + lista + '\n\n')
    # escrever no arquivo texto
categorias = 'Total de Categorias: {:>4}' . format(len(dicCategoria))
produtos = 'Total de produtos: {:>4}' . format(len(listaProdutos))
resumo = ' Resumo ' .center(80,"*")
final = '{}\n\n{:>80}\n{:>80}' . format(resumo, categorias, produtos)
relatorio.write(final)
relatorio.close()
