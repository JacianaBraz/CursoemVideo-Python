# Crie um ´programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida
# No final tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

aproveitamento = {}
partidas = []

aproveitamento['jogador'] = str(input('Nome do jogador: '))
aproveitamento['n de partidas'] = int(input('Quantas partidas foram jogadas: '))
for c in range(0,aproveitamento['n de partidas']):
    partidas.append(int(input('Quantos gols foram feitos? ')))
aproveitamento['gols'] = partidas[:]
aproveitamento['total de gols'] = sum(partidas)
print(aproveitamento)
