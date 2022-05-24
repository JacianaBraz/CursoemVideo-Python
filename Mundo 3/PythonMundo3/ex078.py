# Faça um programa que leia 5 valores númericos e guarde numa lista. No final mostre qual foi o maior e o menor digitados
# e suas respectivas posições na lista.

lista = []
for v in range(0,5):
    lista.append(int(input('Digite um número: ')))
print(lista)
print(f'O maior valor da lista é: {max(lista)} na posição  {lista.index(max(lista))+1}')
print(f'O menor valor da lista é: {min(lista)} na posição {lista.index(min(lista))+1}')
