#Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se
# o usuário quer ou não continuar. No final mostre:
# Quantas pessoas tem mais de 18 anos
# Quantos homens foram cadastrados
# Quantas mulheres tem menos de 20 anos

somaidade = 0
qtdhomens = 0
qtdmulheres20 = 0

while True:
    idade = int(input('Qual a sua idade: '))
    sexo = str(input('Qual o seu sexo: '))
    continuar = str(input('Deseja continuar? [S/N]? '))
    if idade > 18:
        somaidade += 1
    if sexo == 'M':
        qtdhomens += 1
    if sexo == 'F' and idade < 20:
        qtdmulheres20 +=1
    if continuar == 'N':
        break
print(f'{somaidade} tem mais de 18 anos')
print(f'{qtdhomens} homens foram cadastrados')
print(f'{qtdmulheres20} mulheres tem menos de 20 anos')
