# Estruturas condicionais

# if - estrutura condicional simples

nome = input ('Digite o seu nome:')
if nome == 'Fernando' :
    print ('Bem vindo de volta Fernando')

print (f'Você é novo (a) aqui,olá {nome}!!!')

# se a condição for atingida, o bloco indentaoo {bloco verdade} é executado
# caso contrário, é simplesmente ignorado
# estruturas de condição podem ser chamadas também, de estruturas de controle de fluxo.

# if, else - estrutura condicional com dois possíveis desfechos

num = 51
if num < 50 :
    print ('Menor que 50')
else:
    print ('Maior que 50')
# se o valor de num for menor que 50 exiba na tela 'Menor que 50'
# caso contrário (senão), exiba na tela 'Maior que 50'.

# Estrutura condicional composta

nome = input ('Digite seu nome:')
if nome == 'Fernando' :
    print ('Bem vindo de volta Fernando')
if nome == 'Maria' :
    print ('Bem vinda de volta Maria !!!')
else:
    print (f' Você é novo (a) aqui,olá {nome}!!!')
# Sendo a primeira proposição verdadeira, a execução desse bloco indentado é executado 
# e mesmo assim será realizado o teste na segunda condição

nome = input ('Digite seu nome:')
if nome == 'Fernando' :
    print ('Bem vindo de volta Fernando')
if nome == 'Carlos' :
    print ('Bem vinda de volta Carlos!')
    nome = input ('Digite seu nome:')
if nome == 'Maria' :
    print ('Bem vindo de volta Maria')
if nome == 'Tânia' :
    print ('Bem vindo de volta TâniaA')
else: 
    print ('Você não é Fernando nem Carlos nem Maria nem Tânia...')
    print (f' Você é novo (a) aqui,olá {nome}!!!')
# percebam que ele executou o print no caso da proposição verdadeira
# e executou o bloco do else que faz referência a condição de Tânia

# if, elif e else - estrutura condicionais aninhadas

nome = input ('Digite seu nome:')
if nome == 'Fernando' :
    print ('Bem vindo de volta Fernando')
elif nome == 'Carlos' :
    print ('Bem vinda de volta Carlos!')
    nome = input ('Digite seu nome:')
elif nome == 'Maria' :
    print ('Bem vindo de volta Maria')
elif nome == 'Tânia' :
    print ('Bem vindo de volta TâniaA')
else: 
    print ('Você não é Fernando nem Carlos nem Maria nem Tânia...')
    print (f' Você é novo (a) aqui,olá {nome}!!!')
# observar o que aconteça com a troca de if por elif
# usando elif a partir da segunda proposição, 
# garante que uma proposição sendo verdadeira, já encerra o processo naquele ponto

num = float (input('Digite um número: '))
if num < 50 :
    print ('Menor que 50')
elif num == 50:
    print ('Igual a 50')
elif num >= 51 and num < 100:
    print ('Maior que 50')
else:
    print('Número inválido')

# Duas ou mais condições sendo verdadeiras

nome1 = 'Fernando'
nome2 = 'Maria'

if nome1 == 'Fernando':
    print('Bem vindo Fernando')
if nome2 == 'Maria' :
    print ('Bem vinda Maria')
else: 
    print('Erro: desconhecido')
# usando if mais de uma proposição pode ser considerada verdade
# e aí nesse caso, retorna bem vindo para os dois nomes

nome1 = 'Fernando'
nome2 = 'Maria'

if nome1 == 'Fernando':
    print('Bem vindo Fernando')
elif nome2 == 'Maria' :
    print ('Bem vinda Maria')
else: 
    print('Erro: desconhecido')
# usando elif o retorno seria apenas para a proposição verdadeira
# e sendo uma verdade já encerra o processo.