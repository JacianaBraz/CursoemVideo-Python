# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos
# quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
km_rodado = float(input('Quantos Km você percorreu com o carro? '))
dias = int(input('Quantos dias você alugou o carro? '))
print('Você terá que pagar R${} pelos dias alugados e R${} pelos Km rodados. Totalizando R${}'.format(60*dias, 0.15*km_rodado, (60*dias)+(0.15*km_rodado)))
