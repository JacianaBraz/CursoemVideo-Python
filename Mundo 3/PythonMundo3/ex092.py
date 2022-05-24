# Crie um programa que leia nome, ano de nascimento, carteira de trabalho e cadastre-os (com idade) em um dicionário
# Se por acaso a CTPS for diferente de 0, o dicionário também receberá o ano de contratação e o salário.
# Calcule a acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

import datetime

cadastro = {}

cadastro['nome'] = str(input('Nome: '))
cadastro['ano'] = int(input('Ano de nascimento: '))
cadastro['ctps'] = int(input('Digite o número da sua carteira de trabalho: '))
niver = datetime.date.today().year - cadastro['ano']
cadastro['idade'] = niver
if cadastro['ctps'] != 0:
    cadastro['contratação'] = int(input('Qual seu ano de contratação: '))
    cadastro['salário'] = float(input('Qual o salário: '))
    aposentar = 65 - niver
    cadastro['aposentadoria'] = aposentar
print(cadastro)



