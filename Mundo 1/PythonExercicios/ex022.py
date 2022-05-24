# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas
# O nome com todas as minúsculas
# Quantas letras ao todo (sem considerar espaços)
# Quantas letras tem o primeiro nome

nome = input('Digite seu nome completo: ')
nome_espaço = nome.replace(" ","")
nome_separado = nome.split()

print(nome.upper())
print(nome.lower())
print(len(nome_espaço))
print(len(nome_separado[0]))