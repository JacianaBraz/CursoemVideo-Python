# Faça um programa que leia o nome completo de uma pessoa, mostrando o primeiro e o último nome separadaments
nome = str(input('Digite seu nome completo: '))
separado = nome.split()
primeiro = separado[0]
ultimo = separado[-1]
print('O nome é {}, o primeiro nome é {} e o último {}'.format(nome, primeiro, ultimo))