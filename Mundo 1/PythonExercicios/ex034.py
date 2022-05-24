# Escreva um programa que pergunte o salário de um funcionário e calcula o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%
# Para inferiores ou iguais, o aumento é de 15%
salario= float(input('Qual seu salário: '))
if salario <= 1250:
    aumento = salario*1.15
    print('Seu salário era R${}, agora é R${:.2f}'.format(salario, aumento))
else:
    aumento = salario*1.10
    print('Seu salário era R${}, agora é R${:.2f}'.format(salario, aumento))