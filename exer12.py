from os import system
import random
system('cls')
#print(random.randint(0,100))

num = random.randint(0,100)

#o numero escolhido é par ou impar?
resto = num % 2
if resto == 0:
    print('O numero escolhido é par')
else:
    print('O numero escolhido é impar')
#o numero escolhido é maior que 50 ou menor
#  (mais perto do 100 ou do 0)

if num > 50:
    print('O numero escolhido esta mais perto do 100')
else:
    print('O numero escolhido esta mais perto do 0')

#o numero escolhido é primo