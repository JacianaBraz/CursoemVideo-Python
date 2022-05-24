# Faça um programa que leia o peso de cinco pessoas. No final mostre o maior e o menor peso lidos

pesop = 0
pesom = 0
for c in range(1, 6):
    peso = float(input('Qual o seu peso? '))
    if c == 1:
        pesop = peso
        pesom = peso
    else:
        if peso > pesom:
            pesom = peso
        elif peso < pesop:
            pesop = peso
print('O menor peso é: {:.2f}Kg'.format(pesop))
print('O maior peso é: {:.2f} Kg'.format(pesom))



