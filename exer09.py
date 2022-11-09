""" vamos trabalhar com dados de texto, usando varios metodos para verificar e modificar o valor de uma variavel da clss str """

from os import system
system('cls')
nomeCompleto = input('Informe o seu nome completo: ')
print(nomeCompleto)

#após o from, colocar o nome da biblioteca e após o import, é o local de onde será importado a biblioteca

#tamanho da minha string | total de caracteres 
print('1. total de caracteres:', len (nomeCompleto))

#acessando um caracter a partir da posicao
print('2. o caracter da posicao 2 é: ', nomeCompleto[2])

#transformando string em maiuscula | minuscula
print ('3. texto em maiusculo', nomeCompleto.upper())
print ('4. texto em minusculo', nomeCompleto.lower())
print ('5. Primeira letra maiuscula', nomeCompleto.capitalize())

#procurar a posicao de um determinado caractere
print ('6. posicao do caractere espaco', nomeCompleto.find(' '))

#fatiar uma string ate uma determinada posicao

espaco = nomeCompleto. find(' ')
print('7. Somente o primeiro nome:', nomeCompleto [0:espaco])

#substituir um caractere por outro
print('8. nome sem espaco:', nomeCompleto.replace(' ', ''))

#verificar somente letras ou letras e numeros
print ('9. Tem somente letras? ',nomeCompleto.replace(' ','').isalpha())
print ('10. É alfanumerico? ',nomeCompleto.replace(' ','').isalnum())

#quebrar o texto a cada espaco em partes especificas retornando array
print ('11. quebrar o texto a cada espaco em branco: ', nomeCompleto.split (" "))

#centralizar o texto usando * para completar as laterais
print('12. centralizar o texto entre * ')
print (nomeCompleto.center(80,"*"))