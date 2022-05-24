#Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor solicitado pelo usuário.
#O programa será interrompido quando o número for negativo.

c = 0
while True:
    tabuada = int(input('Digite um número: '))
    if tabuada < 0:
        break
    for c in range(0,10):
        c += 1
        print(f'{c} x {tabuada} = {c*tabuada}')


