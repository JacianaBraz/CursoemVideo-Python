# Faça um programa que leia o sexo de uma pessoa, mas só aceita os valores 'M' ou 'F'. Caso esteja errado, peça a
# digitação novamente até ter um valor correto.

sexo = str(input('Qual o seu sexo [M/F] ')).strip()

while sexo not in 'MmFm' :
    print('Digite um sexo válido')
    sexo = str(input('Qual o seu sexo [M/F] ')).strip()
print('Sexo válido')
