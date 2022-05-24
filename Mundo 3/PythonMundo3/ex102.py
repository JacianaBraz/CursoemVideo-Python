# Crie um programa que tenha uma função fatorial(), que tenha dois parâmetros: o primeiro que indique o número
# e o segundo chamado show, que terá um valor lógico (opcional) indicando se será mostrado na tela o processo de cálculo

def fatorial(n,show=False):
    fat = 1
    while n != 0:
        if show == True:
            print(f'{n}', end=' ')
            if n > 1:
                print('x', end=' ')
            else:
                print('=')
        fat *= n
        n -= 1
    print(f'\nResultado: {fat}')

fatorial(3,True)