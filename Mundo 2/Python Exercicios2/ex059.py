# Crie um programa que leia dois valores e mostre um menu na tela:
# [1] somar
# [2] multiplicar
# [3] maior
# [4] novos números
# [5] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso

print('-'*50)
print('MENU'.center(50))
print('-'*50)
print('[1] Somar')
print('[2] Multiplicar')
print('[3] Maior')
print('[4] Novos Números')
print('[5] Sair do programa')
print('-'*50)

num1 = float(input('Digite um número:' ))
num2 = float(input('Digite um número: '))
escolha = 0
soma = 0
mult = 0
while escolha != 5:
    escolha = int(input('O que deseja fazer: '))
    if escolha == 1:
        soma = num1+num2
        print('A soma é:{}'. format(soma))
    elif escolha == 2:
        mult = num1*num2
        print('A multiplicação é:{}'.format(mult))
    elif escolha == 3:
        if num1 > num2:
            print('O número maior é: {}'.format(num1))
        else:
            print('O numero maior é: {}'.format(num2))
    elif escolha == 4:
        num3 = float(input('Qual o novo número? '))
        num4 = float(input('Qual o segundo novo número: '))
        num1 = num3
        num2 = num4

