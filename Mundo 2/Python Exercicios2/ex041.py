# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria
# Até 9 anos: MIRIM
# Até 14 anos: INFANTIL
# Até 19 anos: JÚNIOR
# Até 20 anos: SÊNIOR
# Acima: MASTER

from datetime import date

anoHoje = date.today().year
anoNascimento = int(input('Qual ano você nasceu? '))
idade = anoHoje - anoNascimento

if idade <=9:
    print('Sua idade é {} anos. Você está na liga MIRIM.'.format(idade))
elif idade <= 14:
    print('Sua idade é {} anos. Você está na liga INFANTIL.'.format(idade))
elif idade <= 19:
    print('Sua idade é {} anos. Você está na liga JÚNIOR.'.format(idade))
elif idade == 20:
    print('Sua idade é {} anos. Você está na liga SÊNIOR'.format(idade))
else:
    print('Sua idade é {} anos. Você está na liga MASTER.'.format(idade))