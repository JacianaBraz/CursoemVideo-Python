# Crie um programa que leia vários números inteiros pelo teclado. o programa só vai parar quando o usuário digitar 999,
# que é a condição de parada. No final mostre quantos números foram digitados e qual foi a soma entre eles
c = 0
soma = 0
while True:
    usuario = int(input('Digite um número: '))
    if usuario == 999:
        break
    soma += usuario
    c += 1
print(f'Foram digitados {c} e a soma entre eles é {soma}')

