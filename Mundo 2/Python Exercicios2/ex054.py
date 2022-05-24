# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date
anoHoje = date.today().year

s=0
for c in range(1,8):
    anoN = int(input('Qual ano você nasceu? '))
    idade = anoHoje - anoN
    if idade >= 21:
        s += 1
print('{} pessoas atingiram a maioridade e {} não atingiram'.format(s,c-s))
