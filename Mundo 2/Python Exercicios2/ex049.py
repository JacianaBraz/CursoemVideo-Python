# Refação o EXERCÍCIO 9, mostrando a tabuada de um número que o usúário escolher, só que agora com o laço for.

cont = 0
mult = 0
n = int(input('Digite um número:'))
for cont in range(0, 10):
    cont+=1
    mult = n*cont
    print('{} x {} = {}'.format(n, cont, mult))