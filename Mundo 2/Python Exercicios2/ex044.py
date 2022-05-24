# Elabore um programa que calcule o valor a ser pago por um produto, considerando seu preço normal e condição de pagamento
# Á vista dinheiro/cheque: 10% de desconto
# Á vista cartão: 5% de desconto
# Em até 2x no cartão: preço normal
# 3x ou mais no cartão: 20% de juros

preco = float(input('Qual o preço do produto? '))
pagamento = str(input('Como deseja pagar: '))

if pagamento == 'dinheiro' or pagamento == 'cheque':
    valor = preco*0.9
    print('Você pagará R${:.2f} pela compra'.format(valor))
elif pagamento == 'cartao':
    tipo = str(input('a vista ou parcelado? '))
    if tipo == 'a vista':
        valor = preco*0.95
        print('Você pagará R${:.2f} pela compra'.format(valor))
    else:
        vezes = int(input('Quantas vezes você quer parcelar? '))
        if vezes == 2:
            valor = preco
            print('Você pagará R${:.2f} pela compra. E cada parcela será de: R$ {}'.format(valor, valor/2))
        else:
            valor = preco*1.2
            print('Você pagará R${:.2f} pela compra. E cada parcela será de: R${:.2f}'.format(valor, valor/vezes))
