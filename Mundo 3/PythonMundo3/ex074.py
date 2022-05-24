# Crie um programa que vai gerar cinco números aleatórios e colocar numa tupla.
# Depois disso mostre a listagem de números gerados e também indique o menor e o maior valor

from random import randint

a = randint(1,10)
b = randint(1,10)
c = randint(1,10)
d = randint(1,10)
e = randint(1,10)

tupla = (a, b, c, d, e)
print(tupla)
print(f'O maior valor da tupla é: {max(tupla)}')
print(f'O menor valor da tupla foi de: {min(tupla)}')