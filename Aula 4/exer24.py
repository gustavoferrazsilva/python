#Jogo da Adivinhação

from os import system
import random
system('cls')
titulo = 'JOGO DA ADIVINHAÇÃO'
print(titulo.center(80, '*'))

num = random.randint (1,10)

tentativa = int(input('Adivinhe o número de 1 a 10: (0 - para sair'))
while tentativa > 0:
  if tentativa > num:
    print('é menor, tente novamente')
  elif tentativa < num:
    print('é maior, tente novamente')
  else:
    print(f' UHULLL VOCÊ ACERTOU - {num}')
  tentativa = int(input('Adivinhe o número de 1 a 10'))