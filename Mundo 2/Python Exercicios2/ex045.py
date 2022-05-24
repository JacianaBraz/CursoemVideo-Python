# Crie um programa que faça o computador jogar Jokenpô com você.
from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
comp = randint(0, 2)
print('Suas opções: '
      '[0] Pedra' 
      '[1] Papel'
      '[2] Tesoura')
jogador = int(input('Qual você deseja jogar? '))
print('O computador escolheu {}'.format(itens[comp]))
print("O jogador jogou {}".format(itens[jogador]))
if jogador == 0:
    if comp == 0:
        print('EMPATE')
    elif comp == 1:
        print('PERDEU')
    elif comp == 2:
        print('GANHOU')
elif jogador == 1:
    if comp == 0:
        print('GANHOU')
    elif comp == 1:
        print('EMPATE')
    elif comp == 2:
        print('PERDEU')
elif jogador == 2:
    if comp == 0:
        print('PERDEU')
    elif comp == 1:
        print('GANHOU')
    elif comp == 2:
        print('EMPATE')

