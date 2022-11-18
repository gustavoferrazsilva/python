from os import system
system ('cls')
titulo = 'CONVERSOR DE MEDIDAS'
print(titulo.center(80,'*'))
medida = float (input('informe a medida em centímetros: '))

print('\nEscolha para que unidade deseja converter:')
print ('1 - polegada\n2 - Pé \n3- jarda')

menu = input ('Opção: ')

valorPolegada = 2.54
valorPes = 30.48
valorJarda = 91.44

if menu == '1':
    polegada = medida / valorPolegada
    resultado =str (f'{medida:.4f} centimetros correspondem a {polegada: .4f}: polegadas')
elif menu == '2':
    pes = medida / valorPes
    resultado =str (f'{medida:.4f} centimetros correspondem a {pes: .4f}: pes')
elif menu == '3':
    jarda = medida / valorJarda
    resultado =str (f'{medida:.4f} centimetros correspondem a {jarda: .4f}: jarda')
else:
    resultado = str(f'Voce nao escolheu uma das opções válidas')
print (resultado)