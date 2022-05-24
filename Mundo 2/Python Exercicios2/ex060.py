# Faça um programa que leia um número e mostre seu fatorial

num = int(input('Digite um número: '))
c = 1
fat = 1
while c <= num:
    fat = c * fat
    c += 1
    print(fat, end=" ")