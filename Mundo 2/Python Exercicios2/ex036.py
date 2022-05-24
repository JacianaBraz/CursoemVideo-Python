# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# O programa vai perguntar o valor da casa, do salário e quantos anos ele vai levar para pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exeder 30% do salário ou então o empréstimo será negado
valorCasa = float(input('Qual o valor da casa? '))
valorSalario = float(input('Qual é o seu salário? '))
anos = int(input('Em quantos anos você pretende pagar? '))
mes = anos*12
parcela = valorCasa/mes
if parcela > 0.3*valorSalario:
    print('O valor da parcela é R$ {:.2f}. Seu salário é R${:.2f}. Seu empréstimo foi NEGADO.'. format(parcela,valorSalario))
else:
    print('O valor da parcela é R${:.2f}. Seu salário é R${:.2f}. Seu empréstimo foi APROVADO'.format(parcela,valorSalario))