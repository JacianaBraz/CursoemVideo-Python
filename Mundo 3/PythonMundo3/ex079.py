# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista
# lá dentro, ele não será adicionado. No final,serão exibidos todos os valores únicos digitados em ordem crescente.

numeros = []
while True:
    n = int(input('Digite um número: '))
    if n not in numeros:
        numeros.append(n)
    else:
        print('Tente novamente')
        n = int(input('Digite um número: '))
        numeros.append(n)
    resposta = str(input('Deseja continuar? S/N '))
    if resposta in 'Nn':
        break
print(sorted(numeros))


