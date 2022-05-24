# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# Apenas os cinco primeiros colocados
# Os quatro últimos colocados
# Uma lista com os times em ordem alfabética
# De qual posição está o time Chapecoense

times = ('Corinthians', 'Santos', 'América-MG', 'Bragantino', 'São Paulo', 'Atlético-MG', 'Botafogo', 'Internacional',
         'Coritiba', 'Avaí', 'Cuiabá', 'Athletico-PR', 'Palmeiras', 'Flamengo', 'Fluminense', 'Goiás', 'Ceará-SC',
         'Juventude', 'Atlético-GO', 'Fortaleza')
print(f'Os cinco primeiros colocados são:{times[:5]}')
print(f'Os quatro últimos colocados são {times[16:]}')
print(sorted(times))
print(f'O Coritiba está na {times.index("Coritiba")+1} posição')