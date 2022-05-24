# Crie um programa que simule um caixa eletrônico. No início, pergunte ao usuário qual o valor será sacado (número inteiro)
# e o programa vai informar quantas cédulas de cada valor serão entregues.
# Considere que o caixa possui cédulas de $50, $20, $10 e $2
c50 = 0
c20 = 0
c10 = 0
c2 = 0
while True:
    saque = int(input('Quanto você quer sacar? '))
    c50 = saque//50
    c20 = (saque - c50*50) // 20
    c10 = (saque - (c50*50 + c20*20)) // 10
    c2 = (saque - (c50*50 + c20*20 + c10*10))//2
    print(f'Serão entregues: {c50} cédulas de R$50,00, {c20} cédulas de R$20, {c10} cédulas de R$10,00 e {c2} cédulas '
          f'de R$2,00')
    break
