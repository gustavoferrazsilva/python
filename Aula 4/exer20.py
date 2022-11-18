# Faça um programa que receba três numeros e mostre - os em ordem decrescente

from os import system
import random
system ('cls')

titulo = 'EXIBIR NUMEROS EM ORDEM DECRESCENTE'
print (titulo.center(60,'*'))

num1 = random. randint (0,1000) #alt + shift + seta pra baixo: copiar 
num2 = random. randint (0,1000)
num3 = random.randint (0,1000)

if num1 > num2 and num1 > num3:
    menor = num1
elif num2 > num3:
    maior = num2
else:
    maior = num3

if num1 < num2 and num1 < num3:
    menor = num1
elif num2 < num3:
    menor = num2
else:
    menor = num3

if (num1 < num3 and num1 > num2) or (num1 > num3 and num1 < num3):
    meio = num1
elif (num2 < num1 and num2 > num3) or (num2 < num3 and num2 > num3):
    meio = num2
else:
    meio = num3
print(f'{maior}\n{meio}\n{menor}')
