nota1 = float (input('informe a nota 1: '))
nota2 = float (input('informe a nota 2: '))
nota3 = float (input('informe a nota 3: '))

media = (nota1 + nota2 + nota3) / 3
if media < 7:
    print ('Reprovado')
elif media >= 7:
    print ('Aprovado')
else: 
    print ('Aprovado com distinção')
