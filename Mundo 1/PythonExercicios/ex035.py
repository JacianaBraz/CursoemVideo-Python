# Desenvolva um programa que leia o comprimento de 3 retas e diga ao usuário se elas podem ou não formar um triângulo
reta1 = float(input('Digite o comprimento de reta: '))
reta2 = float(input('Digite o comprimento da segunda reta: '))
reta3 = float(input('Digite o comprimento da terceira reta: '))
if reta1+reta2 > reta3 and reta1 +reta3 > reta2 and reta2+reta3 > reta1:
    print('Pode formar triângulo.')
else:
    print('Não pode formar triângulo.')