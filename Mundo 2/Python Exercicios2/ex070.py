# Crie um programa que leia o nome e o preço de vários produtos.O programa deverá perguntar se o usuário vai continuar.
# No final mostre:
# Qual é o total gasto na compra
# Quantos produtos custam mais de $1000
# Qual o nome do produto mais barato
qtd = 0
total = 0
barato = 0
c = 0
produtobarato = ''
while True:
    produto = str(input('Qual o produto: '))
    preco = float(input('Qual o preço: '))
    continuar = str(input('Deseja continuar [S/N]? '))

    total += preco
    c += 1
    if c == 1 or preco < barato:
        barato = preco
        produtobarato = produto
    if preco > 1000:
        qtd += 1
    if continuar == 'N':
        break
print(f'O total gasto na compra foi de R$ {total:.2f}')
print(f'{qtd} produtos custam mais de R$1000,00')
print(f'O nome do produto mais barato é {produtobarato}')




