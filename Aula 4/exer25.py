# Número Primo

from os import system
system('cls')
titulo = 'Verificador de número primo'
print(titulo.center(80, '*'))

while True:    
    num = int(input('Digite um número inteiro: '))
    if num >= 2:
        break
    else:
        print(f'Informe número maior ou igual a 2')

resultado = 'O número é primo'
i = 2
while i < num:
    resto = num % i 
    if resto == 0:
        resultado = 'O número não é primo'
        break
    i += 1
print (resultado)