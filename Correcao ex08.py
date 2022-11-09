#faca um programa que pergunte quanto voce ganha por hora e o numero de horas trabalhadas no mes. Calcule 
# e mostre o total do seu salário do mes referido

horas = int(input('Informe total de horas:'))
valorHora = float (input('Informe o valor da hora:'))
salario = valorHora * horas
print (' Salario do mes R$: {:.2f}' .format(salario))