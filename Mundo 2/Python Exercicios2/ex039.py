# Faça um programa que leia o ano de nascimento de um jovem e informa, de acordo com sua idade:
# Se ele ainda vai se alistar ao serviço militar
# Se é a hora de se alistar
# Se já passou da hora de se alistar
# Seu programa também deve mostrar o tempo que falta ou que já passou do prazo

from datetime import date
anoHoje = date.today().year
anoNiver = int(input('Em qual ano você nasceu? '))
idade = anoHoje - anoNiver

if idade == 18:
    print('Está na hora de se alistar.')
elif idade < 18:
    alistar = 18 - idade
    print('Ainda faltam {} anos para seu alistamento.'.format(alistar))
else:
    alistar = idade - 18
    print('Já passaram {} anos dos seu alistamento.'.format(alistar))

