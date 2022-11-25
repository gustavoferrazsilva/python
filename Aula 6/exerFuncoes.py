# Exercício funções

from os import system

def soma (v1, v2):
    try:
        return float(v1) + float(v2)
    except:
        return False 
    
def subtraca (v1, v2):
    return v1 - v2

def multiplicacao (v1,v2):
    return v1*v2

def divisao (v1,v2):
    """if v1 == 0 or v2 == 0:
    return False """
    try:
        return float (v1)/float (v2)
    except ZeroDivisionError as error:
        print (error)
        return False
    except:
        print('erro conversao')
        return False
        
opcao = 1
while opcao:
    v1 = float (input ('Informe o valor 1: '))
    v2 = float (input ('Informe o valor 2: '))
    operador = int (input(''' 
    1. Somar
    2. Subtrair
    3. Multiplicar
    4. Dividir
    Opção:
    '''))
    if operador == 1:
        print (f'Soma: {soma(v1,v2)}')
    if operador == 2:
        print (f'Subtrair: {subtraca(v1,v2)}')
    if operador == 3:
        print (f'Multiplicar: {multiplicacao(v1,v2)}')
    if operador == 4:
        print (f'Dividir: {divisao(v1,v2)}')
    
    opcao = input (f'\nAperte 0 para sair ou Enter para continuar: ')
    if opcao == "0":
        opcao = int(opcao) 
    else:
        opcao=1
