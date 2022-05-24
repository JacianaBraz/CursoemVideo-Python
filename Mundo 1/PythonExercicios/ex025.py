# Crie um programa que leia o nome de uma pessoa e diga se ela tem 'SILVA' no nome
nome = str(input('Digite seu nome completo: '))
nomeCAP = nome.upper()
nomeS = nomeCAP.find('SILVA')
if nomeS == -1:
    print("Você não tem o sobrenome Silva")
else:
    print('Você tem o sobrenome Silva')
