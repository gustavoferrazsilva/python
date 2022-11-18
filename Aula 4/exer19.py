# Programa que verifica se uma letra digitada é vogal ou consoante

vogais = ['a','e','i','o','u']
letra = input ('Digite uma letra: ')

if letra.lower () in vogais: #in significa que pertentece a lista
    print ('Você digitou uma vogal')
else:
    print ('VOcê digitou uma consoante')