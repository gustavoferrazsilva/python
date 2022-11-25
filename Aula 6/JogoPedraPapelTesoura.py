# Jogo Pedra, Papel ou Tesoura

from os import system
import random
system ('cls')
titulo = 'Pedra | Papel | Tesoura'
print(titulo.center(60,'#'))

opcao = 's'
contadorJogadas = 0
contadorJogador = 0 
contadorComputador = 0

while opcao.upper () == 'S':
    system ('cls')

    computador = random.randint(0,2) #jogador escolhe uma opção
    jogador = int(input('''Escolha uma opção para se jogar 
    [0] Pedra 
    [1] Papel 
    [2] Tesoura 
    Digite sua escolha: '''))

    if jogador > 3:
        resultado = (f' Você não escolheu uma opção válida!')
    else: 
        contadorJogadas += 1 
        peças = ('Pedra','Papel','Tesoura') # para saber a posição na tabela, considera - se a escolha do computador
        print (f'Você escolhe {peças[jogador]}')
        print (f'Computador escolheu {peças[computador]}')
        tabela = ((0,1,-1),(-1,0,1),(1,-1,0))
        jogada = tabela [computador][jogador]
        if jogada == 0:
           resultado = (f' Deu Empate')
        elif jogada == 1:
            resultado = (f' Você ganhou!')
            contadorJogador += 1 
        elif jogada == -1:
            resultado = (f' O computador ganhou!!')
            contadorComputador += 1
    print (resultado)
    opcao = input ('Jogar novamente ? (S) para sim')
system ('cls')
print ('Resumo do jogo'.center(60,'*'))
print (f'Quantidade de jogadas: {contadorJogadas}')
print (f'Você ganhou {contadorJogador} jogadas')
print (f'Computador ganhou {contadorComputador} jogadas')