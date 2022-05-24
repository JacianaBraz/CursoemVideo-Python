# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
def maior(* num):
    m = 0
    c = 0
    print('Analisando os números:')
    for numero in num:
        print(f' {numero}', end=' ')
        if c == 0:
            m = numero
        else:
            if m < numero:
                m = numero
    print(f'\nO maior número é: {m}')
    c += 1


maior(1,10,0,20)

