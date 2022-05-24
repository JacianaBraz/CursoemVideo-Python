# Faça um programa que leia um ângulo qualquer e mostre na tela o valor de seno, cosseno e tangente desse ângulo.
import math

angulo = float(input('Qual o ângulo: '))
graus = math.radians(angulo)
sen = math.sin(graus)
cos = math.cos(graus)
tan = math.tan(graus)
print('O grau que você deseja é: {}, seu seno é: {:.3f}, seu cosseno é: {:.3f} e sua tangente é: {:.3f}'.format(angulo, sen, cos, tan))
