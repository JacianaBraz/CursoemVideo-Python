# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento
salario = float(input('Qual seu salário atual? '))
aumento = salario*1.15
print('Seu salário era R${}. Parabéns pelo aumento! Seu novo salário é R${:.2f}'.format(salario, aumento))
