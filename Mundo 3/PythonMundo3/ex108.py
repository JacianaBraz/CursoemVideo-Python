# Adapte o códigodo DESAFIO 107, criando uma função adicional chamada moeda() que consiga mostrar os os valores como um
# valor monetário formatado.

from utilidadesCeV import moedas

reais = float(input('Digite um valor monetário: '))
por = float(input('Quanto você quer aumentar: '))

print(f'O aumento de {por} % em {moedas.moeda(reais)} é {moedas.moeda(moedas.aumentar(reais,por))}')
print(f'O dobro de {moedas.moeda(reais)} é {moedas.moeda(moedas.dobro(reais))}')
print(f'A metade de {moedas.moeda(reais)} é {moedas.moeda(moedas.metade(reais))}')


