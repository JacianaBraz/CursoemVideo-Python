# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses reusltados em um
# dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número do dado.

from random import randint

jogo = {}
dados = []


for j in range(0,4):
    jogo['jogador'] = str(input('Nome jogador: '))
    jogo['valor'] = randint(1, 6)
    dados.append(jogo.copy())
print(dados)
