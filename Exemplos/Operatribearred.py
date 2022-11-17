#Operadores de atribuição

#Operador de atribuição ' = '
nome = "Maria"
idade = 30
# = atribui um dado/ valor e uma variável
# o símbolo "=" usado uma vez é um operador de atribuição
# quando usado duas vezes "==" é um operador de igualdade
print(nome)
print(idade)

#Atribuição aditiva
valor = 4
valor += 3
'''
mesmo que:
valor = valor + 3
'''
print (valor)

#Atribuição subtrativa
valor = 4
valor -= 3
'''
mesmo que:
valor = valor - 3
'''
print (valor)

#Atribuição multiplicativa
valor = 4
valor *= 3
'''
mesmo que:
valor = valor * 3
'''
print (valor)

#Atribuição divisão
valor = 12
valor /= 2
'''
mesmo que:
valor = valor / 2
'''
print (valor)

#Atribuição módulo / resto de divisão
valor = 12
valor %= 2
'''
mesmo que:
valor = valor % 2
'''
print (valor)

#Atribuição divisão inteira
valor = 512
valor //= 256
'''
mesmo que:
valor = valor // 256
'''
print (valor)

#Atribuição exponenciativa
valor = 4
valor **= 3
'''
mesmo que:
valor = valor ** 256
ou 
valor = 4 * 4 * 4
'''
print (valor)

#Arredondando valores de casas decimais
equacao = ((50 + 25) * 7.2) / 3.8
print(f' o resultado bruto da equação é {equacao}')
print(f' o resultado arredondado da equação é {equacao:.2f}')
print(f' o resultado arredondado da equação é {round(equacao,2)}')


