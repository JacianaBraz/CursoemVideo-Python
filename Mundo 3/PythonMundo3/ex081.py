# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

lista = []

while True:
    n = int(input('Digite um número: '))
    lista.append(n)
    r = str(input('Deseja digitar mais algo? S/N '))
    if r in 'Nn':
        break
print(f'A quantidade de números digitados foi: {len(lista)}')
lista.sort(reverse=True)
print(f'Ordem decrescente: {lista}')
if 5 in lista:
    print('O número 5 foi digitado e está na lista')
else:
    print('O valor 5 não foi encontrado.')