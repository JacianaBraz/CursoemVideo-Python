# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os
# valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar
# a digitar mais valores

maior = 0
menor = 0
soma = 0
media = 0
c = 0
num = 0
u = 'S'

while u in 'Ss':
    num = int(input('Digite um número: '))
    if c == 0:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
    soma+=num
    c+=1
    u = str(input('Deseja digitar algum outro número [S/N]: '))
    if u in 'Nn':
        media = soma/c
        print('O maior número foi {}'.format(maior))
        print('O menor número foi {}'.format(menor))
        print('A soma dos números foi {}'.format(soma))
        print('A média dos números foi {}'.format(media))

