# Faça um programa que leia o nome e a média de um aluno guardando também a situação em um dicionário.
# No final, mostre o conteudo da estrutura da tela.

dados = {}
media = 0

dados['nome'] = str(input('Nome: '))
dados['nota1'] = float(input('Digite a primeira nota: '))
dados['nota2'] = float(input('Digite a segunda nota: '))
dados['nota3'] = float(input('Digite a terceira nota: '))
media = (dados['nota1'] + dados['nota2'] +dados['nota3'])/3
dados['media'] = media
if media >= 6:
    dados['situação'] = 'APROVADO'
else:
    dados['situação'] = 'REPROVADO'

print(dados)




