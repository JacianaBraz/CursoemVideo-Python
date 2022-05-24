# Crie um módulo chamado moedas.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
# Faça também um programa que importe esse módulo e use algumas dessas funções.

from utilidadesCeV import moedas

moeda = float(input('Digite um valor monetário: '))
por = float(input('Quanto você quer aumentar: '))
aumento = moedas.aumentar(moeda, por)
diminuir = moedas.diminuir(moeda, por)
d = moedas.dobro(moeda)
m = moedas.metade(moeda)
print(f'O aumento de {por:.2f}% em R${moeda:.2f} é R${aumento:.2f}')
print(f'A redução de {por:.2f}% em R${moeda:.2f} é R${diminuir:.2f}')
print(f'O dobro de R${moeda:.2f} é R${d:.2f}')
print(f'A metade de R${moeda:.2f} é R${m:.2f}')

