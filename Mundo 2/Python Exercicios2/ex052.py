# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

num = int(input('Digite um número: '))
divisiveis = 0

for c in range(1, num+1):
    if num % c == 0:
        divisiveis += 1
if divisiveis == 2:
    print('Esse número é primo')
else:
    print('Esse número não é primo')