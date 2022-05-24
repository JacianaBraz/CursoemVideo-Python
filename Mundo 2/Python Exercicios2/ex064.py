#Crie um programa que leia vários números inteiros pelo teclado. O programa vai parar quando o usuário digitar 999,
# que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles
# (desconsiderando o 999)

num = 0
c = 0
soma = 0
while num != 999:
    num = int(input('Digite um número: '))
    c += 1
    soma += num
print('A quantidade de números digitados foi de {} e a soma foi {}'.format(c-1, soma-999))
