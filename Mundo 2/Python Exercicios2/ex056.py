# Desenvolva um programa que leia o nome, o sexo e a idade de 4 pessoas. No final mostre:
# A média de idade do grupo
# Qual o nome do homem mais velho
# Quantas mulheres tem menos de 20 anos

soma = 0
media = 0
velho = 0
nomevelho = ''
nova = 0
for n in range(1,5):
    nome = str(input('Qual é o nome? '))
    sexo = str(input('Qual o sexo (F ou M) '))
    idade = int(input('Qual a idade? '))
    soma += idade
    if n == 1 and sexo in 'Mm': #ao colocar o in ele aceita tanto o maiúsculo quanto o minúsculo
        velho = idade
        nomevelho = nome
    elif sexo in 'Mm'and idade > velho:
        velho = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        nova += 1
media = soma /4
print('A média das idades foi: {} anos'.format(media))
print('O nome do homem mais velho é {}'.format(nomevelho))
print('Existem {} mulheres com menos de 20 anos'.format(nova))
