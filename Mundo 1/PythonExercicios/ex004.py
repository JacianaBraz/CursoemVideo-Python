# faça um programa que leia algo pelo teclado e mostre na tela seu tipo primitivo e todas as informaçãoes possíveis
# sobre ele.
desconhecido = input('Digite algo: ')
print(type(desconhecido))
print('É numérico: ',end='')
print(desconhecido.isnumeric())
print('É uma letra: ', end='')
print(desconhecido.isalpha())
print('É uma letra e/ou um número: ', end='')
print(desconhecido.isalnum())


