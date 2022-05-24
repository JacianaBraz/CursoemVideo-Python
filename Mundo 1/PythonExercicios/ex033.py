# Faça um programa que leia três números e mostre qual é maior e qual é menor.
n1 = float(input('Digite um número: '))
n2 = float(input('Digite um número: '))
n3 = float(input('Digite um número: '))
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
print('O menor valor é: {}'.format(menor))
maior = n3
if n1 > n3 and n1 > n2:
    maior = n1
if n2 > n3 and n2 > n1:
    maior = n2
print('O maior valor é {}'.format(maior))
