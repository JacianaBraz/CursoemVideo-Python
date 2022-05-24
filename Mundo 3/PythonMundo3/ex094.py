# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e
# todos numa lista. No final mostre:
# Quantas pessoas foram cadastradas
# A média da idade do grupo
# Uma lista com todas as mulheres
# Uma lista com todas as idades acima da média

dados = []
pessoas = {}
cont = 0
media = 0
idade = 0
mulheres = []
acima =[]

while True:
    pessoas['nome'] = str(input('Digite seu nome: '))

    while True:
        pessoas['sexo'] = str(input('Digite seu sexo [M/F]: '))
        if pessoas['sexo'] in 'MmFf':
            break
        else:
            print('ERRO! Digite apenas M ou F')

    pessoas['idade'] = int(input('Digite sua idade: '))
    idade += pessoas['idade']
    dados.append(pessoas.copy())
    while True:
        p = str(input('Deseja continuar[S/N]: '))
        if p in 'SsNn':
            cont += 1
            media = idade/cont
            break
        else:
            print('ERRO! Digite apenas S ou N')
    if p in 'nN':
        break

print(f'A lista de pessoas cadastradas foi de: {dados}')
print(f'A quantidade de pessoas cadastradas foi: {cont}')
print(f'A média das idades foi: {media:.2f} anos')

print(f'As mulheres são:',end=' ')
for item in dados:
    if item['sexo'] in 'Ff':
        print(f'{item["nome"]},',end=' ')

print('\nAs idades maiores que a média foram:', end=' ')
for item in dados:
    if item['idade'] > media:
        print(f'{item["nome"]},', end=' ')




