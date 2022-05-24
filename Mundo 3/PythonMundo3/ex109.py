# Modifique as funções que foram criadas no desafio 107, para que elas aceitem um parâmetro a mais informando se o valor
# retornado por elas pode ou não formatado pela função moeda(), desenvolvida no desafio 108

from utilidadesCeV import moedas

reais = float(input('Digite um valor monetário: '))
por = float(input('Quanto você quer aumentar: '))
aumento = moedas.aumentar(reais, por, True)
diminuir = moedas.diminuir(reais, por, True)
d = moedas.dobro(reais, True)
m = moedas.metade(reais, True)
rs = moedas.moeda(reais)
print(f'O aumento de {por}% em {rs} é {moedas.aumentar(reais, por, True)}')
print(f'A redução de {por}% em {rs} é {diminuir}')
print(f'O dobro de {rs} é {d}')
print(f'A metade de {rs} é {m}')