# Adicione ao módulo moedas.py criado nos desafios anteriores, uma função chamada resumo(), que mostre na tela algumas
# informações geradas pelas funções que já temos no módulo criado até aqui.

from utilidadesCeV import moedas

moeda = float(input('Digite um valor monetário: '))
pormax = float(input('Quantos porcento você quer aumentar? '))
pormin = float(input('Quantos porcento você deseja diminuir? '))

moedas.resumo(moeda, pormax, pormin)


