# Aprimore o desafio 93 para que ele funcione com vários jogadores,
# incluindo um sistema de visualização de detalhes de aproveitamento de cada jogador.

aproveitamento = {}
partidas = []
while True:
    aproveitamento['jogador'] = str(input('Nome do jogador: '))
    aproveitamento['n de partidas'] = int(input('Quantas partidas foram jogadas: '))
    for c in range(0,aproveitamento['n de partidas']):
        partidas.append(int(input('Quantos gols foram feitos? ')))
    aproveitamento['gols'] = partidas[:]
    aproveitamento['total de gols'] = sum(partidas)
    print(f'O {aproveitamento["jogador"]} jogou {aproveitamento["n de partidas"]}')
    for i, v in enumerate(aproveitamento['gols']):
        print(f'Na partida {i + 1} ele fez {v} gols')

    while True:
        p = str(input('Deseja continuar? [s/n] '))
        if p in 'SsNn':
             break
        else:
            print('ERRO! Digite somente S ou N')
    if p in 'Nn':
            break



