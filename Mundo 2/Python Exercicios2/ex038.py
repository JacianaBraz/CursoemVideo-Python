# Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem
# O primeiro valor é maior
# O segundo valor é maior
# Os dois valores são iguais
n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))

if n1 > n2:
    print('O primeiro valor é maior.')
elif n2 > n1:
    print('O segundo valor é maior')
else:
    print('Os valores são iguais')
