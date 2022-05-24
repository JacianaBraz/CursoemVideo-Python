# Faça um algoritmo que leia o preço de um produto e mostra seu novo preço com desconto de 5%
preco = float(input('Digite o preço atual: '))
preco_desconto = preco*0.95
print('O preço atual é de R${}. Aplicado o desconto de 5% ele fica em R${:.2f}'.format(preco, preco_desconto))