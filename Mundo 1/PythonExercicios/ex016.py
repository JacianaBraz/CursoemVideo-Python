# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
import math

r = float(input('Digite um número: '))
i = math.trunc(r)
print('O número escolhido foi {} e sua parte inteira é {}'.format(r, i))
