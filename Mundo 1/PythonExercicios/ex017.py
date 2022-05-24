# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo,
# calcule e mostre a hipotenusa.
import math

b = float(input('Qual o comprimento do cateto oposto: '))
c = float(input('Qual o comprimento do cateto adjacente: '))
a = math.hypot(b, c)
print('Os catetos são {} e {} e a hipotenusa é {:.2f}.'.format(b, c, a))

