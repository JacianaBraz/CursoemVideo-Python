#Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador PERDER, mostrando
# o total de vitórias consecutivas que ele conquistou no final do jogo

from random import randint
soma = 0
c = 0
while True:
    computador = randint(0, 10)
    usuario = int(input('Digite um número: '))
    escolha = str(input('Escolha PAR ou IMPAR: '))
    soma = computador + usuario
    if soma % 2 == 0 and escolha == 'PAR':
        print(computador)
        print('Ganhou!')
        c += 1
    elif soma % 2 == 1 and escolha == 'PAR':
        print(computador)
        print('Perdeu!')
        break
    elif soma % 2 == 1 and escolha == 'IMPAR':
        print(computador)
        print('GANHOU!')
        c += 1
    elif soma % 2 == 0 and escolha == 'IMPAR':
        print(computador)
        print('Perdeu!')
        break
print(f'Voce venceu {c} vezes')




