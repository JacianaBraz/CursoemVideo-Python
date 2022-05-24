# Faça um programa que leia o nome e peso de várias pessoas, guardando tudo em uma lista. No final mostre:
# Quantas pessoas foram cadastradas
# Uma lista de pessoas mais pesadas
# Uma listagem com as pessoas mais leves

pessoas = []
dados = []
c = 0
pesada = 0
leve = 0

while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    pessoas.append(dados[:])
    dados.clear()
    continuar = str(input('Deseja continuar? S/N '))

    if c == 0:
        pesada = pessoas[0][1]
        leve = pessoas[0][1]
    for i in range(0, c+1):
        if pesada < pessoas[i][1]:
            pesada = pessoas[i][1]
        elif leve > pessoas[i][1]:
            leve = pessoas[i][1]
    c += 1
    if continuar in 'Nn':
        break

for p in pessoas:
    if p[1] == pesada:
        print(f'O nome da pessoa mais pesada é {p[0]} e o peso é {pesada} Kg')
    elif p[1] == leve:
        print(f'O nome da pessoa mais leve é {p[0]} e o seu peso é {leve} Kg')
print(f'Foram cadastradas {c} pessoas')
