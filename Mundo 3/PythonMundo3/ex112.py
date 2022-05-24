# Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado. Crie uma função chamada
# leiaDinheiro() que seja capaz de funcionar como função input(), mas com ums validação de dados para aceitar apenas
# valores que sejam monetários.

from utilidadesCeV import dado
from utilidadesCeV import moedas

p = dado.leiaDinheiro('Digite o preço: ')
max= float(input('Aumento: '))
min = float(input('Desconto: '))
moedas.resumo(p, max, min)