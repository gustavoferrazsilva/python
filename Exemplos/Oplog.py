# Operadores lógicos

# Operador de igualdade
print (5 == 6)
# 5 é igual a 6 ?
print (12 == 12)
# 12 é igual a 12 ?

# Operador de diferença
print (7 != 3)
# 7 é diferente de 3 ?

# Operadores lógicos compostos

# Operador or
# Apenas uma proposição precisa ser verdadeira para o retorno ser True
print (7 != 3 or 2 > 3)

# Operador and
# Todas as condições precisam ser verdadeiras para o retorno ser True
print (7 != 3 and 3 > 2)
print (7 != 3 and 2 > 3)

# Operador is
num1 = 4
num2 = 9 
num3 = 9
print (num1 == num2)
# o valor de num1 é igual ao valor de num2 ?
print (num1 is num2)
# o valor de num1 é a mesma coisa que o valor de num2 ?
print (num2 is 9)
# o valor de num2 é 9

# Operador in
lista = [1,2,3,'Ana','Maria']
print (2 in lista)
# verifica se um elemento é membro daquele tipo de dado
# 2 está dentro da lista (dentro do conteúdo da lista)

# Operador not in
lista = [1,2,3,'Ana','Maria']
print ('Maria' not in lista)
# Maria não está em lista ?
# 2 está dentro da lista (dentro do conteúdo da lista)

# Operadores relacionais

# maior que 
idade = 3
print (idade > 4)
# 3 é maior que 4 ?

# igual ou maior que 
num = 7
print (num >= 6)
#7 é maior ou igual a 7 ?
#7 é maior ou igual a 6 ?

# menor igual
y = 7
x = 5
print (x <= y)
#o valor de x é menor ou igual ao valor de y ?

# condições lógicas compostas
x = 2
y = 7
print(x is 2 and y != x)
# o valor de x é 2 ? E o valor de y é diferente de x ?

# Operadores em estruturas condicionais

idade = 21
if idade > 18:
    print ('idade adulta')
# se o valor de idade for maior que 18: faça | execute o bloco True

num1 = 2
num2 = 1
if num1 > num2:
    print(f'{num1} é maior que {num2}')
