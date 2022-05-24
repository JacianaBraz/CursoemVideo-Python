# Crie um programa que tem uma função chamada voto() que vai receber como parâmetro o ano de um nasciemento de uma
# pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPICIONAL ou OBRIGATÓRIO nas eleições.
import datetime


def voto(ano):
    idade = datetime.date.today().year - ano
    if idade < 16:
        print(f'Com {idade} anos, o voto é NEGADO')
    elif idade <= 17:
        print(f'Com {idade} anos, o voto é OPCIONAL')
    else:
        print(f'Com {idade} anos, o voto é OBRIGATÓRIO')


#Programa Principal
nascimento = int(input('Digite o ano do seu nascimento: '))
voto(nascimento)

