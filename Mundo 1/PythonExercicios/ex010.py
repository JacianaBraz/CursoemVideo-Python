# Crie um programa que leia quanto em dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
# Considere US$1=R$3,75
reais = float(input('Quantos reais você tem? '))
dolares = reais/3.75
print('Você possui R${}, pode comprar US${:.2f}.'.format(reais, dolares))
