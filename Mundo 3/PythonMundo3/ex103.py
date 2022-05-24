# Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opicionais: o nome do jogador e
# quantos gols ele marcou.
# O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.

def ficha(nome=0, gols=0):
    nome = jogador
    gols = ngols
    if jogador == '':
        nome = '<desconhecido>'
    if ngols.isnumeric():
        gols = int(ngols)
    else:
        gols = 0
    print(f'O jogador {nome} fez {gols} gols')




#Programa Principal
jogador = str(input('Digite o nome do jogador: '))
ngols = str(input('Digite a quantidade de gols: '))
ficha(jogador,ngols)